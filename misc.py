import json
import requests

###########################################################################
aaa = json.loads(requests.get("https://api.thecatapi.com/v1/images/search").text)
img = requests.get(aaa[0]["url"])
with open("mew.jpg", "wb") as handler:
    handler.write(img.content)

def new_cat():
    aaa = json.loads(requests.get("https://api.thecatapi.com/v1/images/search").text)
    img = requests.get(aaa[0]["url"])
    with open("mew.jpg", "wb") as handler:
        handler.write(img.content)
############################################################################

