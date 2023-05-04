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
print(len(mre_comptes.keys()),"types de <MRE> :",mre_comptes)

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
          f"Nb d'exemplifications sans <MRE> : {j}")


########################################################################################
## trouver le nb de MRE pour 3 cats
## une fonction qui traite 3 parties de corpus (masante, patient, 3oral)
def nb_MRE(mode):
    with open("corpus_final.txt", 'r') as fichier:
        n = 0
        for ligne in fichier:
            # chercher les modes qui indiquent le corpus et le MRE pour compter
            if re.search(fr'{mode}.*?(<MRE>)', ligne):
                n += 1
        return n

# attacher la valeur à chaque catégorie
nb1 =nb_MRE('corpus="masante"')
nb2 =nb_MRE('corpus="patient"')
nb3 =nb_MRE('mod="oral"')

# affichage de résultat
print("Nb de <MRE> dans masante :", nb1)
print("Nb de <MRE> dans patient :", nb2)
print("Nb de <MRE> dans corpus oral :", nb3)

# construction de pie chart
labels = ['<MRE> dans masante', '<MRE> dans patient', '<MRE> dans 3 corpus oraux']
sizes = [nb1, nb2,nb3]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Proportion de <MRE> dans 3 corpus")
plt.show()






