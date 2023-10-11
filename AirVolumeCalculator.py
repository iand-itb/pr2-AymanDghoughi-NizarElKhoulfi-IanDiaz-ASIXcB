'''
Ayman Dghoughi, Nizar ElKhoulfi, Ian Diaz
M03 UF1
Calcular el volum d'una habitació a partir de les 3 dimensions
11/10/23
'''

print("Amplada de l'habitació?")
amplada = float(input())
print("Llargada de l'habitació?")
llargada = float(input())
print("Alçada de l'habitació?")
alcada = float(input())

volumen = float(amplada * llargada * alcada)

print(f"El volum de l'aula és {volumen:.2f} m³")

