# Convertir n'importe quelle unité en une autre

def convertisseur(unit1: str, unit2: str, facteurdeconversion:  float):
    valeur_str  = input(f"Donnez la valeur à convertir en {unit1} : ")
    valeur_convertie = round(float(valeur_str) * facteurdeconversion ,2)
    print (f"La conversion donne :  {valeur_str} {unit1} = {valeur_convertie} {unit2}")

print("Bonjour; vous voulez convertir des unités de mesure")
print("tapez 1 pour convertir des pouces en cm")
print("tapez 2 pour convertir des cms en pouces")
print("tapez 3 pour convertir des ha en m2")
print("tapez 4 pour convertir des m2 en ha")

choice = input("Votre choix (1, 2, 3 ou 4): ")

if choice == "1":  
    convertisseur("pouces", "cm", 2.54)
if choice == "2":  
    convertisseur("cm", "pouces", 0.394)   
if choice == "3":  
    convertisseur("ha", "m2", 10000)
if choice == "4":  
    convertisseur("m2", "ha", 0.0001)