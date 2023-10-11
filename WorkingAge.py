'''
Ayman Dghoughi, Nizar ElKhoulfi, Ian Diaz
ASIXc M03 UF1 A2
Descripció: Llegeixi l'edat de l'usuari i mostri si té edat per treballar
11/10/23
'''

edat = int(input("Quina edat tens? "))

if edat >= 16 and edat <= 65:
    print("Apte per treballar")
else:
    print("No apte per treballar")