import random
import time

mensen = ["Johan", "Hannes", "Dirk", "Tom", "Pieter", "Rik", "Damian", "Guido", "Joost", "Aki", "Sem", "Amber", "Waldo", "Raphael"]
random.shuffle(mensen)

for Menneke in mensen:
    print(Menneke)
    if Menneke == "Waldo":
        print(Menneke + " is gevonden! heck ye")
        break

stoel = mensen.index(Menneke)
time.sleep(1.5)
print("Waldo zit op stoel nummer: " + str(stoel))
