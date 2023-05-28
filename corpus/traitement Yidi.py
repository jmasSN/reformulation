# Le script ici consiste à traiter, dans le corpus final, les caractéristiques des exemplifications,
# en détectant d'abord les statistiques tels que nb de l'attribut rel_pragm et les marqueurs
# L’emploi des marqueurs : MRE (pour le moment)
# Les relations lexicales utilisées (rel_pragm =”prec” etc..)
# Modifications morphologiques (flexion, dérivation etc)
# 	HYPOTHESE 3 : exemplifications sans MRE (ALIENOR ET ELODIE)
# HYPOTHESE 2 : Regarder aussi si les marqueurs d’exemplifications (MRE) apparaissent dans d’autres types de reformulations que les exemplifications (pourquoi est-il utilisé ? dans quel corpus il est le plus utilisé ?)
# Les exemplifications peuvent aussi être élargies aux dénominations, définitions et paraphrases (les erreurs d’annotations ?) à vérifier

import re
import matplotlib.pyplot as plt
import numpy as np


# proportion de exempl dans 3 corpus



n1,n2,n3=0,0,0
with open('corpus_final.txt', 'r') as t:

    for line in t:
        if 'rel_pragm="exempl"' in line:
            if 'corpus="masante' in line:
                n1+=1
            elif 'corpus="patient"' in line:
                n2+=1
            elif 'mod="oral"' in line:
                n3+=1
print(n1,n2,n3)
labels = ['masante','patient','oral']
valeurs = [n1,n2,n3]

plt.pie(valeurs, labels=labels, autopct='%1.1f%%')
plt.title("Proportion d'exemplifications dans 3 corpus")
plt.show()


#######################################################################################

## trouver le nb de MRE pour 3 cats
## une fonction qui traite 3 parties de corpus (masante, patient, 3oral)
import re
import matplotlib.pyplot as plt

def nb_MRE(mode):
    with open("corpus_final.txt", 'r') as fichier:
        n,s = 0,0
        for ligne in fichier:
            # chercher les modes qui indiquent le corpus et le MRE pour compter
            if re.search(fr'{mode}.*?(<MRE>)', ligne):
                n += 1
            if re.search(fr'{mode}.*?',ligne):
                s+=1
        return [n,n/s]

# attacher la valeur à chaque catégorie
nb1 =nb_MRE('corpus="masante"')
nb2 =nb_MRE('corpus="patient"')
nb3 =nb_MRE('mod="oral"')

# affichage de résultat
print(f"Nb de <MRE> dans masante : {nb1[0]}\nNb de <MRE> dans patient : {nb2[0]}\n"
      f"Nb de <MRE> dans corpus oral : {nb3[0]}\n")


# construction de graphe en barres
labels = ['masante', 'patient', 'corpus oral']
x = [0, 1, 2]
width = 0.35

nb_MRE_masante = nb1[0]
nb_MRE_patient = nb2[0]
nb_MRE_corpus_oral = nb3[0]

fig, ax = plt.subplots()
rect = ax.bar(x, [nb_MRE_masante, nb_MRE_patient, nb_MRE_corpus_oral], width)

# ajouter les étiquettes et les titres
ax.set_ylabel('Nombre de <MRE>')
ax.set_title('Nombre de <MRE> par corpus')
ax.set_xticks(x)
ax.set_xticklabels(labels)

plt.show()

print(f"Proportion de <MRE> relative : \nmasante : {nb1[1]}\n"
      f"patient : {nb2[1]}\n3 corpus oraux : {nb3[1]}\n")

#############################################################################################
# détecter les contenus de MRE et leur fréquence dans 3 corpus
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

# Charger le fichier XML
tree = ET.parse('corpus_final.xml')
root = tree.getroot()

# Compter le nombre d'apparitions de chaque contenu MRE pour chaque corpus
mre_comptes_oral = {}
mre_comptes_masante = {}
mre_comptes_patient = {}

# Parcourir toutes les balises <reformulation>
for reformulation in root.iter('reformulation'):
    # Vérifier le corpus et le mod de chaque balise <reformulation>
    corpus = reformulation.attrib.get('corpus')
    mod = reformulation.attrib.get('mod')

    # Parcourir toutes les balises <MRE> à l'intérieur de la balise <reformulation>
    for mre_element in reformulation.iter('MRE'):
        mre = mre_element.text.strip()

        # Ajouter le contenu MRE à l'approprié dictionnaire de comptage
        if mod == 'oral':
            if mre in mre_comptes_oral:
                mre_comptes_oral[mre] += 1
            else:
                mre_comptes_oral[mre] = 1
        elif corpus == 'masante':
            if mre in mre_comptes_masante:
                mre_comptes_masante[mre] += 1
            else:
                mre_comptes_masante[mre] = 1
        elif corpus == 'patient':
            if mre in mre_comptes_patient:
                mre_comptes_patient[mre] += 1
            else:
                mre_comptes_patient[mre] = 1

print(mre_comptes_oral)
print(mre_comptes_masante)
print(mre_comptes_patient)


def create_double_bar_graph(dict1, dict2, dict3, y, x, titre):
    # Get the unique keys from all dictionaries
    all_keys = set(list(dict1.keys()) + list(dict2.keys()) + list(dict3.keys()))

    # Initialize the values for all dictionaries
    values1 = []
    values2 = []
    values3 = []

    # Populate the values lists, setting missing values to zero
    for key in all_keys:
        values1.append(dict1.get(key, 0))
        values2.append(dict2.get(key, 0))
        values3.append(dict3.get(key, 0))

    # Set the positions of the bars on the x-axis
    positions = np.arange(len(all_keys))

    # Create the figure and axis objects
    fig, ax = plt.subplots()
    bar_width = 0.2

    # Plot the bars
    ax.bar(positions - bar_width, values1, width=bar_width, label='Corpus oral')
    ax.bar(positions + bar_width * 0, values2, width=bar_width, label='Corpus masante', alpha=0.5)
    ax.bar(positions + bar_width * 1, values3, width=bar_width, label='Corpus patient', alpha=0.5)

    # Set the labels and title
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(titre)

    # Set the x-axis tick labels
    ax.set_xticks(positions)
    ax.set_xticklabels(all_keys)
    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()
print(create_double_bar_graph(mre_comptes_oral,mre_comptes_masante,mre_comptes_patient,"nombre de MRE","MRE","Distribution de MRE dans 3 corpus"))

#######################################################################################
# détecter et compter les non MRE dans exemplification
# trouver leur MR (sans MRE) et leur relation lexicale
e_with_mre_count = 0
MRE_masante, MRE_patient, MRE_oral = 0, 0,0
e_without_mre_count = 0
e_without_mre_oral = 0
e_without_mre_masnate = 0
e_without_mre_patient = 0

e_oral = 0
e_masante = 0
e_patient=0

liste_mre_masante = []
liste_mre_oral = []
liste_mre_patient = []

element_counts_oral = {}
element_counts_masante = {}
element_counts_patient = {}

rel_lex_ens_masante = {}
rel_lex_ens_oral = {}
rel_lex_ens_patient = {}

pas_rel_lex = 0
rel_lex = 0

modif_morph_ens_oral = {}
modif_morph_ens_masante = {}
modif_morph_ens_patient = {}
modif_morph = 0
pas_modif_morph = 0

# ______________________________________________________________________

for r in root.findall('reformulation'):
    for segment in r:
        # On sélectionne les reformulations qui sont des exmplifications
        if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
            # On regarde les rel_lex :
            if "rel_lex" in segment.attrib:
                value_without_parentheses = re.sub(r'\([^()]+\)?', '', segment.attrib["rel_lex"])
                if r.attrib['corpus'] == "masante":
                    if value_without_parentheses.strip() not in rel_lex_ens_masante:
                        rel_lex_ens_masante[value_without_parentheses.strip()] = 1
                    else:
                        rel_lex_ens_masante[value_without_parentheses.strip()] += 1
                elif r.attrib['corpus'] == "patient":
                    if value_without_parentheses.strip() not in rel_lex_ens_patient:
                        rel_lex_ens_patient[value_without_parentheses.strip()] = 1
                    else:
                        rel_lex_ens_patient[value_without_parentheses.strip()] += 1
                else:
                    if value_without_parentheses.strip() not in rel_lex_ens_oral:
                        rel_lex_ens_oral[value_without_parentheses.strip()] = 1
                    else:
                        rel_lex_ens_oral[value_without_parentheses.strip()] += 1
                rel_lex += 1
            else:
                pas_rel_lex += 1

            ###On regarde les modif_morph
            if "modif_morph" in segment.attrib:
                value_without_parentheses = re.sub(r'\([^()]+\)?', '', segment.attrib["modif_morph"])
                if r.attrib['corpus'] == "masante":
                    if value_without_parentheses not in modif_morph_ens_masante:
                        modif_morph_ens_masante[value_without_parentheses] = 1
                    else:
                        modif_morph_ens_masante[value_without_parentheses] += 1
                elif r.attrib['corpus'] == "patient":
                    if value_without_parentheses not in modif_morph_ens_masante:
                        modif_morph_ens_patient[value_without_parentheses] = 1
                    else:
                        modif_morph_ens_patient[value_without_parentheses] += 1
                else:
                    if value_without_parentheses not in modif_morph_ens_oral:
                        modif_morph_ens_oral[value_without_parentheses] = 1
                    else:
                        modif_morph_ens_oral[value_without_parentheses] += 1
                modif_morph += 1
            else:
                pas_modif_morph += 1
            # On regarde s'il y a un marqueur d'exemplification
            if r.find('MRE') is not None:
                e_with_mre_count += 1
                mre_elem = r.find('MRE')
                # Si c'est à l'écrit, on incrémente le compteur et la liste
                if r.attrib['corpus'] == "masante":
                    e_masante += 1
                    MRE_masante += 1
                    if mre_elem.text.strip() not in liste_mre_masante:
                        liste_mre_masante.append(mre_elem.text.strip())
                elif r.attrib['corpus'] == "patient":
                    e_patient += 1
                    MRE_patient += 1
                    if mre_elem.text.strip() not in liste_mre_patient:
                        liste_mre_patient.append(mre_elem.text.strip())
                # Si c'est à l'oral, on incrémente le compteur et la liste
                else:
                    e_oral += 1
                    MRE_oral += 1
                    if mre_elem.text.strip() not in liste_mre_oral:
                        liste_mre_oral.append(mre_elem.text.strip())
            # Sinon, on sélectionne les exemplifications sans MRE
            else:
                e_without_mre_count += 1

                # Si c'est à l'écrit, on incrémente le compteur
                if r.attrib['corpus'] == "masante":
                    e_masante += 1
                    e_without_mre_masnate += 1
                    for element in r:
                        mot = element.tag
                        mot.strip()
                        if mot in (
                        'MR', 'MRP', 'MRCONC', 'MRCOR', 'MRCOR', 'MRDENOM', 'MRDESIGN', 'DA', 'DH', 'DI', 'DMD'):
                            if mot not in element_counts_masante:

                                element_counts_masante[mot] = 1
                            else:
                                mot = element.tag
                                mot.strip()
                                element_counts_masante[mot] += 1
                elif r.attrib['corpus'] == "patient":
                    e_patient += 1
                    e_without_mre_patient += 1
                    for element in r:
                        mot = element.tag
                        mot.strip()
                        if mot in (
                        'MR', 'MRP', 'MRCONC', 'MRCOR', 'MRCOR', 'MRDENOM', 'MRDESIGN', 'DA', 'DH', 'DI', 'DMD'):
                            if mot not in element_counts_patient:

                                element_counts_patient[mot] = 1

                            else:
                                element_counts_patient[mot] += 1

                # Si c'est à l'oral, on incrémente le compteur
                else:
                    e_oral += 1
                    e_without_mre_oral += 1
                    # EN COURS
                    for element in r:
                        mot = element.tag
                        mot.strip()
                        if mot in ('MR', 'MRP', 'MRCONC', 'MRCOR', 'MRCOR', 'MRDENOM', 'MRDESIGN', 'DA', 'DH', 'DI', 'DMD'):
                            if mot not in element_counts_oral:

                                element_counts_oral[mot] = 1
                            else:
                                element_counts_oral[mot] += 1

print(element_counts_masante, element_counts_oral,element_counts_patient)
print(create_double_bar_graph(element_counts_oral,element_counts_masante,element_counts_patient,"nombre de marqueurs","Marqueurs","Distribution de non MRE dans les exemplifications"))
print(create_double_bar_graph(rel_lex_ens_oral, rel_lex_ens_masante, rel_lex_ens_patient,"Nb de rel lex", "Relations lex", "Distribution de rel lex dans 3 corpus"))

#############################################################################################################
# trouver les autres rel_pragms qui contiennent MRE
def MRE_pragm_autre(type):
    with open('corpus_final.txt','r') as c :
        n = 0
        dico_type = {}
        for l in c :
            if "<MRE>" in l and 'rel_pragm="exempl' not in l:
                if type in l:
                    n += 1
                    resultats = re.findall(r"</MRE>(.*?)rel_pragm=\"([^\"]+)\"", l)

                    # pour chaque résultat trouvé, on incrémente le comptage associé dans le dictionnaire
                    for contenu, nom in resultats:
                        if nom in dico_type:
                            dico_type[nom] += 1
                        else:
                            dico_type[nom] = 1

        return dico_type, n

print("Les reformulations avec <MRE> mais qui ne sont pas l'exemplification :")
dico_masante, n1= MRE_pragm_autre('corpus="masante"')
print(f"{n1} cas dans le corpus masante : {dico_masante}")
dico_patient, n2= MRE_pragm_autre('corpus="patient"')
print(f"{n2} cas dans le corpus patient : {dico_patient}")
dico_oral, n3 = MRE_pragm_autre('mod="oral"')
print(f"{n3} cas dans les corpus ecrits : {dico_oral}")


labels = ['corpus masante', 'corpus oraux']
n_values = [n1, n2]

dico_total = {}
for k in dico_masante:
    dico_total[k] = [dico_masante[k], 0]

for k in dico_oral:
    dico_total.setdefault(k, [0, 0])
    dico_total[k][1] = dico_oral.get(k, 0)


x = np.arange(len(labels))
w = 0.2

# Dessiner les barres
for i, (k, v) in enumerate(dico_total.items()):
    plt.bar(x - w + i * w, v, width=w, label=k)

plt.xticks(x, labels)
plt.ylabel('Nb de non exemplifications avec <MRE>')
plt.legend()
plt.show()

######################################################################################
## la proportion relative d'exemplification dans 2, 3 corpus
def nb_relative_exempl():
	n1,n2,n3,n4=0,0,0,0
	with open('corpus_final.txt', 'r') as t:

	    for line in t:

		if 'rel_pragm="exempl"' in line:
		    if 'mod="ecrit"' in line:
		        n1+=1
		    elif 'mod="oral"' in line:
		        n2+=1
		if 'mod="ecrit"' in line:
		    n3+=1
		elif 'mod="oral"' in line:
		    n4+=1
	print(n1/n3,n2/n4)

	n5,n6,n7,n8,n9,n10=0,0,0,0,0,0
	with open('corpus_final.txt', 'r') as t:

	    for line in t:

		if 'rel_pragm="exempl"' in line:
		    if 'corpus="masante"' in line:
		        n5+=1
		    elif 'corpus="patient"' in line:
		        n6+=1
		    elif 'mod="oral"' in line:
		        n7+=1
		if 'corpus="masante"' in line:
		    n8+=1
		elif 'corpus="patient"' in line:
		    n9+=1
		elif 'mod="oral"' in line:
		    n10+=1
	print(n5/n8,n6/n9,n7/n10)

