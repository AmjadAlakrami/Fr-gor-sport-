import requests

name = input("jejejejej"   )

r = requests.get('https://opentdb.com/api.php?amount=10&difficulty='+ str(name))# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
res = r.json ()
for data in res ['results']:
    print(data["question"])