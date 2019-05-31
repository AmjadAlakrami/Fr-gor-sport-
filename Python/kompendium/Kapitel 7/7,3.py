import random 

randomNummer = random.randint(0, 99) 
print ("Jag har en siffra i minnet mellan 0 och 99, Kan du gissa vilkket det är? ")

while True: 
    NummerInput = int(input("Din gissning:  "))
    if (NummerInput > randomNummer):
        print ("din gissning är för hög")
    elif (NummerInput < randomNummer):
        print ("din gissning är för låg")
    else:
        print ("Bra jobbat! din gissning är korekt")
        break
                
