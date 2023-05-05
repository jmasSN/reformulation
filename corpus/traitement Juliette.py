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
e_without_mre_oral = 0
e_without_mre_ecrit = 0

e_oral=0
e_ecrit=0

liste_mre_ecrit=[]
liste_mre_oral=[]

element_counts={}
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

