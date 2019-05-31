#skapar listor
registrerade =["Anna", "Eva", "Erik", "Lars", "Karl"] 
avanmälningar =["Anna", "Erik", "Karl"]


for namn in avanmälningar: #för alla namn i listan avanmälningar .. namn = alla namn i listan 
    registrerade.remove(namn) # ta bort variabel namn, alltså alla namn i listan avanmälningar från registrerade listan 

#print ur registrerade
print ( registrerade )
