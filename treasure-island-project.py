print('''
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

left_or_right = input('You\'re at a crossroad, which direction you want to go? '
                      '"left" or "right"?\n').lower()

if left_or_right == "left":
    print("You are now at the coast of sea. Now choose to swim or wait.")
    swim_or_wait = input("Want to wait for a boat or swim to the Island?\n").lower()
    if swim_or_wait == "wait":
        print("You successfully crossed the sea and landed on the Island. "
              "Now choose the right door.")
        which_door = input("There are three doors, Red, Yellow, and Blue. "
                           "Which door you want to open?\n").lower()

        if which_door == "red":
            print("Burned by fire. Game Over.")
        elif which_door == "blue":
            print("Eaten by beasts. Game Over.")
        elif which_door == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fell into a hole. Game Over.")
