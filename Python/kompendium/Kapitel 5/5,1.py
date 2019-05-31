#skapar listor 
Kim_kardishian = ["svart", "kvinna", "grön"] 
Hillary_Clinton = ["blond", "kvinna", "blå"]
Zayn_Malik = ["svart", "man", "brun"]
Trump = ["röd", "man", "blå"]

#skapar input variablar 
Kön = input("Ange ditt kön" +  "(man/kvinna)")
Hårfärg = input("Vad har du för hår färg?")
Ögonfärg = input("Vad har du för färg på dina ögon?")


if Kön in Zayn_Malik: # om kön finns i zayn malik listan 
    if Hårfärg in Zayn_Malik:  # om hårfärg finns i zayn malik listan  
        if Ögonfärg in Zayn_Malik: # om Ögonfärg finns i zayn malik listan 
            print("Du liknar Zayn Malik")  # printa ut du liknar zayn malik 
elif Kön in Trump: # annars om .. 
    if Hårfärg in Trump:  
        if Ögonfärg in Trump:
            print("Du liknar Trump")

elif Kön in Kim_kardishian:
    if Hårfärg in Kim_kardishian:  
        if Ögonfärg in Kim_kardishian:
            print("Du liknar Kim Kardishian")
elif Kön in Hillary_Clinton:
    if Hårfärg in Hillary_Clinton:  
        if Ögonfärg in Hillary_Clinton:
            print("Du liknar Hillary Clinton")

 # om inget av det som som står ovan gäller, prina ut du är unik 
else : 
    print("Du är unik")
   
