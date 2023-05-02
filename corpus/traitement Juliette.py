import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

tree = ET.parse('ecrit.xml')
root = tree.getroot()



patient,masante=0,0
y=[]

for child in root:
    if child.attrib['forum'] == "patient":
        patient +=1
    else:
        masante+=1
y.append(patient)
y.append(masante)
mylabels = ["Forum patient", "Forum Masante"]

plt.pie(y, labels = mylabels, autopct = '%1.1f%%')
plt.show() 