'''
Ayman Dghoughi, Nizar ElKhoulfi, Ian Diaz
M03 UF1
Calcular el volum d'una habitació a partir de les 3 dimensions
11/10/23
'''

print("Amplada de l'habitació?")
amplada = int(input())
print("Llargada de l'habitació?")
llargada = int(input())
print("Alçada de l'habitació?")
alcada = int(input())

volumen = int(amplada * llargada * alcada)

print("El volum de l'aula és " + str(volumen) + "m³")

