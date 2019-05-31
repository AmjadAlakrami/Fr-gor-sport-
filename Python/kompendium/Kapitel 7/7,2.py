MultiplikInput = int(input("välj en  multiplikationstabell:   ")) # anger multiplikationstabell
upprepning = 0

while True: # sätter while loopen på 
    upprepning =  upprepning + 1 # lägger 1 på upprepning variabel 
    print(upprepning, "*" , MultiplikInput, "=", upprepning * MultiplikInput)
    if (upprepning % 3 == 0): # om man delar upprepning med 3 och får rest 0 
        fortsättinput = input("vill du fortsätta? ") 
        if (fortsättinput  == "ja"):
            continue # ett nyckerl ord som tvinger while loopen att fortsätta 
        else:
            break # ett nyckerl ord som tvinger while loopen att sluta 

#det som kommer att hända i while loopen är att först lägger den till 1 på variabel upprepning, sedan multiplicera det med inmatningen,
# sedan kollar om upprepning variabel är delbar med tre så betyder det att den har multiplicerat tre siffror och då kommer den att ställa frågas osv 