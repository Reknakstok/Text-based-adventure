def start_game():
    print("Wilt u uitleg hoe het spel werkt? (ja/nee)")

    choice = input("> ")

    if choice.lower() == "ja":
        explanation()

    print("Gegroet, avonturier! Je staat voor de poort van een gigantisch mysterieus kasteel.")
    print("Wil je de poort openen en het kasteel betreden? (ja/nee)")

    choice = input("> ")

    if choice.lower() == "ja":
        enter_castle()
    else:
        print("Je hebt ervoor gekozen om weg te lopen. Het avontuur eindigt. Misschien een andere keer!")

def explanation():
    print("\nJe bent de hoofdpersoon van een verhaal en JIJ moet de keuzes maken! Zometeen wordt een verhaal verteld en dan wordt er een vraag gesteld en mag jij de keuze maken. Veel succes!\n")

def enter_castle():
    print("Je duwt de zware poort open en stapt het kasteel binnen.")
    print("Het is donker en stil. Je ziet een trap naar boven en een gang die naar de kelder leidt.")
    print("Waar wil je heen?")
    print("1. Naar boven")
    print("2. Naar de kelder")
    
    choice = input("> ")
    
    if choice == "1":
        go_upstairs()
    elif choice == "2":
        go_to_basement()
    else:
        print("Ongeldige keuze. Probeer het opnieuw.")
        enter_castle()

def go_upstairs():
    print("a")

def go_to_basement():
    print("b")

while True:
    start_game()

    print("\nWilt u het spel opnieuw spelen? (ja/nee)")

    choice = input("> ")

    if choice.lower() != "ja":
        print("Bedankt voor het spelen! Tot ziens!")
        break