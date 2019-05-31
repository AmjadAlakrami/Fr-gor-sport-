#skapar listor
male = [
"Erik",
"Lars",
"Karl",
"Anders",
"Johan"
]
female = [
"Maria",
"Anna",
"Margareta",
"Elisabeth",
"Eva"
]

# input variablar
tabortman= input("vilket namn vill du ta bort från listan "+ str(male)) 
tabortkvinna = input("vilket namn vill du ta bort från listan"+ str(female))

male.remove (tabortman) # ta bort den användaren matade in i input a från male listaan 
female.remove(tabortkvinna)

# printa ut 
print(male)
print(female)


