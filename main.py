import requests

name = "znr"
number = "232"
language = "en"
ID = "https://api.scryfall.com/cards/"+name+"/"+number+"/"+language

response = requests.get(ID)
print(response.json())


