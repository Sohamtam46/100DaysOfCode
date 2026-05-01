import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
site_html = response.text
soup = BeautifulSoup(site_html,"html.parser")
all_movie_titles = soup.select(selector=".article-title-description__text > h3")

title = [movie_title.getText() for movie_title in all_movie_titles]


for movie in reversed(title):
    with open("Best Movies.txt","a", encoding="utf-8") as file:
        file.write(movie + "\n")