# Comparer les exemplifications dans les 2 corpus (écrit (forum +masanté) vs oral)


import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import re

tree = ET.parse('corpus_final.xml')
root = tree.getroot()

# Emploie des marqueurs MRE dans exemplification : Nombre total et ecrit/oral
# HYPOTHESE 1 : MRE sont employé surtout à l'écrit car à l'oral on aura sans doute plus tendance a avoir des disfluences, une rupture plus abrupt


#Variables ___________________________________________________________
e_with_mre_count = 0
MRE_ecrit, MRE_oral = 0,0
e_without_mre_count = 0
e_without_mre_oral = 0
e_without_mre_ecrit = 0

e_oral=0
e_ecrit=0

liste_mre_ecrit=[]
liste_mre_oral=[]

element_counts={}

rel_lex_ens_ecrit={}
rel_lex_ens_oral={}

pas_rel_lex=0
rel_lex=0

modif_morph_ens_oral={}
modif_morph_ens_ecrit={}
modif_morph=0
pas_modif_morph=0

#______________________________________________________________________

for r in root.findall('reformulation'):
    for segment in r:
            # On sélectionne les reformulations qui sont des exmplifications
            if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
                # On regarde les rel_lex :
                if "rel_lex" in segment.attrib:
                    value_without_parentheses = re.sub(r'\([^()]+\)?','', segment.attrib["rel_lex"])
                    if r.attrib['mod']=="ecrit":
                        if value_without_parentheses not in rel_lex_ens_ecrit:
                            rel_lex_ens_ecrit[value_without_parentheses] = 1
                        else:
                            rel_lex_ens_ecrit[value_without_parentheses] += 1
                    else:
                        if value_without_parentheses not in rel_lex_ens_oral:
                            rel_lex_ens_oral[value_without_parentheses] = 1
                        else:
                            rel_lex_ens_oral[value_without_parentheses] += 1
                    rel_lex+=1
                else :
                    pas_rel_lex+=1
                ###
                if "modif_morph" in segment.attrib:
                    value_without_parentheses = re.sub(r'\([^()]+\)?','', segment.attrib["modif_morph"])
                    if r.attrib['mod']=="ecrit":
                        if value_without_parentheses not in modif_morph_ens_ecrit:
                            modif_morph_ens_ecrit[value_without_parentheses] = 1
                        else:
                            modif_morph_ens_ecrit[value_without_parentheses] += 1
                    else:
                        if value_without_parentheses not in modif_morph_ens_oral:
                            modif_morph_ens_oral[value_without_parentheses] = 1
                        else:
                            modif_morph_ens_oral[value_without_parentheses] += 1
                    modif_morph+=1
                else :
                    pas_modif_morph+=1
                # On regarde s'il y a un marqueur d'exemplification
                if r.find('MRE') is not None:
                    e_with_mre_count += 1
                    mre_elem = r.find('MRE')
                    # Si c'est à l'écrit, on incrémente le compteur et la liste
                    if r.attrib['mod']=="ecrit":
                        e_ecrit+=1
                        MRE_ecrit+=1
                        if mre_elem.text.strip() not in liste_mre_ecrit:
                            liste_mre_ecrit.append(mre_elem.text.strip())
                    # Si c'est à l'oral, on incrémente le compteur et la liste
                    else:
                        e_oral+=1
                        MRE_oral+=1
                        if mre_elem.text.strip() not in liste_mre_oral:
                            liste_mre_oral.append(mre_elem.text.strip())
                #Sinon, on sélectionne les exemplifications sans MRE
                else:
                    e_without_mre_count += 1
                    
                    # Si c'est à l'écrit, on incrémente le compteur
                    if r.attrib['mod']=="ecrit":
                        e_ecrit+=1
                        e_without_mre_ecrit += 1
                        #for element in r:
                            #if element.tag in ('MR', 'MRP','MRCONC','MRCOR','MRCOR','MRDENOM','MRDESIGN','DA','DH','DI','DMD'):
                                #print(element.tag,element.text)
                    # Si c'est à l'oral, on incrémente le compteur
                    else:
                        e_oral+=1
                        e_without_mre_oral +=1
                        #EN COURS
                        for element in r:
                            if element.tag in ('MR', 'MRP','MRCONC','MRCOR','MRCOR','MRDENOM','MRDESIGN','DA','DH','DI','DMD'):
                                if element.tag not in element_counts:
                                    element_counts[element.tag] = 1
                                else:
                                    element_counts[element.tag] += 1
                                                
print(rel_lex_ens_ecrit,rel_lex_ens_oral)
rel_nom_list_oral = list(rel_lex_ens_oral.values())
rel_nb_list_oral = list(rel_lex_ens_oral.keys())
plt.pie(rel_nom_list_oral, labels=rel_nb_list_oral, autopct='%1.1f%%')

# Add a title
plt.title('Distribution des relations lexicales à l\'oral')

# Display the chart
plt.show()

###################################

rel_nom_list_ecrit = list(rel_lex_ens_ecrit.values())
rel_nb_list_ecrit = list(rel_lex_ens_ecrit.keys())
plt.pie(rel_nom_list_ecrit, labels=rel_nb_list_ecrit, autopct='%1.1f%%')
# Add a title
plt.title('Distribution des relations lexicales à l\'écrit')

# Display the chart
plt.show()
###################################

rel_lex_nb = [pas_rel_lex,rel_lex]
rel_lex_nb_nom = ['Sans rel_lex','Avec rel_lex']
plt.pie(rel_lex_nb, labels=rel_lex_nb_nom, autopct='%1.1f%%')
# Add a title
plt.title('Distribution des relations lexicales')

# Display the chart
plt.show()


################################

modif_morph_nb = [pas_modif_morph,modif_morph]
modif_morph_nom = ['Sans modif morph','Avec modif_morph']
plt.pie(modif_morph_nb, labels=modif_morph_nom, autopct='%1.1f%%')
# Add a title
plt.title('Distribution des modifications lexicales')

# Display the chart
plt.show()

print(element_counts)
print(liste_mre_ecrit)
print(liste_mre_oral)
print("\nNombre total d'exemplifications : ",e_without_mre_count+e_with_mre_count)
print("________________________________________________")
print(f"Nombre d'exemplification à l'oral: {e_oral}")
print(f"Nombre d'exemplification à l'écrit: {e_ecrit}")
print("________________________________________________")
print(f"Nombre d'exemplification avec <MRE>: {e_with_mre_count}")
print(f"Nombre d'exemplification sans <MRE>: {e_without_mre_count}")
print("________________________________________________")
print(f"Nombre d'exemplification avec <MRE> à l'oral: {MRE_oral}")
print(f"Nombre d'exemplification avec <MRE> à l'écrit: {MRE_ecrit}")
print("________________________________________________")
print(f"Nombre d'exemplification sans <MRE> à l'oral: {e_without_mre_oral}")
print(f"Nombre d'exemplification sans <MRE> à l'écrit: {e_without_mre_ecrit}")

"""La comparaison va porter sur (ON VEUT COMPRENDRE LE LIEN ENTRE CE QUI EST DENOMME ET L’EXEMPLE)
L’emploi des marqueurs : MRE (pour le moment)
Les relations lexicales utilisées (rel_pragm =”prec” etc..)
Modifications morphologiques (flexion, dérivation etc)
	HYPOTHESE 3 : exemplifications sans MRE (ALIENOR ET ELODIE)
HYPOTHESE 2 : Regarder aussi si les marqueurs d’exemplifications (MRE) apparaissent dans d’autres types de reformulations que les exemplifications (pourquoi est-il utilisé ? dans quel corpus il est le plus utilisé ?)
Les exemplifications peuvent aussi être élargies aux dénominations, définitions et paraphrases (les erreurs d’annotations ?) à vérifier
Toutes les remarques et les observations sont importantes.
Pour élargir les données ; on peut annoter le forum (ou une partie du forum) : forum-hta (problèmes cardiaques)"""

