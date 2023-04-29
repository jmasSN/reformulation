# **************************************************************************** #
#                                                                              
#    extraction_reformulation.py                                           
#                                                     
#    By: @juliette, @yidi             
#
#    Created: 2023/04/07 11:20:09                         
#    Updated: 2023/04/20 18:27:59                         
#                                                                              
# **************************************************************************** #

import argparse
import xml.etree.ElementTree as ET
import re


# Appel en ligne de commande __________________________________________________
# Récupération du fichier à trier
argParser = argparse.ArgumentParser()

# Création argument obligatoire : nom du fichier XML à traiter
argParser.add_argument('filename', help="fichier TXT à traiter")
args = argParser.parse_args()

fichier_traite = args.filename

#_____________________________________________________________________________


with open(fichier_traite,'r') as t:
        text = t.read()
        reformulations = re.findall(r'<reformulation>(.*?)</reformulation>', text, re.DOTALL)
with open("sortie.xml","w") as f:
        f.write("<body>\n")
        for reformulation in reformulations:
                f.write(f"<reformulation>{reformulation}</reformulation>\n")
        f.write("</body>\n")