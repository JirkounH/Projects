import random

def print_welcome():
    """Prints the welcome message and instructions for the game."""
    print("Hi there!")
    print("-" * 55)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 55)
    print("Enter a number (or type 'hint' for a clue):")
    print("-" * 55)

def generate_secret_number():
    """Generates a random 4-digit number with unique digits that does not start with 0."""
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]  # Ensure first digit is not 0
    return ''.join(map(str, digits[:4]))

def validate_input(user_input):
    """Validates the user's input, ensuring it is a 4-digit number with unique digits and no leading zero."""
    if user_input.lower() == "hint":
        return None  # Allow hint input
    if not user_input.isdigit():
        return "Input must contain only digits or 'hint'."
    if len(user_input) != 4:
        return "Input must be exactly 4 digits long."
    if len(set(user_input)) != 4:
        return "Input must not contain duplicate digits."
    if user_input[0] == '0':
        return "Input must not start with 0."
    return None

def calculate_bulls_and_cows(secret, guess):
    """Calculates the number of bulls (correct digit and position) and cows (correct digit but wrong position)."""
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def play_game():
    """Handles the game flow, prompting the user and processing guesses."""
    secret_number = generate_secret_number()
    attempts = 0
    
    while True:
        user_input = input(">>> ").strip()
        
        if user_input.lower() == "hint":
            print(f"Hint: The secret number is {secret_number}")
            continue
        
        attempts += 1
        
        validation_error = validate_input(user_input)
        if validation_error:
            print(validation_error)
            continue
        
        bulls, cows = calculate_bulls_and_cows(secret_number, user_input)
        
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print("-" * 55)
            print("That's amazing!")
            break
        
        bulls_text = "bull" if bulls == 1 else "bulls"
        cows_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_text}, {cows} {cows_text}")

def main():
    """Main function to start the game."""
    print_welcome()
    play_game()

if __name__ == "__main__":
    main()
