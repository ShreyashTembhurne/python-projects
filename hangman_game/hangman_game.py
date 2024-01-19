
import random
from hangman_words import word_list 
chosen_word = random.choice(word_list);
word_length = len(chosen_word)

display =[]
for _ in range(word_length):
    display += "_"
print(display)

end_of_game =False
lives = 6

from hangman_art import logo, stages
print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower();

    if guess in display:
      print(f" '{guess}' is previously entered")    
       
    #Check gussed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            print(f" The choosen word is {chosen_word}." )

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win.")

    print(stages[lives])

   