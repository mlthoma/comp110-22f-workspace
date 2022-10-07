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
        response = int(input("Select what your animal should do: 0-Get Berries, 1-Fight, 2-End Game "))
        if response == 0:
            global points
            get_berries()
            print(f"Points: {points}")
        elif response == 1:            
            fight(points)
        if response == 2:
            end_game()
            boolean_variable = False


def greet() -> None:
    """Prints welcome message, explains game, asks player for name."""
    global player
    print("Welcome! In this game, you have to train and take care of your animal. You're animal get berries to gain points. Also, to gain more points, your animal has to win a fight with another animal " + GRIN_EMOJI + ".")
    player = input("What is your animal's name? ")


def get_berries() -> None:
    """Animal eats the berry it chose to restore health."""
    global points
    berry_choice = int(input(f"{player}, Type the number of the berry you want: 0-strawberry, 1-blueberry, 2-raspberry "))
    if berry_choice == 0:
        points += 7
    elif berry_choice == 1:
        points += 6
    elif berry_choice == 2:
        points += 5


def fight(points_1: int) -> int:
    """Animal fights and gets points depending on if they win or not."""
    global points
    fight_choice = int(input(f"{player}, would you like to fight with a wolf or a tiger? Press 1 for wolf or 2 for tiger: "))
    fight_result: int
    if fight_choice == 1:
        fight_result = randint(0, 1)
        if fight_result == 0:
            points = points_1 + 25
            print(f"You Win! {GRIN_EMOJI} Points: {points}")
            print(f"Great Job {player}")
        else:
            points = points_1 - 15
            print(f"You Lose!   Points:  {points}")
            print(f"Better luck next time, {player}")
    else:
        fight_result = randint(0, 1)
        if fight_result == 0:
            points = points_1 + 25
            print(f"You Win! {GRIN_EMOJI} Points: {points}")
            print(f"Great Job {player}")
        else:
            points = points_1 - 15
            print(f"You Lose!   Points:  {points}")
            print(f"Better luck next time, {player}")
    return points


def end_game() -> None:
    """Allows user to end game and displays their total adventure points."""
    global points
    print(f"Thanks for playing {player}! Total Adventure Points: {points} {GRIN_EMOJI}")


if __name__ == "__main__":
    main()
