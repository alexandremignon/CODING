import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier Excel
df = pd.read_excel('/Users/alexandremignon/Desktop/DAR BICHAT/SFAR 2023/BASE FUSIONNEE CDT 4 MAI.xlsx')

# Afficher les premières lignes du DataFrame pour vérifier l'importation
print(df.head())

# Statistiques descriptives pour les données numériques
print(df.describe())


