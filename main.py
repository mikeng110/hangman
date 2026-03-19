import time
import os

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


def game():
    i = 0
    while True: 
        print("Lets play a game!")

        if i > 6: i = 0
        os.system('cls')
        print(HANGMAN_PICS[i])
        
        time.sleep(1)
        i+=1

game()
