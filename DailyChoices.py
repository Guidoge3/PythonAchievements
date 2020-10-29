import time

def dailychoices():
    print("Hey hoi hallo goeie morgen! Ga je nu je bed uit of niet en blijf je nog 10 minuten liggen? Antwoord met: Ja/Nee")
    choice = input()
    if choice.lower() == "ja":
        print("Top kan je nog optijd komen!.")
    elif choice.lower() == "nee":
        print("ah oke maar pas wel op dat je niet telaat komt.")
    else:
        print(choice, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices2():
    print("wat eten we vandaag? Antwoord met: brood/pizza")
    choice2 = input().lower()
    if choice2 == "brood":
        print("ah lekker een broodje")
    elif choice2 == "pizza":
        print("hmm mijn favoriete lekker hoor!")
    else:
        print(choice2, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices3():
    print("We moeten naar school toe wat ben je van plan om te doen? Met de trein of fietsen? Antwoord met: Trein / Fietsen")
    choice3 = input()
    if choice3.lower() == "trein":
        print("lekker lui met de trein.")
    elif choice3.lower() == "fietsen":
        print("We gaan lekker fietsen!")
    else:
        print(choice3, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices4():
    print("Je komt op school aan en je docent wordt boos omdat je iets niet hebt afgemaakt. Antwoord met: een discussie aangaan / het laten gaan")
    choice4 = input()
    if choice4.lower() == "een discussie aangaan":
        print("je geeft tegenargumenten waarom je iets niet hebt gedaan en komt er gelukkig vanaf.")
    elif choice4.lower() == "het laten gaan":
        print("de docent blijft zeuren maar je luisterd er maar niet naar.")
    else:
        print(choice4, "is niet een geldig antwoord.")

time.sleep(1)
def dailychoices5():
    print("wat gaan we doen huiswerk of gamen? Antwoord met: huiswerk / gamen")
    choice5 = input()
    if choice5.lower() == "huiswerk":
        print("Lekker bezig maat! Je bent leer gierig.")
    elif choice5.lower() == "gamen":
        print("Is niet de slimste keuze maar gamen is altijd leuk!")
    else:
        print(choice5, "is niet een geldig antwoord.")

dailychoices()
dailychoices2()
dailychoices3()
dailychoices4()
dailychoices5()
	