
import random

opties = ["steen" , "papier" , "schaar"]
speler_score = 0
computer_score = 0
while True:
computer_keuze = random.choice(opties)
speler_keuze = input("Kies steen, papier of schaar:  ").lower()

print (f"De computer heeft gekozen: {computer_keuze}")
if speler_keuze not in opties:
    print("Ongeldige keuze! Kies steen, papier of schaar.")
    else:
        print(f"Je hebt gekozen: {speler_keuze}")
        continue
    
    print(f"De computer koos: {computer_keuze}")
    print(f"Jij koos: {speler_keuze}")

if speler_keuze == computer_keuze:
    print("Gelijkspel")
elif (speler_keuze == "steen" and computer_keuze == "schaar") or \
     (speler_keuze == "papier" and computer_keuze == "steen") or \
     (speler_keuze == "schaar" and computer_keuze == "papier"):
    print("Je wint!")
    speler_score += 1
else:
    print("Je verliest!")
    computer_score += 1

print(f"Scores: Jij - {speler_score}, Computer - {computer_score}")

opnieuw = input ("Wil je opnieuw spelen? (ja/nee:) ").lower()
if opnieuw != "ja":
    print("Bedankt voor het spelen!")
    break

    pass