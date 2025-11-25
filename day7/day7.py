# Hangman
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6
placeholder = ""
print(logo)

chosen_word = random.choice(word_list)

for letter in chosen_word:
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    
    print(f"--------------------- {lives} LIVES LEFT ---------------------")
    
    guess = input("Guess a letter: ").lower()
    
    display = ""
    
    if guess in correct_letters:
        print(f"You already guessed {guess}, try again.")

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
    
    if lives == 0:
        game_over = True
        print(f"Your word was {chosen_word}. YOU LOSE.")
    
    if "_" not in display:
        game_over = True
        print("YOU WIN.")
        
    
    print(stages[lives])
    
