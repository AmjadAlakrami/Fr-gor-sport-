import requests
AntalFr = input("Välj antal frågor: ")
Defic = input ("Välj svårighetsgraden: ")
Catig = input ("Välj Katigorien: ")

if Defic.title() = 

r = requests.get('https://opentdb.com/api.php?amount='+ str(AntalFr))# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
res = r.json ()
for data in res ['results']:
    print(data["question"])