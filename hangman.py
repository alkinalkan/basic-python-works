import random

def hangman():
    words = ['python', 'hangman', 'game', 'openai', 'programming']  # List of words to choose from
    word = random.choice(words).lower()  # Choose a random word from the list
    guessed_letters = []
    tries = 6  # Number of tries the player has

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 tries.")

    while True:
        print("\n")

        # Display the word with blanks for unguessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Check if the player has won or lost
        if "_" not in display_word:
            print("Congratulations! You guessed the word correctly!")
            break
        elif tries == 0:
            print("Game over! You ran out of tries. The word was:", word)
            break

        guess = input("Guess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess not in word:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
        else:
            print("Correct guess!")

hangman()
