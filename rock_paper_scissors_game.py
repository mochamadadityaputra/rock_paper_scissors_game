import random
import emoji

# Define emojis for each choice
rock = emoji.emojize(":rock:")
paper = emoji.emojize(":page_with_curl:")
scissors = emoji.emojize(":scissors:")

# Map choices to emojis
emojizes = {"r": rock, "p": paper, "s": scissors}
choices = ("r", "p", "s")


def get_computer_choice():
    """Randomly select the computer's choice."""
    return random.choice(choices)


def get_winner(user, computer):
    """Determine the winner based on user and computer choices."""
    if user == computer:
        return "Tie"
    elif (
            (user == "r" and computer == "s") or
            (user == "p" and computer == "r") or
            (user == "s" and computer == "p")
    ):
        return "User wins"
    else:
        return "Computer wins"


def play_game():
    """Main function to play the game."""
    while True:
        user_choice = input("Choose rock, paper, or scissors (r/p/s): ").lower()
        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"You chose {emojizes[user_choice]}")
        print(f"Computer chose {emojizes[computer_choice]}")

        result = get_winner(user_choice, computer_choice)
        print(result)

        should_continue = input("Continue the game (y/n)? ").lower()
        if should_continue == "n":
            print("Thanks for playing!")
            break


# Start the game
play_game()
