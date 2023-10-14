
print("bonjour; vous voulez convertir des unités de mesure")
print("tapez 1 pour convertir de pouces en cm")
print("tapez 2 pour convertir de cm en pouces")


choice = input("Votre choix (1 ou 2): ")

if choice == "1":
    
    valeur_string  = input("Donnez la valeur à convertir en pouces: ")
    valeur_convertie = round(float(valeur_string) * 2.54,2)
    
    print ("La conversion donne " + str(valeur_convertie) + " en pouces")


else:
    valeur_string2  = input("Donnez la valeur à convertir en cms: ")
    valeur_convertie2 = round(float(valeur_string2) * 0.5,2)
    
    print ("La conversion donne " + str(valeur_convertie2) + " en cms")

   