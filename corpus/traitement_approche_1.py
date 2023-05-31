# COMPARAISON DES EXEMPLIFICATIONS DANS LES CORPUS ÉCRITS ET ORAUX

import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import re
import numpy as np
from matplotlib.ticker import FuncFormatter


tree = ET.parse('corpus_final.xml')
root = tree.getroot()

#_____________________________________VARIABLES _____________________________________________

liste_mr=['MR', 'MRP','MRCONC','MRCOR','MRCOR','MRDENOM','MRDESIGN','DA','DH','DI','DMD']


e_with_mre_count = 0
MRE_ecrit, MRE_oral = 0,0
e_without_mre_count = 0
e_without_mre_oral = 0
e_without_mre_ecrit = 0

e_oral=0
e_ecrit=0

liste_mre_ecrit=[]
liste_mre_oral=[]

element_counts_oral={}
element_counts_ecrit={}

rel_lex_ens_ecrit={}
rel_lex_ens_oral={}

pas_rel_lex_oral,pas_rel_lex_ecrit=0,0
rel_lex_oral,rel_lex_ecrit=0,0

modif_morph_ens_oral={}
modif_morph_ens_ecrit={}
modif_morph=0
pas_modif_morph=0
reformulation_ecrit,reformulation_oral=0,0

#______________________________________________________________________

# On parcoure les reformulations :
for r in root.findall('reformulation'):
    if r.attrib['mod']=="ecrit":
         reformulation_ecrit+=1
    else:
        reformulation_oral+=1
    for segment in r:
            # On sélectionne les reformulations qui sont des exemplifications
            if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
                # On regarde les rel_lex :
                if "rel_lex" in segment.attrib:
                    value_without_parentheses = re.sub(r'\([^()]+\)?','', segment.attrib["rel_lex"])
                    if r.attrib['mod']=="ecrit":
                        rel_lex_ecrit+=1
                        if value_without_parentheses.strip() not in rel_lex_ens_ecrit:
                            rel_lex_ens_ecrit[value_without_parentheses.strip()] = 1
                        else:
                            rel_lex_ens_ecrit[value_without_parentheses.strip()] += 1
                    else:
                        rel_lex_oral+=1
                        if value_without_parentheses.strip() not in rel_lex_ens_oral:
                            rel_lex_ens_oral[value_without_parentheses.strip()] = 1
                        else:
                            rel_lex_ens_oral[value_without_parentheses.strip()] += 1
                else :
                    if r.attrib['mod']=="ecrit":
                        pas_rel_lex_ecrit+=1
                    else:
                        pas_rel_lex_oral+=1
                ###On regarde les modif_morph
                if "modif_morph" in segment.attrib:
                    value_without_parentheses = re.sub(r'\([^()]+\)?','', segment.attrib["modif_morph"])
                    if r.attrib['mod']=="ecrit":
                        if value_without_parentheses.strip() not in modif_morph_ens_ecrit:
                            modif_morph_ens_ecrit[value_without_parentheses.strip()] = 1
                        else:
                            modif_morph_ens_ecrit[value_without_parentheses.strip()] += 1
                    else:
                        if value_without_parentheses not in modif_morph_ens_oral:
                            modif_morph_ens_oral[value_without_parentheses.strip()] = 1
                        else:
                            modif_morph_ens_oral[value_without_parentheses.strip()] += 1
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
                        for element in r:
                            mot=element.tag
                            mot.strip()
                            if element.tag in liste_mr:
                                if element.tag not in element_counts_ecrit:
                                    element_counts_ecrit[mot] = 1
                                else:
                                    element_counts_ecrit[mot] += 1
                    # Si c'est à l'oral, on incrémente le compteur
                    else:
                        e_oral+=1
                        e_without_mre_oral +=1
                        for element in r:
                            mot=element.tag
                            mot.strip()
                            if element.tag in liste_mr:
                                if mot not in element_counts_oral:
                                    element_counts_oral[mot] = 1
                                else:
                                    element_counts_oral[mot] += 1

            


#_____________________CALCUL DES POURCENTAGES POUR LES DICTIONNAIRES______________________________________________________________

def calculate_value_percentages(dictionary):
    total_sum = sum(dictionary.values())
    percentages = {key: (value / total_sum) * 100 for key, value in dictionary.items()}
    return percentages
MRE_ecrit_pourcent = calculate_value_percentages(element_counts_ecrit)
MRE_oral_pourcent = calculate_value_percentages(element_counts_oral)
rel_lex_ens_ecrit = calculate_value_percentages(rel_lex_ens_ecrit)
rel_lex_ens_oral = calculate_value_percentages(rel_lex_ens_oral)


def transform_dictionaries(dict1, dict2):
    all_keys = list(set(dict1.keys()) | set(dict2.keys()))
    values1 = [dict1.get(key, 0) for key in all_keys]
    values2 = [dict2.get(key, 0) for key in all_keys]
    return all_keys, values1, values2
keys, values1, values2=transform_dictionaries(MRE_ecrit_pourcent,MRE_oral_pourcent)
keys1, values3, values4=transform_dictionaries(rel_lex_ens_ecrit,rel_lex_ens_oral)


      
      
#_______________________CREATION DES DIAGRAMMES_______________________________________________________________
def create_double_bar_graph(dict1, dict2,y,x,titre):
    
    all_keys = set(list(dict1.keys()) + list(dict2.keys()))

    values1 = []
    values2 = []

    for key in all_keys:
        values1.append(dict1.get(key, 0))
        values2.append(dict2.get(key, 0))


    positions = np.arange(len(all_keys))

    fig, ax = plt.subplots()
    bar_width = 0.4
    ax.bar(positions - bar_width/2, [dict1.get(key, 0) for key in all_keys], width=bar_width, label='Corpus oral')
    ax.bar(positions + bar_width/2, [dict2.get(key, 0) for key in all_keys], width=bar_width, label='Corpus écrit', alpha=0.5)

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(titre)

    ax.set_xticks(positions)
    ax.set_xticklabels(all_keys)

    ax.legend()
    plt.show()

def create_double_bar_chart(categories, percentages1, percentages2, title,nom_x,nom_y):

    x = np.arange(len(categories))


    bar_width = 0.35
    fig, ax = plt.subplots()

    ax.bar(x - bar_width/2, percentages1, bar_width, label=nom_x)

    ax.bar(x + bar_width/2, percentages2, bar_width, label=nom_y)

    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)

    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y/100)))

    ax.legend()

    return ax

#chart = create_double_bar_chart(['Pourcentages d\'exemplifications'],[100*(e_oral/reformulation_oral)], [100*(e_ecrit/reformulation_ecrit)], 'Pourcentages d\'exemplifications dans les corpus','Oral','Écrit')
#chart = create_double_bar_chart(['Avec MRE','Sans MRE'],[100*(MRE_oral/e_oral),100*(e_without_mre_oral/e_oral)], [100*(MRE_ecrit/e_ecrit),100*(e_without_mre_ecrit/e_ecrit)], 'Pourcentages d\'exemplifications avec et sans MRE dans les corpus','Oral','Écrit')
#chart = create_double_bar_chart(keys,values2, values1, 'Pourcentages de marqueurs non MRE dans les corpus','Oral','Écrit')
#chart = create_double_bar_chart(['Avec rel lex'],[100*(rel_lex_oral/(rel_lex_oral+pas_rel_lex_oral))],[100*(rel_lex_ecrit/(rel_lex_ecrit+pas_rel_lex_ecrit))], 'Pourcentages des relations lexicales les corpus','Oral','Écrit')
#chart = create_double_bar_chart(keys1,values3, values4, 'Pourcentages des relations lexicales les corpus','Oral','Écrit')

plt.show()


#create_double_bar_graph(element_counts_oral, element_counts_ecrit)

#______________________________________________________________________________________)

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
