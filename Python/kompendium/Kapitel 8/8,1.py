#input variablar 
enhet = input("ange enheten du vill omvandla till:  ")
enhet2 = input("ange enheten du vill omvandla från:  ")
sträckan = int(input("ange strcäkan :   "))

# skapa en funktion
def km_till_miles (dist):
    print (25 * "*")
    print (sträckan, enhet2, " = ", dist * 1.609344, enhet)
    print (25 * "*")
def miles_till_km (dist):
    print (25 * "*")
    print (sträckan, enhet2, " = " , dist / 1.609344, enhet)
    print (25 * "*")

if enhet.title() == ("Km"): #om input enhet är km 
    miles_till_km (sträckan) #kör  miles_till_km, och använd sträckan som en argument 

elif enhet.title() == ("Miles"):
    km_till_miles (sträckan)
