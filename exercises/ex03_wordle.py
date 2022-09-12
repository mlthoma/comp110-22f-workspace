"""Making wordle that contains the game loop."""
__author__ = "730578788"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """Determines if the single character of the second string is found anywhere in the first string."""
    assert len(letter) == 1
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1 
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Given a guess and the secret word, this function definition returns the corresponding emoji."""
    assert len(guess) == len(secret_word)
    i: int = 0
    emoji_of_guess: str = ""
    while i < len(secret_word):
        if guess[i] == secret_word[i]:
            emoji_of_guess = emoji_of_guess + GREEN_BOX
            
        elif contains_char(secret_word, guess[i]):
            emoji_of_guess = emoji_of_guess + YELLOW_BOX
            
        else:
            emoji_of_guess = emoji_of_guess + WHITE_BOX
        i += 1
    return emoji_of_guess

def input_guess(expected_length: int) -> str:
    """Given an integer of the expected length of a guess, this will prompt the user for a guess until they provide one of the expected length."""
    guess_input: str = str(input("Enter a " + str(expected_length) + " character word: "))
    while len(guess_input) != expected_length:
        guess_input = str(input("That was not " + str(expected_length) + " letters! Try again: "))
    if len(guess_input) == expected_length:
        return guess_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 0
    win: bool = False
    user_guess: str = ""
    secret: str = "codes"
    emoji_string: str = ""
    while turns <= 5 and not win:
        turns += 1
        print("=== Turn " + str(turns) + "/6 ===")
        user_guess = input_guess(len(secret))
        emoji_string = emojified(user_guess, secret)
        if user_guess == secret:
            win = True
        print(emoji_string)
    
    if win:
        print("You won in " + str(turns) + "/6 turns! ")
    else:
        print(" X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()
