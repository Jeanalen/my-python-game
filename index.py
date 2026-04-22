import random 

choice_map = {
    "a": "rock",
    "b": "paper",
    "c": "scissors"
}

choices = list(choice_map.values())

def determine_winner(player_choice, computer_choice): 
    if player_choice == computer_choice: 
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"): 
        return "win"
    else:
        return "lose"

def play_game(): 
    print("Welcome to Rock, Paper, Scissors!") 
    print("Type 'quit' to exit the game.") 
    print("Choose:")
    print("A - Rock")
    print("B - Paper")
    print("C - Scissors")
    print("-" * 30)  

    # Player records
    player_wins = 0
    player_losses = 0
    player_ties = 0

    # Computer records
    computer_wins = 0
    computer_losses = 0
    computer_ties = 0

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        player_input = input("Human's choice (A/B/C): ").lower()
        
        if player_input == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if player_input not in choice_map:
            print("Invalid choice. Please enter A, B, or C.")
            continue
        
        player_choice = choice_map[player_input]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice) 

        if result == "win":
            print("You win!")
            player_wins += 1
            computer_losses += 1
        elif result == "lose":
            print("You lose!")
            player_losses += 1
            computer_wins += 1
        else:
            print("It's a tie!")
            player_ties += 1
            computer_ties += 1
        
        attempts += 1

        print(f"\nAfter {attempts} attempts:")
        print(f"Player (Human)   - Wins: {player_wins}, Losses: {player_losses}, Ties: {player_ties}")
        print(f"Computer - Wins: {computer_wins}, Losses: {computer_losses}, Ties: {computer_ties}")
        print("-" * 30)
    
    # FINAL RESULTS
    print("\nGame Over!")
    print("FINAL RECORDS:")
    print(f"Player (Human)   - Wins: {player_wins}, Losses: {player_losses}, Ties: {player_ties}")
    print(f"Computer - Wins: {computer_wins}, Losses: {computer_losses}, Ties: {computer_ties}")

    if player_wins > computer_wins:
        print("Overall Winner: HUMAN PLAYER (You)!")
    elif computer_wins > player_wins:
        print("Overall Winner: COMPUTER!")
    else:
        print("Overall Result: IT'S A TIE!")

if __name__ == "__main__": 
    play_game()
