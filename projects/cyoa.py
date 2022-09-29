"""Choose your own adventure program."""
__author__ = "730578788"

from random import randint

player: str = ""
points: int = 0
GRIN_EMOJI: str = "\U0001f600"


def main() -> None:
    """Entry point of program."""
    greet()
    boolean_variable: bool = True
    while boolean_variable is True:
      response: int = int(input("Select what your animal should do: 0-Get Berries, 1-Fight, 2-End Game "))
      if response == 0:
        berry_choice = int(input(player + ", Type the number of the berry you want: 0-strawberry, 1-blueberry, 2-raspberry "))
        get_berries(berry_choice)
        print(f"Points: {points}")
      elif response == 1:            
        fight()
      if response == 2:
        end_game()
        boolean_variable = False
    

def greet() -> None:
    """Prints welcome message, explains game, asks player for name"""
    global player
    print("Welcome! In this game, you have to train and take care of your animal. You're animal get berries to gain points. Also, to gain more points, your animal has to win a fight with another animal." + GRIN_EMOJI)
    player = input("What is your animal's name? ")

def get_berries(berry_choice: int) -> int:
    """Animal eats the berry it chose to restore health."""
    global points
    if berry_choice == 0:
      points += 7
    elif berry_choice == 1:
      points += 6
    elif berry_choice == 2:
      points += 5

    return points

def fight() -> None:
    """Animal fights and gets points depending on if they win or not."""
    global points
    fight_result: int = randint(0, 1)
    if fight_result == 0:
      points += 25
      print("You Win! "+ GRIN_EMOJI + f" Points: {points}")
      print("Great Job " + player)
    else:
      points -= 15
      print(f"You Lose!   Points:  {points}")
      print("Better luck next time, " + player)
      return points

def end_game() -> None:
    """Allows user to end game and displays their total adventure points."""
    global points
    print(f"Thanks for playing! Total Adventure Points: {points} " + GRIN_EMOJI)






if __name__ == "__main__":
  main()
