import ui 
import web 

ui.line()
ui.header("ARTIST DATABASE")
ui.line()
ui.echo("Welcome to a world of")
ui.echo("Music!")
ui.line()
ui.echo("L", "List artists")
ui.echo("V", "View artist profile")
ui.echo("E", "Exit application")
a=ui.prompt("Selection")
#det vi gör i från rad 5 till 14 är att vi kör funktionerna som finns i ui filenn genom att skriva filens namn (ui) . funktionens namn 

run="KÖR" #en variabel för att kunna loopa 

while run=="KÖR":
    res = web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/") #skickar en get request till url:en
    if a.title()=="L": #om input är l 
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        for artister in res["artists"]: 
            ui.echo(artister["name"]) 
        ui.line(True) #sätter boolen argumentet till true, då skriver den ut *
        ui.echo("L", "List artists")
        ui.echo("V", "View artist profile")
        ui.echo("E", "Exit application")
        a=ui.prompt("Selection") #input
    elif a.title()=="V": #annars om input är V
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        artist=ui.prompt("Artist name") #input
        ui.line(True)
        q=False #skapar en boolen variabel 
        for artister in res["artists"]:
            if artist.title() in artister["name"]: #om artis input finns i json objektet
                ui.header(artist.title())
                ui.line(True)
                check=True #sätt q till true 
        if check==True: # om q är true 
            for z in res["artists"]:
                if z["name"]==artist.title():
                    id=z["id"] #hämtas id 
            res2=web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+id) #skickar get request till url:en med ide
            genres=res2["artist"]["genres"] #hämtar värdena från json objektet
            years=res2["artist"]["years_active"]
            members=res2["artist"]["members"] 
            tomt=""
            for gen in genres:
                tomt+=gen + ", "
            tomt2="" 
            for år in years:
                tomt2+=år + ", "
            tomt3=""
            for medlemer in members:
                tomt3+=medlemer + " "  
            ui.echo("Genres: "+ tomt )  #använder echo funktionen för att printa det bi hämtade 
            ui.echo("Years active: "+ tomt2)
            ui.echo("Members: "+ tomt3 ) 
            ui.line()
            ui.echo("L", "List artists")
            ui.echo("V", "View artist profile")
            ui.echo("E", "Exit application")
            a=ui.prompt("Selection")
        else: #annars om artisten inte finns 
            ui.echo("That artist does not exist") 
            ui.line(True) 
    elif a.title()=="E": #om inputet är e 
        ui.echo("Exiting")
        run="stopp" # sätter run till stopp, då är den inte kör längre vilket betyder att while lopen slutar funka och då avslutas allt 
    else: 
        a=""
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        ui.echo("Invalid choice")
        ui.line()
        ui.echo("L", "List artists")
        ui.echo("V", "View artist profile")
        ui.echo("E", "Exit application")
        a=ui.prompt("Selection") 