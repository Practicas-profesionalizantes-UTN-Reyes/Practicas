from bs4 import BeautifulSoup
import requests
html = "https://www.frd.utn.edu.ar/"

paginaZ= requests.get(html)

soup = BeautifulSoup(paginaZ.content,"html.parser")

links = soup.find_all('link')

for link in links:
    href = link.get("href")
    rel = link.get("rel")

    print(f"href: {href}, rel: {rel}")