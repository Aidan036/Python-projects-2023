import settings
import settings as settings
import random

def game ():
    word = random.choice(settings.WORDS)
    so_far = " "*len(word)
    used_letters = []

    print("welcome to hangman, Good luck")
    while settings.guesses < setting.max_guess and so_far != word:

        print("you have used the following letters")
        print(used_letters+"\n\n")

        print(settings.HANGMAN[settings.guesses])

        print"\nSo Far, the word is:\n", so_far)

        guess = " "
        while guess in used_letters:
            guess = input("\n\npick a letter: ")
            if guess.isalpha():
                guess = guess.lower()
            else:
                continue
            used_letters.append(guess)

            if guess in word:
                print("\nYes!", guess, "is in the word!")
                new = ""
                for i in range(len(word)):
