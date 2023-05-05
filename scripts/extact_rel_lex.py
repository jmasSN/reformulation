import xml.etree.ElementTree as ET

les_fichiers_oraux = ['sortie5.xml', 'sortie33.xml', 'sortie53.xml']


for nom_fichier in les_fichiers_oraux:
#on utilise la méthode parse pour analyser le fichier xml stocké dans la variable nom_fichier et on stocke l'arbre xml extrait dans la variable arbre. 
    arbre = ET.parse(nom_fichier)
#on utilise la méthode getroot pour extraire la racine de l'arbre xml et la stocker dans la variable racine. 
    racine = arbre.getroot()
    
#on ouvre le fichier qui contiendra les balises rel_lex en sortie.
    with open(nom_fichier + '_relations_lexicales.xml', 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        #on écrit une balise d'ouverture racine dans le fichier de sortie.
        f.write('<racine>\n')

#la boucle for parcourt tous les éléments de l'arbre avec la méthode .iter et ce, depuis la racine de l'arbre xml. 
        for element in racine.iter():
        #si il vérifie si il y a l'attribut rel_lex et si il le trouve, il l'écrit dans le fichier de sortie.
            if 'rel_lex' in element.attrib:
            #la méthode .trosting permet de spécifier l'encodage et de retourner des caractères qui seraient non ASCII.
                f.write(ET.tostring(elem, encoding='unicode'))
                     
        #on écrit une balise de fermeture dans le fichier de sortie.
        f.write('</racine>\n')

