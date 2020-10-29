import time

sleep = 'time.sleep(1)'

def choices():
    sleep
    print("hallo kom je bed uit je moet naar school! kom je nog? Antwoord: Ja/Nee")
    choice = input().lower()
    if choice == "ja":
        print("Top kan je nog optijd komen!.")
    elif choice == "nee":
        print("ah oke maar pas wel op dat je niet telaat komt.")
    else:
        print(choice, "is geen geldig antwoord sorry.")
        return choice
        

def choices2():
    sleep
    print("wat eten we vanavond? Antwoord: brood/pizza")
    choice2 = input().lower()
    if choice2 == "brood":
        print("ah lekker een broodje met jam hoop ik:)")
    elif choice2 == "pizza":
        print("hmm mijn favoriete eten lekker hoor!")
    else:
        print(choice2, "is geen geldig antwoord sorry.")
        return choice2

def choices3():
    sleep
    print("We moeten naar school toe en je bent bijna te laat gaan we met de fiets of de auto? Antwoord: auto/fiets")
    choice3 = input().lower()
    if choice3 == "auto":
        print("lekker lui met de auto man...")
    elif choice3 == "fiets":
        print("We gaan lekker fietsen!")
    else:
        print(choice3, "is geen geldig antwoord sorry.")
        return choice3

def choices4():
    sleep
    print("je komt thuis na een lange dag van school en je ma is boos wat doe je. Antwoord: een discussie aangaan / het laten gaan")
    choice4 = input().lower()
    if choice4 == "een discussie aangaan":
        print("je krijgt veel gezeik maar je komt er gelukkig goed vanaf maar je dag is wel verpest")
    elif choice4 == "het laten gaan":
        print("je negeert je ma en gaat lekker muziek luisteren")
    else:
        print(choice4, "is geen geldig antwoord sorry.")
        return choice4

def dailychoices5():
    sleep
    print("wat gaan we doen na dat gezeik met je ma huiswerk of gamen of misschien het nieuwe nummer van sefa luisteren? Antwoord: huiswerk / gamen / muziek")
    choices5 = input().lower()
    if choice5 == "huiswerk":
        print("lekker bezig man je gaat voor die voldoendes en miss is je ma dan ook blij")
    elif choice5 == "gamen":
        print("niet zo slim maar sure ga je gang")
    elif choice5 == "muziek":
        print("goeie keuze, luister naar het nieuwe nummer van sefa! going under")
    else:
        print(choice5, "is geen geldig antwoord sorry.")
        return choice5


choices()
choices2()
choices3()
choices4()
choices5()

sleep
print("nice je bent door de vragen heen! vier dat maar jij geluksvogel ;)")