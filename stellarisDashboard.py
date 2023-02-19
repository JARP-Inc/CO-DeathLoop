#https://galactos-production.up.railway.app/
import requests

def stellarisDashboard():

    response = requests.get("https://galactos-production.up.railway.app/articles?page=0")
    #print(response.json())

    if str(response.json()[0]["date"]).split(".")[1] > str(response.json()[1]["date"]).split(".")[1]:
        return True
    return False

