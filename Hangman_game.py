import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_"]*len(chosen_word)
number_of_lives = 6
print(display)
game_over = False


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def fill_character(ch):
    global number_of_lives, game_over
    index = 0
    char_found = False
    for character in chosen_word:
        if character == ch:
            display[index] = guess
            char_found = True
        index +=1
    if not char_found:
        number_of_lives -=1
        if number_of_lives == 0:
            game_over = True
            print(stages[number_of_lives])
            print("You lose")
        else:
            print(stages[number_of_lives])
    print(display)



while not game_over:
    guess = input("Guess a character").lower()
    fill_character(guess)
    if "_" not in display:
        print("You won")
        break




