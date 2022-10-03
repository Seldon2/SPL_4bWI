import random

numWuerfel = 6
sumPlayer = 0
sumComp = 0
gameOver = False

while gameOver == False:
  mode = int(input("1: Spiel Starten\n2: Spiel beenden\nAuswahl: "))
  if mode == 1:
    for i in range(numWuerfel):
      player = input("Beliebige Taste drücken um zu würfeln\n")
      playerWuerfel = random.randint(1, 6)
      sumPlayer += playerWuerfel

      print(f"Sie haben {playerWuerfel} gewürfelt!")

      compWuerfel = random.randint(1, 6)
      sumComp += compWuerfel

      print(f"Der Computer hat {compWuerfel} gewürfelt!")

      print(f"Spieler Gesamtpunkte: {sumPlayer}, Computer Gesamtpunkte: {sumComp}\n")

    if sumPlayer == sumComp:
      print("Unentschieden\n")
    elif sumPlayer > sumComp:
      print("Spieler hat gewonnen\n")
    else:
      print("Computer hat gewonnen\n")

  if mode == 2:
    gameOver == True
    quit()


