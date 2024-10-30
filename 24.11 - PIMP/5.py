# Korisnik unosi svoje, unosi godinu rođenja =>2000 mlad, <2000 star

ime = input("Unesite vaše ime:")
godina_rodenja = int(input("Unesite vašu godinu rodenja: "))

if godina_rodenja > 2000:
  print("Vi ste mladi")
elif godina_rodenja < 2000:
  print("Vi ste stari") 
elif godina_rodenja == 2000: print("Vi ste rodeni u zanimljivo vrijeme")
