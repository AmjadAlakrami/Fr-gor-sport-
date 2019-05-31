#input variabel .. input sätts till en int 
ålder = int(input("Vänligen ange din ålder:" + " "))

#skapar en lista 
timmar = ["14", "13", "12", "11,5", "11", "11", "10.5", "10", "10", "10", "9.5", "9", "9", "9", "9", "8.5", "8"]


if ålder > 16 : # om inmatningen i ålder är större än 16 

    print (timmar[16]) # printa ut variabel som har plast nummer 16 i listan timmar 

else : #annars 
    print(timmar[ålder -1] ) # printa ut variabel som har plast nummer ålder - 1, alltså om ålder = 15 så kommer variabel som har plast nummer 14 printas ut 
