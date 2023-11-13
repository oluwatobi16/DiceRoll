import random

def roll_dice():
    return random.randint(1, 6)

def get_user_guess():
    try:
        guess = int(input("Guess the number (1-6): "))
        if 1 <= guess <= 6:
            return guess
        else:
            print("Please enter a number between 1 and 6.")
            return get_user_guess()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_guess()

def play_game():
    print("Welcome to the Dice Roll Game!")
    
    while True:
        user_guess = get_user_guess()
        dice_result = roll_dice()
        
        print(f"You guessed: {user_guess}")
        print(f"The dice rolled: {dice_result}")
        
        if user_guess == dice_result:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you guessed wrong. Try again.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
