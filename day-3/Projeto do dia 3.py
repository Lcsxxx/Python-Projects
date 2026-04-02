print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

optn1= input("Do you wish to walk left or right type in \n").lower()

if optn1 == "left":
    print("You found an abandoned Castle")
    optn2 = input("Do you wish to get in or walk off? type in\n").lower()

    if optn2 == "get in":
         print("You just found three doors a Blue, Yellow and Red one")
         optn3 = input("Which one do you get in? type in\n").lower()

         if optn3 == "blue":
             print("That room  had a giant Gorilla that beat you up Game over.")

         elif optn3 == "yellow":
             print("Congratulations you Found the lost treasure!")

         else:
             print("That room was at fire you got burned to death Game over.")

    else:
         print("A Knight fell from the Castle and killed you Game over.")

else:
    print("A Giant Fireball hit you Game over.")
    