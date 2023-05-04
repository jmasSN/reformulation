# Le script ici consiste à traiter, dans le corpus final, les caractéristiques des exemplifications,
# en détectant d'abord les statistiques tels que nb de l'attribut rel_pragm et les marqueurs
# L’emploi des marqueurs : MRE (pour le moment)
# Les relations lexicales utilisées (rel_pragm =”prec” etc..)
# Modifications morphologiques (flexion, dérivation etc)
# 	HYPOTHESE 3 : exemplifications sans MRE (ALIENOR ET ELODIE)
# HYPOTHESE 2 : Regarder aussi si les marqueurs d’exemplifications (MRE) apparaissent dans d’autres types de reformulations que les exemplifications (pourquoi est-il utilisé ? dans quel corpus il est le plus utilisé ?)
# Les exemplifications peuvent aussi être élargies aux dénominations, définitions et paraphrases (les erreurs d’annotations ?) à vérifier

import re

with open('corpus_final.txt','r') as t :
    text=t.read()

## trouver ce qui est dans les balises MRE
    # l'expression pour trouver le contenu au milieu
    mre=r'<MRE>(.*?)</MRE>'
    resultat=re.findall(mre,text)

    contenus=[]
    # garder les expressions dans la liste en limitant les répétition
    for mre in resultat:
        if mre not in contenus:
            contenus.append(mre)
    print(f"{len(contenus)} MRE : {contenus}")

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
    print(f"Nb d'exemplifications avec <MRE> : {i} \n"
          f"Nb d'exemplifications sans <MRE> : {j}")

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
print("Nb de MRE dans masante :", nb_MRE('corpus="masante"'))
print("Nb de MRE dans patient :", nb_MRE('corpus="patient"'))
print("Nb de MRE dans corpus oral :", nb_MRE('mod="oral"'))






