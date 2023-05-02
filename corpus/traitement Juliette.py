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

# MR d'exemplification (absent ou présents disfluences...) et repartition et nature

nb_ecrit_MRE,nb_ecrit_sans_MRE=0,0
nb_oral_MRE,nb_oral_sans_MRE=0,0
for reformulation in root.findall('reformulation'):
    mre_elem = reformulation.find('MRE')
    if mre_elem is not None and mre_elem.text is not None:
        if reformulation.attrib['mod']=="ecrit":
            mre = mre_elem.text
            print(mre)
            nb_ecrit_MRE+=1
        else:
            nb_oral_MRE+=1
    else:
        print("MRE element not found or has no text content")

print(nb_oral_MRE,nb_ecrit_MRE)

