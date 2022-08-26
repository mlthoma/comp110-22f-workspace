"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730578788"


word: str = str(input("Enter a 5-character word: "))
if len(word) < 5 or len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = str(input("Enter a single character: "))
if len(character) > 1 or len(character) < 1:
    print("Error: Word must contain 5 characters")
    exit()
print("Searching for " + character + " in " + word)

matching_number: int = 0

if word[0] == character:
    matching_number += 1
    print(character + " found at index 0")

if word[1] == character:
    matching_number += 1
    print(character + " found at index 1")

if word[2] == character:
    matching_number += 1
    print(character + " found at index 2")

if word[3] == character:
    matching_number += 1
    print(character + " found at index 3")

if word[4] == character:
    matching_number += 1
    print(character + " found at index 4")

if matching_number == 1:
    print(matching_number, "instance of " + character + " found in " + word)

if matching_number >= 2:
    print(matching_number, "instances of " + character + " found in " + word)

if matching_number == 0:
    print("No instances of " + character + " found in " + word)






    
    
