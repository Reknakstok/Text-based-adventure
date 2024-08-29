def start_game():
    print("Wilt u uitleg hoe het spel werkt? (ja/nee)")

    choice = input("> ")

    if choice.lower() == "ja":
        explanation()
    
    choice = input("> ")

def explanation():
    print("Je bent de hoofdpersoon van een verhaal en JIJ moet de keuzes maken! Zometeen wordt een verhaal verteld en dan wordt er een vraag gesteld en mag jij de keuze maken. Veel succes!\n")

start_game()
