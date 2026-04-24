import random

def play_round(num_players):
    print(f"\n🎲 --- {num_players} PLAYER DICE GAME --- 🎲")

    while True:
        results = {}
        
        # Player Rolling number(means yaha hum range mein numebr of player choose kar sakte hai and then code uske hisaab se chalega)
        for i in range(1, num_players + 1):
            roll = random.randint(1, 6)
            results[f"Player {i}"] = roll
            print(f"Player {i} rolled: {roll}")

        # Determine the maximum value(matlab jiska number bada hoga woh yaha check hoga)
        max_roll = max(results.values())
        winners = [player for player, score in results.items() if score == max_roll]

        # Result
        if len(winners) == 1:
            print(f"🏆 {winners[0]} wins with a {max_roll}!")
        else:
            print(f"🤝 It's a tie between: {', '.join(winners)} (Rolled {max_roll})")

    # agar game dobara khelni hai toh uske liye this is the line
        again = input("\nPlay Again? (y/n): ").lower()
        if again != 'y':
            print("Returning, Now you can play again...")
            break