"""
Unijeti ime studenta. unositi ocjene i racunamo prosjek za njega 
"""

#Korisnik prvo unosi ime, zatim  prosjek, ispisemo

print("Online kalkulator prosjeka")
ime_studenta = input("Unesite vaše ime (E.g: Joe Doe): ")
print(f"Dobrodošao {ime_studenta} u naš program !")
print("Unesite svoje ocjene iz kolegija od 1-5")
kolegij_jedan = int(input("Unesite ocjenu 1/5:"))
kolegij_dva = int(input("Unesite ocjenu 2/5:"))
kolegij_tri = int(input("Unesite ocjenu 3/5:"))
kolegij_cet = int(input("Unesite ocjenu 4/5:"))
kolegij_pet = int(input("Unesite ocjenu 5/5:"))

prosjek = (kolegij_jedan + kolegij_dva + kolegij_tri + kolegij_cet + kolegij_pet) /5
print(f"Vaš prosjek je {prosjek}")

# Izvanredni metoda s petljama






