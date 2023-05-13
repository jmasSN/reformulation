'''

@Alienor @Elodie le 2 Mai 2023

'''


#code pour extraire les catégories de modifieurs du segment 1. 

import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

tree = ET.parse('chemin/xml')
root = tree.getroot()

#les compteurs
np_nb = 0
vp_nb = 0
ap_nb = 0
pp_nb = 0
a_nb = 0
adv_nb = 0
n_nb = 0 
pres_nb = 0
pr_nb = 0 
ger_nb = 0 



for element in root.iter():
    # Vérification du type de l'élément en fonction de son tag
    if element.tag == 'NP1':
        np_nb += 1
    elif element.tag == 'VP1':
        vp_nb += 1
    elif element.tag == 'AP1':
        ap_nb += 1
    elif element.tag == 'PP1':
        pp_nb += 1
    elif element.tag == 'A1':
        a_nb += 1
    elif element.tag == 'ADV1':
        adv_nb += 1
    elif element.tag == 'N1':
        n_nb += 1
    elif element.tag == 'PRES1':
        pres_nb += 1
    elif element.tag == 'Pr1':
        pr_nb += 1
    elif element.tag == 'Ger1':
        ger_nb += 1

#calcule
total_nb = np_nb + vp_nb + ap_nb + pp_nb + a_nb + adv_nb + n_nb + pres_nb + pr_nb + gr_nb
np_pct = np_nb / total_nb * 100
vp_pct = vp_nb / total_nb * 100
ap_pct = ap_nb / total_nb * 100
pp_pct = pp_nb / total_nb * 100
a_pct = a_nb / total_nb * 100
adv_pct = adv_nb / total_nb * 100
n_pct = n_nb / total_nb * 100
pres_pct = pres_nb / total_nb * 100
pr_pct = pr_nb / total_nb * 100
ger_pct = ger_nb / total_nb * 100

#le pie chart
labels = ['NP1', 'VP1', 'AP1', 'PP1','A1', 'ADV1', 'N1', 'PRES1', 'Pr1', 'Gr1']
sizes = [a_pct, adv_pct, n_pct, pres_pct, pr_pct, ger_pct]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'orange', 'purple', ]
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Répartition des catégories syntaxiques seules pour les segments reformulés')
plt.show()


