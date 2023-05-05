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


import re
import matplotlib.pyplot as plt

with open('corpus_final.txt','r') as t:
    text = t.read()

# Trouver ce qui est dans les balises MRE
mre_regex = r'<MRE>(.*?)</MRE>'
resultats = re.findall(mre_regex, text)

# Compter le nombre d'apparitions de chaque contenu MRE
mre_comptes = {}
for resultat in resultats:
    if resultat in mre_comptes:
        mre_comptes[resultat] += 1
    else:
        mre_comptes[resultat] = 1

# Créer un pie chart de proportion basé sur les valeurs du dictionnaire
labels = mre_comptes.keys()
valeurs = mre_comptes.values()

plt.pie(valeurs, labels=labels, autopct='%1.1f%%')
plt.title("Proportion des contenus <MRE> dans le corpus")
plt.show()
print(len(mre_comptes.keys()),"types de <MRE> :",mre_comptes,"\n")

#######################################################################################
## trouver les exemplification avec et sans <MRE>
with open("corpus_final.txt",'r') as f :
    i,j=0,0
    # créer une liste dont chaque élé est une ligne
    lines=f.readlines()
    for line in lines:
        # chercher les lignes d'exemplification
        if 'rel_pragm="exempl"' in line:
            # mettre les cas avec <MRE> dans le compteur i
            if '<MRE>' in line:
                i+=1
            # mettre les cas inverse dans le compteur j
            else:
                j+=1

    # créer une liste de labels et une liste de données pour label
    labels = ['Exempl avec <MRE>', 'Exempl sans <MRE>']
    sizes = [i,j]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.title("Proportion d'exemplifications avec ou sans <MRE>")
    plt.show()
    print(f"Nb d'exemplifications avec <MRE> : {i} \n"
          f"Nb d'exemplifications sans <MRE> : {j}\n")


########################################################################################
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

#########################################################################

## chercher les cas avec <MRE> mais qui n'ont pas de relation exempl
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

