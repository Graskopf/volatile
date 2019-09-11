# Welcome the user to the game
name = input("What is your name? ")
print ("Welcome to my first version of the hangman-game, " + name)

# Import wordlist
import words
random_word = words.get_words()

# Start the game
print ("Start guessing! Will you win or will you")

# Get random word from the wordlist
word = (random_word)
for i in range(len( word )):
    print("___ ", end=" ")

# The user can try guessing up to 10 times
guesses = ""
turns = 10
while turns > 0:
    failed = 0
    for char in (word):
        if char in guesses:
            print (char, end= "")
        else:
            print ("___", end=" ")
            failed += 1
    if failed == 0:
        print ("")
        print ("You won \U0001f600")
        break

# Have the user to guess characters
    guess = input(" Guess a character in the word: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print ("Wrong, you have", + turns, "more guesses left")
        if turns == 0:
            print ("")
            print (" You lost " + "😢")