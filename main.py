from dice_game import roll_dice
from players import play_round

while True:
    print("\n--- DICE GAME SYSTEM ---")
    print("2. Multi-Player Dice Game (Select Players)")
    print("5. Dice Roller (Single Player - Streak Mode)")
    print("0. Exit")

    choice = input("\nEnter choice: ")

    if choice == '2':
        while True:
            count = input("Enter number of players: ").strip()

            if count.isdigit() and int(count) >= 1:
                count = int(count)
                break
            else:
                print("Invalid input! Enter a valid number.")

        play_round(count)

    elif choice == '5':
        roll_dice()

    elif choice == '0':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")