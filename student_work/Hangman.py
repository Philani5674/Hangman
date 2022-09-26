import random, time, string
from re import A

aphabets = list(string.ascii_uppercase)
tries = 1
selected_aphabet = []
selected_word = None
global word

# Hangs the man everytime when the trie is wrong.
def hangman(tries):
    a = ("   _____ \n"
 "  |      \n"
 "  |      \n"
 "  |      \n"
 "  |      \n"
 "  |      \n"
 "  |      \n"
 "__|__\n")
    b = ("   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |     | \n"
    "  |     O \n"
    "  |      \n"
    "  |      \n"
    "__|__\n")
    c =("   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |     | \n"
    "  |     O \n"
    "  |    / \ \n"
    "  |      \n"
    "__|__\n")
    d = ("   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |     | \n"
    "  |     O \n"
    "  |    /|\ \n"
    "  |      \n"
    "__|__\n")
    e = ("   _____ \n"
    "  |     | \n"
    "  |     |\n"
    "  |     | \n"
    "  |     O \n"
    "  |    /|\ \n"
    "  |    / \ \n"
    "__|__\n")
    man = [a,b,c,d,e]
    print(man[tries-1])

# increase the number of tries
def tries(tries):
    return tries +1


#prints alphabtes that are available for selection.
def print_Aphabets(alphabet):
    for i in aphabets:
        if i in selected_aphabet:
            i = "_"
    print(alphabet[0:10])
    print(alphabet[10:20])
    print(f"           {alphabet[20::]}")


#choose the word from the list
# returns one word
def choosing_the_word():
    words_file = open("words.txt")
    list_of_words = words_file.readlines()
    return random.choice(list_of_words)


#input the guess aphabet, and return the guessed alphabet
def guess():
    while True:
        guess_aphabet = input("Please input the aphabet correctly:>>>")
        if guess_aphabet in aphabets:
            if guess_aphabet not in selected_aphabet:
                return guess_aphabet


#Playing the game
def play():
    print(f"This is your {tries} try, make it worth it.")
    print("\n")
    hangman(tries)
    print("\n")
    print_Aphabets(aphabets)
    guess()
    tries()



#Playing the game
print("\n Hello welcome to hangman game, \n Let us get to the game without waasting any time.")
selected_word = choosing_the_word()
play()


