# hangman.py
#   Sarah Ramdhany
#   This code simulates hangman by prompting user to input a letter
def main():
    import random

    # Initialize hangman game
    secrets = ["I love python", "Hello, world!", "Programming is FUN!"]
    bodyparts = ["head", "nose", "left ear", "right_ear",
                     "left eye", "right eye", "mouth", "neck",
                     "left arm", "right arm", "torso", "left leg", "right leg"]

    # Start game
    selection = 0
    while selection != 2:
    
        # Initialize bodyparts, its counter, and guesses 
        part_count = 0
        guesses = []
        # Initialize hangmanStr
        sentence = random.randrange(0, len(secrets))
        hangmanStr = secrets[sentence]
        # Initialize secret sentence
        secret = []
        for ch in hangmanStr:
            if ch.isalpha():
                secret.append("_")
            else:
                secret.append(ch)

        # Display game
        print("Welcome to the Hangman Game!")
        print("The secret sentence is:", " ".join(secret))
        
        # Prompt user for letter
        while "_" in secret and part_count < 13:
            print()
            letter = input("Please enter a letter: ")
            # Validate guess
            letter = letter.strip()
            if len(letter) > 1:
                print("'", letter, "' is not a single letter.", sep = "")
                print("Please guess only one letter at a time ...")
                continue
            if letter.isalpha() == False:
                print("'", letter, "' is not a letter.", sep = "")
                print("Please enter a letter ...")
                continue
            if letter.lower() in guesses or letter.upper() in guesses:
                print("You guessed that already!")
                continue
            # Record guess
            else:
                guesses.append(letter.lower())

            # Process correct guess
            if letter.lower() in hangmanStr.lower():
                # Determine and display number of occurrences of guess in string
                frequency = hangmanStr.lower().count(letter.lower())
                if frequency == 1:
                    print("Found 1 occurrence of the letter '", letter.lower(), "' in the sentence", sep = "")
                else:
                    print("Found ", frequency, " of the letter '", letter.lower(), "' in the sentence", sep = "")
                # Reveal secret sentence
                position = 0
                for ch in hangmanStr:
                    if ch.lower() == letter.lower():
                        position = hangmanStr.index(ch, position)
                        secret[position] = ch
                        position += 1

            # Process incorrect guess
            else:
                part = bodyparts[part_count]
                print("Sorry, that letter is not in the sentence.")
                print("You have now added a", part, "to the hangman.")
                part_count += 1

            # Display secret sentence and user's previous guesses
            print("The secret sentence is:", " ".join(secret))
            print("Letters used thus far:", ", ".join(guesses))

        # Display winner
        print()
        if "_" not in secret:
            print('You win! :-)!! The hangman sentence is: "', hangmanStr, '".', sep = '')
        else:
            print("Sorry! You lose :-(.")

        # Prompt user to play again or quit
        print()
        print("Thank you for playing the Hangman Game!")
        print()
        print("Would you like to play again or quit?")
        print("1. Play again!")
        print("2. Quit!")
        print()
        selection = 0
        while selection != 1 and selection != 2:
            selection = input("Enter 1 or 2: ")
            selection = selection.strip()
            if selection.isdigit() == False:
                print("'", selection, "' is not a valid option.", sep = "")
                print("Please enter 1 to play again or 2 to quit ...")
                print()
                continue
            else:
                selection = eval(selection)
            if selection != 1 and selection != 2:
                print("'", selection, "' is not a valid option.", sep = "")
                print("Please enter 1 to play again or 2 to quit ...")
                print()
        print()
    print("It was a pleasure playing with you!  Goodbye!")
main()
