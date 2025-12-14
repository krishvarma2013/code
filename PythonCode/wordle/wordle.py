import random

WORD_LIST = ["apple", "crane", "slate", "point", "train", "ghost", "water", "house", "table", "chair", "plant", "ocean"]
max_guess = 6
word_length = 5
def check_guess(secret_word, guess):
    feedback = ['_'] * WORD_LENGTH
    secret_word_letters = list(secret_word)
    
   
    for i in range(WORD_LENGTH):
        if guess[i] == secret_word_letters[i]:
            feedback[i] = '#008000'
            secret_word_letters[i] = None
            
   
    for i in range(WORD_LENGTH):
        if feedback[i] == '_': 
            try:
                match_index = secret_word_letters.index(guess[i])
                feedback[i] = '#FFFF00'
                secret_word_letters[match_index] = None  # Mark as used
            except ValueError:
                pass