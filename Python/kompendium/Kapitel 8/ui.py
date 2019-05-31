def line(dots=False):
    if dots == True: 
        print (25 * "*" )
    else :
     print(25 * "-")

def header(text): 
    Centerd_text = text.center(23)
    print("| ", Centerd_text," |")

def echo(text1="", text2=""): 
    if text2=="":
        print("| "+ text1) 
    else: 
        print("| "+ text1 + " | "+ text2) 


def prompt(text): 
    a=input("| "+text+ " > ")  
    return(a)
    




