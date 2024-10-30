"""
Ime studenta, podatak koliko student ima kolegija na godini, ocjene tih kolegija, prosjek
"""

#Greet
print("Online kalkulator prosjeka")
ime_studenta = input("Unesite vaše ime (E.g: Joe Doe): ")
broj_kolegija = int(input("Koliko imate kolegija: ")) #n 
ocjene = []

for i in range(1, broj_kolegija +1):
  ocjena = int(input("Unesite vašu ocjenu")) 
  #print(ocjena)
  #Validacija prije upisa u listu
  if ocjena >= 1 and ocjena <= 5:
    ocjene.append(ocjena)
  else:
    print("Korisniče van raspona ste ! (1-5)")
    i = i - 1
  #print(ocjene)
  


#Racunamo prosjek
prosjek = sum(ocjene) / len(ocjene)

print(f"Korisniče {ime_studenta} vaš prosjek ocjena je {prosjek}")