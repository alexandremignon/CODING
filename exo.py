def convertir_to_cm(valeur, unite):
    if unite.lower() == 'pouces':
        return valeur * 2.54
    elif unite.lower() == 'cm':
        return valeur
    else:
        return None

def determiner_categorie_age(age):
    if age > 60:
        return 'sénior'
    elif age >= 18:
        return 'majeur'
    else:
        return 'mineur'

# Obtenir les informations de l'utilisateur
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))
sexe = input("Entrez votre sexe (M/F) : ")

# Vérifier si l'utilisateur est majeur ou sénior
categorie_age = determiner_categorie_age(age)

# Demander la valeur à convertir
valeur = float(input(f"Entrez la valeur à convertir (en {'' if categorie_age == 'majeur' else 'pouces ' if categorie_age == 'sénior' else 'cm '}) : "))
unite = input(f"Entrez l'unité (cm ou pouces) : ")

# Convertir la valeur
valeur_convertie = convertir_to_cm(valeur, unite)

# Afficher les résultats
if valeur_convertie is not None:
    print(f"{nom} ({categorie_age}, {sexe}) a rentré une valeur de {valeur} {'' if categorie_age == 'majeur' else 'pouces ' if categorie_age == 'sénior' else 'cm '} qui équivaut à {valeur_convertie:.2f} cm.")
else:
    print("L'unité entrée est invalide. Veuillez entrer 'cm' ou 'pouces'.")
