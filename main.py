import time
import os
import random


HANGMAN_PICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

HANGMAN_WORDS = ["APPLE","CARROT","TELEPHONE", "CHOCOLATE","HARMONY", "BREATHE", "GOODBYE", "SHADOW", "WHISPER" ]

def get_all_pos(c, s):
    return [pos for pos, char in enumerate(s) if char == c]

def print_text(text):
    result = ""
    for letter in text:
        result += letter + " "
    print(result)

def game():
    MAX_FAIL = len(HANGMAN_PICS)-1

    i = 0
    current_word = random.choice(HANGMAN_WORDS)
    solution = len(current_word)*['_']

    os.system('cls')
    print(HANGMAN_PICS[i])
    print_text(solution)
     
    while i < MAX_FAIL: 
        letter= str(input("Guess a letter: ")).upper()
        pos_found = get_all_pos(letter, current_word)
        if len(pos_found) == 0:
            i+=1
        else:
            for pos in pos_found:
                solution[pos] = letter

        os.system('cls')
        print(HANGMAN_PICS[i])
        print_text(solution)

        if ''.join(solution) == current_word:
            break
                
    if i < MAX_FAIL:
        print("\nCongratulations you won!")
    else: 
        print("\nYou are dead!")
        print("The word was: "+ current_word)

game()


