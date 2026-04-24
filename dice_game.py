import random
import time

def roll_dice():
    print("\n🎲 --- WELCOME TO THE DICE ROLLER --- 🎲")
    
    while True:
        user_input = input("\nPress 'Enter' to roll (or type 'exit'): ").strip().lower() #output will remove extra space and convert to uppercase letter.
        
        if user_input == 'exit':  # code exit ho jayega if entered exit
            break

        print("Rolling...")
        time.sleep(0.5)
        result = random.randint(1, 6)
        print("You rolled:", result)

        if result == 6:
            print("🔥 LUCKY SIX! Roll again!")
        else:
            print("Game Over!")
            break