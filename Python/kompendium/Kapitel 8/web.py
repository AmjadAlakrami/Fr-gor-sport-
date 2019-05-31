import requests

def get(url):
    r = requests.get(url) # hämtar datan från den angivna urlen
    res_Dic = r.json() # returnerar som en json objekt
    return (res_Dic)