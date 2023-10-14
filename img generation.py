import requests

# Remplacez 'VOTRE_API_KEY' par votre propre clé API
API_KEY = 'qD1bnTa6xvXkJJ1zs1OjVt002Py1'

# URL de l'API de Clindrop pour générer des images
URL_API = 'https://api.clindrop.com/generate'

# Paramètres pour générer l'image
params = {
    'template': 'Doctor',  # Remplacez 'template_name' par le nom du modèle que vous souhaitez utiliser
    'text': 'playing chess',     # Remplacez par le texte que vous souhaitez afficher sur l'image
    'apiKey': API_KEY
}

# Effectuer la requête à l'API
response = requests.get(URL_API, params=params)

# Vérifier si la requête a réussi (code de statut HTTP 200)
if response.status_code == 200:
    # Enregistrer l'image
    with open('generated_image.png', 'wb') as f:
        f.write(response.content)
    print('Image générée avec succès !')
else:
    print(f'Erreur lors de la requête à l\'API. Code de statut : {response.status_code}')
