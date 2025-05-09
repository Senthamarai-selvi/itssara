import random

def get_user_choice():
    print("\nChoices:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Please enter a number!")

def get_ai_choice():
    return random.randint(1, 3)

def choice_to_string(choice):
    if choice == 1:
        return "Stone"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

def determine_winner(user, ai):
    if user == ai:
        return "draw"
    elif (user == 1 and ai == 3) or (user == 2 and ai == 1) or (user == 3 and ai == 2):
        return "user"
    else:
        return "ai"

def main():
    print("Welcome to Stone, Paper, Scissors Game!")

    while True:
        user_choice = get_user_choice()
        ai_choice = get_ai_choice()

        print(f"\nYou chose: {choice_to_string(user_choice)}")
        print(f"AI chose: {choice_to_string(ai_choice)}")

        winner = determine_winner(user_choice, ai_choice)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("Congratulations! You win!")
        else:
            print("AI wins! Better luck next time.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

main()
