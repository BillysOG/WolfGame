import random as r

def print_hangman(wrongs,hidden_word):
    for line in HANGMAN[wrongs]:
        print(line)
    print(*hidden_word, sep=" ")

def making_a_guess(wrongs,hidden_word,right):
    guess = input("\nGuess the letter : ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess and hidden_word[i] == "_":
                hidden_word[i] = guess
                right += 1
    else:
        wrongs += 1
    return wrongs,right

HANGMAN = {0 :("   ",
               "   ",
               "   "),
           1: (" o ",
               "   ",
               "   "),
           2: (" o ",
               " | ",
               "   "),
           3: (" o ",
               "/| ",
               "   "),
           4: (" o ",
               "/|\\",
               "   "),
           5: (" o ",
               "/|\\",
               "/  "),
           6: (" o ",
               "/|\\",
               "/ \\")
           }

WORD_LIST = ["elephant", "umbrella", "mountain", "chocolate", "butterfly",
         "adventure", "pineapple", "nightmare", "happiness", "treasure",
         "waterfall", "strawberry", "galaxy", "fireworks", "hurricane",
         "mystery", "telescope", "champion", "horizon", "whirlwind",
         "dandelion", "sunflower", "harmony", "caterpillar", "dragonfly",
         "paradise", "moonlight", "lightning", "voyager", "explorer",
         "carousel", "symphony", "universe", "labyrinth", "marathon",
         "reinforms", "butterscotch", "constellation", "volcano", "peppermint",
         "sapphire", "enchantment", "lighthouse", "serenity", "buttercup",
         "oceanic", "gargoyle", "whimsical", "crescendo", "mermaid", "firecracker"]

right = 0
wrongs = 0
chosen_word = r.choice(WORD_LIST)
hidden_word = ["_"] * len(chosen_word)

def main(wrongs,right):
    print("*******************")
    print("Welcome to HANGMAN!")
    print("*******************\n")

    while wrongs < 6 and right < len(chosen_word):
        print_hangman(wrongs,hidden_word)
        wrongs,right = making_a_guess(wrongs,hidden_word,right)

    print_hangman(wrongs,hidden_word)
    if right == len(chosen_word):
        print(f"\nCongratulations! You guessed '{chosen_word}' correctly!")
        print(f"With {wrongs} incorrect guesses!")
    else:
        print("\nYou lost! Too bad!")
        print(f"The chosen word was '{chosen_word}'")
        print("Better luck next time!")

if __name__ == "__main__":
    main(wrongs,right)