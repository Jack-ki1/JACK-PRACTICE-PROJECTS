import requests
from bs4 import BeautifulSoup as bs
github_profile = "http: //github.com/haralGADygyl"
requests = requests.get(github_profile)

scraper = bs4(request.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avator"})["src"]
print(profile_picture)