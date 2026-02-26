# **Hangman Game (Python CLI)**

A command‑line implementation of the classic Hangman game. The program selects a random word from a predefined list, and the player attempts to guess the word one letter at a time. The game tracks remaining lives, displays ASCII‑based hangman stages, and ends when the player either completes the word or runs out of lives.

---

## **Project Overview**

This project demonstrates core Python concepts:

- Random word selection  
- Loops and conditional logic  
- List manipulation  
- Modular code organization  
- ASCII art rendering  

Two supporting modules provide assets:

- `hangman_words.py` — list of possible words  
- `hangman_art.py` — logo and hangman stages  

---

## **Prerequisites**

- Basic Python knowledge  
- Familiarity with loops, conditionals, and lists  

---

## **How the Game Works**

### **1. Word Selection**
A random word is chosen from the word list:

```python
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
```

### **2. Game State Initialization**
- `lives` starts at 6  
- `display` holds underscores representing each letter  
- `end_of_game` controls the main loop  

```python
end_of_game = False
lives = 6
display = ["_"] * word_length
```

### **3. Main Game Loop**
The player guesses letters until they win or lose:

```python
while not end_of_game:
    guess = input("Guess a letter: ").lower()
```

### **4. Guess Handling**
- Warns if a letter was already guessed  
- Reveals correct letters in the display  
- Deducts a life for incorrect guesses  

```python
if guess in display:
    print(f'letter {guess} has been previously entered')
```

### **5. Win/Loss Conditions**
- Player wins when no underscores remain  
- Player loses when lives reach zero  

```python
if "_" not in display:
    end_of_game = True
    print("You win.")
```

---

## **Displaying Progress**

Each turn prints:

- The current word state  
- The ASCII hangman stage based on remaining lives  

```python
print(" ".join(display))
print(hangman_art.stages[lives])
```

---

## **Complete Code**

```python
#import the random module, hangman ascii art and words
import random
import hangman_art
import hangman_words

#print the logo
print(hangman_art.logo)

#make the choosen words random
chosen_word = random.choice(hangman_words.word_list)

#find the length of the choosen word
word_length = len(chosen_word)

#create a variable to use in determining the end of the game
end_of_game = False

#create a variable for the number of lives 
lives = 6

#Create a list
display = []

#add a dash to represent each word in the choosen word and add it to the list
for _ in range(word_length):
    display += "_"

#create a while loop using the end_of_game variable earlier created so that the questions will repeatedly come up
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #introduce a conditional statement so that if the word has been previously entered, it will inform them.
    if guess in display:
        print(f'letter {guess} has been previously entered')
        
    #loop through the choosen word to replace the blanks with the correct letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    #this checks if user is wrong and deducts the lives with a feedback message.
    if guess not in chosen_word:
        lives -= 1
        print(f" you entered {guess} and it's not in the word.")
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lose, you have no lives left ")
            print(f" The choosen word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f" The choosen word is {chosen_word}")

    #print the corresponding art to the number of lives left
    print(hangman_art.stages[lives])
```

---

## **Conclusion**

This project provides a complete, interactive Hangman game built using fundamental Python concepts. It highlights modular design, user input handling, and visual feedback through ASCII art.

---
