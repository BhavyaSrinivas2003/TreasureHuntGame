#Function to ask play again or not
def lets_play_again():
    print("Do you want to play again? (y or n)")
    # convert the players input to lower_case
    answer=input("Enter ur choice ").lower()
    if answer =="y":
        print("Game is restarting")
        start()
    else:
        print("Game is quitting")
        game_over("reason")
        exit()
    
#game_over function accepts an argument called "reason"
def game_over(reason):
    print("Not in a mood of playing, hence quitting")




# Treasure room
def treasure_room():
    print("You are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take some diamonds and go through the door .")
    print("2). Just go through the door .")
    answer=input("Enter ur choice ")
    if answer=="1":
        print("You cannot open the door, as your hands are filled with diamonds")
        print("Game Over!")
        lets_play_again()
    elif answer=="2":
        print("Hurray! Now the treasure box is yours")
        print("YAY!!!WIN")
        lets_play_again()


# monster room
def monster_room():
    print("Now you entered the room of a monster!")
    print("The monster is sleeping.")
    print("Behind the monster,there is another door.What would you do? (1 or 2)")
    print("1). Go thriugh the door silently")
    print("2). Kill the monster and show your courage!")
    answer=input("Enter ur choice ")
    if answer=="1":
        print("You entered into treasure room")
        treasure_room()
    elif answer=="2":
        print("The monster was hungry, he/it ate you")
        print("Game Over!")
        lets_play_again()

# Snake room
def snake_room():
    print("There is a snake here .")
    print("Behind the Snake is another door .")
    print("The snake is having eggs!")
    print("What would you do? (1 or 2)")
    print("1). Take the eggs.")
    print("2). Taunt the snake.")
    answer=input("Enter ur choice ")
    if (answer=="1"):
        print("You want eggs not the treasure !! Thats why the snake killed you.")
        print("Game Over!")
        lets_play_again()
    elif (answer=="2"):
        print("You entered into treasure room")
        treasure_room()
    

# start the game
def start():
    print("You are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    # convert the players input to lower_case
    answer=input("Enter ur choice ").lower()
    if answer =="l":
        print("You have entered into snake room")
        snake_room()
    elif answer =="r":
        print("You have entered into monster room")
        monster_room()
start()
