#skapar listor 
norden = ["Danmark", "Finland", "Island", "Norge", "Sverige"]
storbritanien = ["England", "Norderland", "Skottland", "Wals"]

#skapar en input variabel Vilketland
Vilketland = input("vilket land kommer du ifrån?")

if Vilketland.title() in norden: # om inmatningen i a finns i norden lista ... vi använder inbygda funktionen title för att oavsett hur användaren skriver i input (stor/små bokstäver) 
                        # så kommer programmet att ändra det till en tittel, då matchar det sätt vi skrev i listan
     print ("landet är en del av norden") # printa ut .. 
elif Vilketland.title()in storbritanien : # annars om .. 
    print ("landet är en del av storbritanien ")

# om inget av det ovan gäller 
else :
    print("landet tillhör inte storbritanien eller norden")