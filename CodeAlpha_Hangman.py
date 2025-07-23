import random

def choose_word():
    word_list = ["apple", "tiger", "robot", "grape", "plant"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print("🎮 Welcome to Hangman! Guess the word, one letter at a time.")
    
    while wrong_guesses < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong guess! {max_attempts - wrong_guesses} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)

def main():
    while True:
        play_hangman()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing Hangman!")
            break

main()
