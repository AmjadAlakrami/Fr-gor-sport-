#skapar listor
förnamn =["Maria", "Erik", "Karl"] 
efternamn =["Svensson", "Karlsson", "Andersson"]


for namn in förnamn:# for namn i listan förnamn .. namn = alla namn i listan förnamn
    for efterN in efternamn: # for efter i listan efter namn .. efterN = alla namn i listan efternamn
        print(namn, efterN) # printa ut namn och efterN

# alltså första for loop kommer gå igenom förnamn listan, tar första variabel, sedan går andrar for loopen i efternamn listan 
# tar första variabelen i listan, sedan printas ut variabel namn och efter .. sedan körs den andra for loopen igen och tar den andra variabeln 
# printar ut den gammla namn med den nya efter osv tills den har gått igenom hela efternamn listan, sedan startas första for loopen igen, och  samma sak händer igen 