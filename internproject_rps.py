import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def decide_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'paper' and computer == 'rock') or \
       (user == 'scissors' and computer == 'paper'):
        return "You win!"
    return "You lose!"

def play_rock_paper_scissors():
    user_score, computer_score = 0, 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = decide_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")

        if input("Play again? (yes/no): ").strip().lower() != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_rock_paper_scissors()
