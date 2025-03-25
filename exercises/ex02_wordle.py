"""Creating a wordle in COMP 110"""

__author__ = "730483620"


def contains_char(word: str, letter: str) -> bool:
    """First function to figure out correct letter of secret word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == letter:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Second function to highlight right or wrong guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result = ""
    i: int = 0
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if guess[i] == secret[i]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i = i + 1
    return result


def input_guess(length: int) -> str:
    """Third function to make sure the word entered is five characters"""

    while True:
        word = input(f"Enter a {length} character word")
        if len(word) == length:
            return word
        else:
            print(f"That wasn't {length} chars! Try again")


def main(secret: str) -> None:
    """The entry point of the program and main game loop."""
    turns: int = 6
    current_turn: int = 1
    guess: str = ""

    while current_turn <= turns:
        print(f"===Turn {current_turn}/{turns}===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {current_turn}/{turns} turns!")
            return
        current_turn += 1
    print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
