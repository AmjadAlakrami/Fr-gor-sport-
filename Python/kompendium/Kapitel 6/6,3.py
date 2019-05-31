import requests


r = requests.get('https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/') # använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
res = r.json() #använder r.json för att få en json object, alltså en dictionarie

print (25* "-")
for namn in res ['artists']: # för alla objekt i res artists
    print (namn['name']) 
print (25* "-") 

artistInput = str(input("välj en artist: "))
for artistinfo in res['artists']: 
    if (artistInput.title()  == artistinfo['name']): #om inmatningen är det smamma som artistens namn
        r = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artistinfo["id"]) #skivka enm get request för den urlen 
        res = r.json() 
        print (50* "-") 
        print ("Namn        :  " + artistInput.title() )
        print (50* "-") 
        print("Genres      :  " + str(res["artist"]["genres"]))
        print (50* "-") 
        print("Years active:  " + str(res["artist"]["years_active"]))
        print (50* "-") 
        print("Members     :  " + str(res["artist"]["members"]))
        print (50* "-") 
#printa ut



    




