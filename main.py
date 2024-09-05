sword_taken = False
upstairs_left_or_right = ""

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
    
    while True:
        if choice == "1":
            go_upstairs()
            break
        elif choice == "2":
            go_to_basement()
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            choice = input("> ")

def go_upstairs():
    global sword_taken
    global upstairs_left_or_right
    print("Je neemt de trap naar boven, terwijl je de krakende trap op loopt zie je aan de muur een zwaard hangen.")
    print("Wil je hem mee nemen? (ja/nee)")
    
    choice = input("> ")

    if choice.lower() == "ja":
        sword_taken = True
        print("Je pakt het zwaard en loopt de krakende trap verder op...")
    else:
        print("Je loopt zonder het zwaard de krakende trap verder op...")

    print("Je komt bovenaan de trap en ziet een lange gang, wil je links of rechts?")

    choice = input("> ")

    while True:
        if choice.lower == "rechts":
            upstairs_left_or_right = "linker"
            break
        elif choice.lower == "links":
            upstairs_left_or_right = "rechter"
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            choice = input("> ")

    print("Op het einde van de gang kom je een deur tegen, je opent de deur en ziet een oud houten bureau.")
    print("Wil je kijken wat erop ligt? (ja/nee)")

    choice = input("> ")

    if choice.lower() == "ja":
        print("Er ligt een oude plattegrond van het kasteel. Op de plattegrond zie je dat er achteraan in de kelder een geheime ruimte zit achter een groot schilderij?!?")
        print("Waar wil je heen?")
        print("1. Naar de kelder")
        print(f"2. Naar de {upstairs_left_or_right} van de gang")
        print("3. Naar de begaande grond")

    while True:
        if choice == "1":
            go_to_basement()
            break
        elif choice == "2":
            go_to_other_side()
            break
        elif choice == "3":
            print(go_to_ground_flour)
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            choice = input("> ")

def go_to_basement():
    print("b")

def go_to_ground_flour():
    print("b")

def go_to_other_side():
    print("b")

while True:
    start_game()

    print("\nWilt u het spel opnieuw spelen? (ja/nee)")

    choice = input("> ")

    if choice.lower() != "ja":
        print("Bedankt voor het spelen! Tot ziens!")
        break