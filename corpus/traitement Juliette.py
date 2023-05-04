# Comparer les exemplifications dans les 2 corpus (écrit (forum +masanté) vs oral)


import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

tree = ET.parse('corpus_final.xml')
root = tree.getroot()

"""# Nombres d'exemplifications total
exempl,reste=0,0
for child in root:
    for segment in child:
        if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
            exempl+=1
            #text = ''.join(child.itertext())
            #print(text)
    reste+=1
reste=reste-exempl

y=[]

print(f"Il y a {exempl} exemplifications sur {reste} reformulation.")

y.append(exempl)
y.append(reste)
mylabels = ["Exempl", "Reformulation"]

plt.pie(y, labels = mylabels, autopct = '%1.1f%%')
plt.show() 

# Nombres d'exemplifications par corpus

ecrit,oral=0,0
for child in root:
    if child.attrib['mod']=='ecrit':
        for segment in child:
            if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
                ecrit+=1
    else:
        for segment in child:
            if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
                oral+=1"""

# Emploie des marqueurs MRE dans exemplification : Nombre total et ecrit/oral
# HYPOTHESE 1 : MRE sont employé surtout à l'écrit car à l'oral on aura sans doute plus tendance a avoir des disfluences, une rupture plus abrupt

e_with_mre_count = 0
MRE_ecrit, MRE_oral = 0,0
e_without_mre_count = 0
liste_mre_ecrit=[]
liste_oral=[]
for r in root.findall('reformulation'):
    for segment in r:
            # On sélectionne les reformulations qui sont des exmplifications
            if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
                # On regarde s'il y a un marqueur d'exemplification
                if r.find('MRE') is not None:
                    e_with_mre_count += 1
                    mre_elem = r.find('MRE')
                    # Si c'est à l'écrit, on incrémente le compteur et la liste
                    if r.attrib['mod']=="ecrit":
                        MRE_ecrit+=1
                        if mre_elem.text.strip() not in liste_mre_ecrit:
                            liste_mre_ecrit.append(mre_elem.text.strip())
                    # Si c'est à l'oral, on incrémente le compteur et la liste
                    else:
                        MRE_oral+=1
                        if mre_elem.text.strip() not in liste_oral:
                            liste_oral.append(mre_elem.text.strip())
                else:
                    e_without_mre_count += 1

print(liste_mre_ecrit)
print(liste_oral)
print(f"Nombre d'exemplification avec <MRE>: {e_with_mre_count}")
print(f"Nombre d'exemplification sans <MRE>: {e_without_mre_count}")
print(f"Nombre de <MRE> à l'oral: {MRE_oral}")
print(f"Nombre de <MRE> à l'écrit: {MRE_ecrit}")



"""La comparaison va porter sur (ON VEUT COMPRENDRE LE LIEN ENTRE CE QUI EST DENOMME ET L’EXEMPLE)
L’emploi des marqueurs : MRE (pour le moment)
Les relations lexicales utilisées (rel_pragm =”prec” etc..)
Modifications morphologiques (flexion, dérivation etc)
	HYPOTHESE 3 : exemplifications sans MRE (ALIENOR ET ELODIE)
HYPOTHESE 2 : Regarder aussi si les marqueurs d’exemplifications (MRE) apparaissent dans d’autres types de reformulations que les exemplifications (pourquoi est-il utilisé ? dans quel corpus il est le plus utilisé ?)
Les exemplifications peuvent aussi être élargies aux dénominations, définitions et paraphrases (les erreurs d’annotations ?) à vérifier
Toutes les remarques et les observations sont importantes.
Pour élargir les données ; on peut annoter le forum (ou une partie du forum) : forum-hta (problèmes cardiaques)"""


