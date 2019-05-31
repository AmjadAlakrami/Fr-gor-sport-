import math # importerar math bibloteket


vanligaKorv2 = input("Hur många elever vill ha 2 Vanilga korvar ?") # input variabel 
vanligaKorv3 = input("Hur många elver vill ha 3 Vanliga korvar ? ")
veganskaKorv2= input("Hur många elever vill ha 2 Veganska korvar ?")
veganskaKorv3 = input("Hur många elever vill ha 3 veganska korvar ?")
drycka = input ("Hur många elever vill ha en dryck? ")

totvanlig = (2 * int(vanligaKorv2)) + (3 * int(vanligaKorv3)) #multiplikation för att räkna totala antalet vanliga korv
totvegansk = (2 * int(veganskaKorv2)) + (3 * int(veganskaKorv3))
print (25 * "*")
print ("Vanlig Korv:" + " " + str(math.ceil((int(totvanlig)/8) )) + " " + "Förpackningar" )  # printar ut vanliga korv + variabel e/8 .. vi använder math.ceil funktionen från math biblotek för att avrunda uppåt 
print (25 * "*")
print ("Veganska Korv:" + " " + str(math.ceil((int(totvegansk)/4) ))+ " " + "Förpackningar")
print (25 * "*")
print ("Dryckor:" + " " + str(drycka))
print (25 * "*")
prisvanlig= int(str(math.ceil((int(totvanlig)/8) ))) * float (20.95)
prisveganska = int(str(math.ceil((int(totvegansk)/4) )))* float (34.95)
prisdrycka = int(drycka) * float(13.95)
totlapriset= int(prisvanlig) + int(prisveganska) + int(prisdrycka)
print ("Det kostar totalt:" + " " + str(totlapriset) + " " + "SEK")
print (25 * "-")

