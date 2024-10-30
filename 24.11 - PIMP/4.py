"""
2.	Napišite program koji izračunava razliku između dva broja.
3.	Napišite program koji množi dva broja. -> promjeni iz minus u *
4.	Napišite program koji dijeli dva broja i ispisuje rezultat cjelobrojnog dijeljenja. -> promjeni iz minus u //
5.	Napišite program koji izračunava ostatak pri dijeljenju dva broja. -> promjeni iz minus u %
"""


#2

broj_jedan = float(input("Unesite prvi broj: ")) #2.0 -> int 2
broj_dva = float(input("Unesite drugi broj: "))  #1.0 -> int 1

print(f"Razlika između dva broja {broj_jedan} i {broj_dva} je: {broj_jedan % broj_dva}")