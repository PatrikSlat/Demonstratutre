"""Potrebno je unijeti dimenzije sobe. te ispisati kolika je površine parketa potrebno kupiti. 
Kod kupnje parketa treba kupiti barem 15% više nego što  je površina prostora. 
Ispisati koliko metara kvardtatnih parketa treba kupiti. 
 """ 

#Potrebno je unijeti dimenzije sobe
duzina_sobe = float(input("Unesite dužinu sobe (u metrima): "))
sirina_sobe = float(input("Unesite sirinu sobe (u metrima): "))

povrsina_sobe = (duzina_sobe * sirina_sobe) *1.15
print(f"Potrebno je kupiti {povrsina_sobe}")
