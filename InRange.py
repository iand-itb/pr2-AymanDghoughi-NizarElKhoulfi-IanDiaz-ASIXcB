'''
Ayman Dghoughi, Nizar ElKhoulfi, Ian Diaz
M03 UF1
Mostra True si el cinquè valor, està comprès dins els dos rangs
11/10/23
'''

#Agafem l'input de l'usuari i el guardem en un array
valors = list(map(int, input("Introdüeix 5 valors separats per un espai...\n").split(" ")))

if valors[4] in range(valors[0], valors[1]) and range(valors[2], valors[3]):
    print("True")
else:
    print("False")