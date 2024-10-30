#15.	Napišite program koji ispisuje sve parne brojeve od 1 do 20.

#Pseudocod: do 20, nakon djeljenja moramo provjeriti je li ostatak jednak 0, ispis parnih brojeva

for i in range(1,20 + 1):
  # izraz = i % 2
  if i % 2 == 0:
    print(f"Ovo je parni broj {i}")
  else:
    print(f"Ovo je neparni broj {i}")