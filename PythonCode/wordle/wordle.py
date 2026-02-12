import random

WORD_LIST = ["apple", "crane", "slate", "point", "train", "ghost",
             "water", "house", "table", "chair", "plant", "ocean"]

MAX_GUESSES = 6
WORD_LENGTH = 5

GREEN = "G"
YELLOW = "Y"
GRAY = "GR"


def check_guess(secret_word, guess):
    feedback = [GRAY] * WORD_LENGTH
    secret_letters = list(secret_word)

    for i in range(WORD_LENGTH):
        if guess[i] == secret_letters[i]:
            feedback[i] = GREEN
            secret_letters[i] = None

    for i in range(WORD_LENGTH):
        if feedback[i] == GRAY and guess[i] in secret_letters:
            idx = secret_letters.index(guess[i])
            feedback[i] = YELLOW
            secret_letters[idx] = None

    return feedback


def play_game():
    secret_word = random.choice(WORD_LIST)
    guesses_left = MAX_GUESSES

    print("Welcome to Wordle!")
    print(f"Guess the {WORD_LENGTH}-letter word.")
    print(f"You have {MAX_GUESSES} guesses.\n")

    while guesses_left > 0:
        guess = input("Enter your guess: ").lower()

        if len(guess) != WORD_LENGTH or not guess.isalpha():
            print("Invalid guess. Use a 5-letter word.\n")
            continue

        feedback = check_guess(secret_word, guess)
        print(" ".join(feedback), "\n")

        if guess == secret_word:
            print("You win!")
            return

        guesses_left -= 1
        print(f"Guesses left: {guesses_left}\n")

    print("Game over!")
    print("The word was:", secret_word)


play_game()