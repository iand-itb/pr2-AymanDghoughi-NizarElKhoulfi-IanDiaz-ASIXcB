'''
Ayman Dghoughi, Nizar El Khoulfi, Ian Diaz
11/10/23
ASIXc M03 UF1 A2
Descripció: Programa per calcular la superfície d'una pizza a partir del diàmetre
'''

#Demanem al usuari els diferents valors per poder calcular el volum
print("Amplada de l'habitació?")
#Agafem el valor i el convertim a float
amplada = float(input())

#Demanem al usuari els diferents valors per poder calcular el volum
print("Llargada de l'habitació?")
#Agafem el valor i el convertim a float
llargada = float(input())

#Demanem al usuari els diferents valors per poder calcular el volum
print("Alçada de l'habitació?")
#Agafem el valor i el convertim a float
alcada = float(input())

#Fem el calcul amb el valors agafats (apliquem la formula del volum)
volumen = float(amplada * llargada * alcada)

#Mostrem en pantalla la frase amb el resultat en m³
print(f"El volum de l'aula és {volumen:.2f} m³")

