import random

# Predefined list of words
words = ["apple", "banana", "grape", "orange", "mango"]
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Display word with blanks
def display_word():
    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while incorrect_guesses < max_incorrect:
    print("\nWord:", display_word())
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Incorrect! You have", max_incorrect - incorrect_guesses, "guesses left.")

    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break
else:
    print("\n💀 Game over! The word was:", word_to_guess)
