# Comparer les exemplifications dans les 2 corpus (écrit (forum +masanté) vs oral)


import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

tree = ET.parse('corpus_final.xml')
root = tree.getroot()

# Nombres d'exemplifications total
exempl,reste=0,0
for child in root:
    for segment in child:
        if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
            exempl+=1
            text = ''.join(child.itertext())
            print(text)
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
    if child.attrib['mod']=='oral':
        for segment in child:
            if "rel_pragm" in segment.attrib and segment.attrib["rel_pragm"] == 'exempl':
                oral+=1


refo=[]

print(f"Il y a {ecrit} exemplifications dans les corpus écrit contre {oral} reformulation à l'oral.")

refo.append(ecrit)
refo.append(oral)
mylabel = ["Ecrit", "Oral"]

plt.pie(y, labels = mylabel, autopct = '%1.1f%%')
plt.show() 