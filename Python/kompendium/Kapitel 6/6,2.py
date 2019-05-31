import requests #importera requests bibloteket

stadInput = input("ange en stad " + ":") #input variabel
r = requests.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + stadInput) # använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
res = r.json() #använder r.json för att få en json object, alltså en dictionarie
for data in  res ['forecasts']: # för alla objekt i res forecasts
    print ( data["date"] + "           " + data["forecast"] ) #printa datum och vädret 
    print("\n") # gör avstånd mellan varje rad 
    print (25 * "*")# printa 25 st *

#mer forklaring om for loopen finns i uppgift 4.4 
   
    
    