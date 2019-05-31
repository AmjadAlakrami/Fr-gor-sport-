m = range(501) #använder funktionen range för att definera m som en lista 
a = 0 
for nummer in m :  #för nummer i m 
    if nummer % 2 != 0 : # om resten av defitionen mellan nummer o 2 inte lika med 0, alltså om nummer är udda 
        summa = summa + nummer # summa = addetionen mellan alla nummer i m och variabel a
print(summa)