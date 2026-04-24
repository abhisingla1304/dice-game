from dice_game import roll_dice
from players import play_round

while True:
    print("\n--- DICE GAME SYSTEM ---")
    print("2. Multi-Player Dice Game (Select Players)")
    print("5. Dice Roller (Single Player - Streak Mode)")
    print("0. Exit")

    choice = input("\nEnter choice: ")

    if choice == '2':
        try:
            count = int(input("Enter number of players: "))
            if count < 1:
                print("You need at least 1 player!")
            else:
                play_round(count)
        except ValueError:
            print("Invalid input! Please enter a number.")

    elif choice == '5':
        roll_dice()

    elif choice == '0':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")