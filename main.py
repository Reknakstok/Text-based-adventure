sword_taken = False
upstairs_left_or_right = ""
key_taken = False
secret_room = False

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
    print("2. Op de begane grond blijven en naar links")
    print("3. Op de begane grond blijven en naar rechts")
    print("4. Naar de kelder")
    
    choice = input("> ")
    
    while True:
        if choice == "1":
            go_upstairs()
            break
        elif choice == "2" or choice == "3":
            go_to_ground_floor()
            break
        elif choice == "4":
            go_to_basement()
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            choice = input("> ")

def go_upstairs():
    global sword_taken
    global upstairs_left_or_right
    global secret_room
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
        if choice.lower() == "rechts":
            upstairs_left_or_right = "rechter"
            break
        elif choice.lower() == "links":
            upstairs_left_or_right = "linker"
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            choice = input("> ")

    print("Op het einde van de gang kom je een deur tegen, je opent de deur en ziet een oud houten bureau.")
    print("Wil je kijken wat erop ligt? (ja/nee)")

    choice = input("> ")

    if choice.lower() == "ja":
        print("Er ligt een oude plattegrond van het kasteel. Op de plattegrond zie je dat er achteraan in de kelder een geheime ruimte zit achter een groot schilderij?!?")
        secret_room = True

    print("Waar wil je heen?")
    print("1. Naar de kelder")
    print(f"2. Naar de {upstairs_left_or_right} kant van de gang")
    print("3. Naar de begane grond")

    choice = input("> ")

    while True:
        if choice == "1":
            go_to_basement()
            break
        elif choice == "2":
            go_to_other_side()
            break
        elif choice == "3":
            go_to_ground_floor()
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")
            choice = input("> ")

def go_to_basement():
    global sword_taken
    print("Je loopt de trap naar beneden...")
    if sword_taken:
        print("Wilt u uw zwaard mee nemen? (ja/nee)")
        choice = input("> ")

        if choice.lower() == "ja":
            print("Je neemt je zwaard mee, je komt aan onderaan de trap. Je ziet een grote ruimte in de duisternis. Je loopt richting de zaal... Plots hoor je gegrom! Je ziet voor je een grote draak en hij spuwt vuur recht op je af.")
            print("Uw avontuur stopt hier want u bent veranderd in een hoopje as.")
        else:
            print("Je komt aan onderaan de trap. Je ziet een grote ruimte in de duisternis. Je loopt richting de zaal... Plots hoor je gegrom! Je ziet voor je een grote draak maar hij valt je nog niet aan.")
            print("Wat wil je doen?")
            print("1. Doorlopen")
            print("2. Uit het kasteel vluchten")

            choice = input("> ")

            while True:
                if choice == "1":
                    print("Je loopt rustig door en de draak blijft gelukkig rustig zitten.")
                    past_dragon()
                    break
                elif choice == "2":
                    print("Je rent de trap terug op en vlucht snel uit het kasteel, uw avontuur stopt hier.")
                    break
                else:
                    print("Ongeldige keuze. Probeer het opnieuw.")
                    choice = input("> ")

def go_to_ground_floor():
    global key_taken
    print("Je loopt rond door het kasteel, je ziet veel stof. Er is hier al lang niemand geweest... Je vindt een kist...")
    if not key_taken:
        print("Helaas zit er een slot op. Je loopt door maar vindt voorderest niks bijzonders.")
    else:
        print("Er zit een slot op, maar je hebt een sleutel gevonden. Wil je proberen of deze past? (ja/nee)")
        choice = input("> ")
        if choice.lower() == "ja":
            print("Je doet de sleutel in het slot. De sleutel past! Je opent de kist en je ziet er een brief in liggen. Je pakt de brief en leest hem:")
            print("LET OP IN DE KELDER VAN DIT KASTEEL ZIT EEN DRAAK. MAAR WEES NIET GESCHROKKEN, DIT IS EEN TAMME DRAAK. ALLEEN ALS JE MET WAPENS AANKOMT ZAL HIJ UW AANVALLEN UIT ZELFVERDEDIGING.")
        else:
            print("Je hebt ervoor gekozen om het niet te proberen. Je loopt door maar vindt voorderest niks bijzonders.")

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

def go_to_other_side():
    print(f"Je loopt naar de {upstairs_left_or_right} kant van de gang. De grond begint steeds harder te kraken, wil je doorlopen? (ja/nee)")

    choice = input("> ")

    if choice.lower() == "ja":
        print("Je loopt door, KRAKKKKKK!!! Je bent door de vloer gevallen... Je bent gelukkig ongedeerd. Je bent nu op de begane grond.")
        go_to_ground_floor()
    else:
        print("Waar wil je heen?")
        print("1. Naar de kelder")
        print("2. Naar de begane grond")

        choice = input("> ")

        while True:
            if choice == "1":
                go_to_basement()
                break
            elif choice == "2":
                go_to_ground_floor()
                break
            else:
                print("Ongeldige keuze. Probeer het opnieuw.")
                choice = input("> ")

def past_dragon():
    if secret_room:
        print("Je ziet het grote schilderij van de plattegrond. Je duwt hem langzaam opzij en je ziet een opening in de muur... Je gaat er doorheen en je ziet een schat liggen!!!")
        won()
    else:
        print("Je doorzoekt de hele kelder maar je vindt helemaal niks, je loopt weer naar boven...")

        print("Waar wil je heen?")
        print("1. Naar boven")
        print("2. Naar de begane grond")
        print("3. In de kelder blijven")

        choice = input("> ")
    
        while True:
            if choice == "1":
                go_upstairs()
                break
            elif choice == "2":
                go_to_ground_floor()
                break
            elif choice == "3":
                go_to_basement()
                break
            else:
                print("Ongeldige keuze. Probeer het opnieuw.")
                choice = input("> ")

def won():
    print("U heeft het spel gewonnen, gefeliciteerd!")

while True:
    start_game()

    print("\nWilt u het spel opnieuw spelen? (ja/nee)")

    choice = input("> ")

    if choice.lower() != "ja":
        print("Bedankt voor het spelen! Tot ziens!")
        break