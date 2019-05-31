import requests #importera requests

nummer = input("ange ett nummer: ") # input variabel
r = requests.get('http://77.238.56.27/examples/numinfo/?integer='+ str(nummer))# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
res = r.json #använder r.json för att få en json object, alltså en dictionarie

if res ['even']:  # om even är san
    print("talet är jämt") #print talet är jämt 
else :
    print("talet är udda")

if res ['prime']: 
    print("talet är ett primtal")
else: 
    print("talet är inte ett primtal")
print ("talet faktorer är: ")

for nummer0 in res['factors']:  
    print (nummer0)
