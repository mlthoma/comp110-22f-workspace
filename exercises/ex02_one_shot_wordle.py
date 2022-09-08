"""EX02 - One Shot Wordle - Another step toward Wordle."""
__author__ = "730578788"

secret_word: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
secret_length: int = len(secret_word)
i: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

emoji_of_guess: str = ""

while len(guess) != secret_length:
    guess = str(input("That was not " + str(secret_length) + " letters! Try again: "))
# This loop detects if someone didn't guess a word with the same number of letters as the secret word.
# This loop prevents people from moving on with the game until they enter a word that has the same length as the secret.
while i < secret_length:
    if guess[i] == secret_word[i]:
        emoji_of_guess = emoji_of_guess + GREEN_BOX
# This loop checks to see if a letter in the person's guess is correct and located in the correct location
# If so, then a green box is added to the emoji_of_guess string.
    else:
        character_in_word: bool = False
        alternate_indices: int = 0
        while character_in_word == False and alternate_indices < secret_length:
            if guess[i] == secret_word[alternate_indices]:
                character_in_word = True
    
            else:
                alternate_indices += 1
            
        if character_in_word:
            emoji_of_guess = emoji_of_guess + YELLOW_BOX
        else:
            emoji_of_guess = emoji_of_guess + WHITE_BOX
        # When the letter in the guess doesn't qualify for a green box, this loop checks to see if the letter is located in the word at all
        # If the letter is in the word, a yellow box is printed in the string. If the letter is not in the word, a white box is printed in the string.
    i += 1

# This part below prints out the final results.    
print(emoji_of_guess)
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
