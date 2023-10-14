import requests
from bs4 import BeautifulSoup

# Define the URL of the IMDb Top 250 page
url = "https://toitoimontoit.fr/9-meilleurs-rooftops-paris/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the list of movies (each movie is in a 'tr' tag)
    movie_list = soup.find("tbody", {"class": "lister-list"})

    # Iterate through each movie in the list
    for movie in movie_list.find_all("tr"):
        # Find the movie title and year (inside 'a' and 'span' tags)
        title = movie.find("td", {"class": "titleColumn"}).find("a").text
        year = movie.find("span", {"class": "secondaryInfo"}).text

        # Find the IMDb rating (inside 'strong' tag)
        rating = movie.find("td", {"class": "ratingColumn"}).find("strong").text

        # Print the movie details
        print(f"Title: {title}")
        print(f"Year: {year}")
        print(f"IMDb Rating: {rating}")
        print("\n")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
