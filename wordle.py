from email.headerregistry import ContentTransferEncodingHeader
import emoji
import fnmatch
import re
from english_words import english_words_lower_alpha_set


def get_users_guess():
    guess_list = []
    users_input = input("please enter your wordle guess:")

    # create dictionary with [char]:[information]
    for char in users_input:
        guess_list.append([char, 3])

    for letter in guess_list:
        # show prompt each time
        print("for each letter in your guess, please enter:")
        print("(1) if the letter is in the correct spot (i.e. green box emoji)")
        print("(2) if the letter is correct but it is in the wrong spot (i.e.yellow emoji)")
        print("(3) if the letter is not correct (i.e.grey emoji)")
        # show user letter in guess
        print(letter[0])
        char_information = input("enter a number: ")
        while (int(char_information) > 3 or int(char_information) < 1):
            print("not valid. please enter 1, 2, or 3")
            char_information = input("enter a number: ")
        letter[1] = char_information
    return guess_list


def print_guess_after_user_prompt(guess_list):
    print("\n--Your Wordle Guess--\n")
    for letter in guess_list:
        if int(letter[1]) == 1:
            # end='' allows to print on the same line
            print(emoji.emojize(' 🟩 '), end='')
        if int(letter[1]) == 2:
            print(emoji.emojize(' 🟨 '), end='')
        if int(letter[1]) == 3:
            print(emoji.emojize(' ⬛️ '), end='')
    print()  # return new line after string is built


def check_if_in(guess_list):
    letters_spot_known = ""
    letters_spot_unknown = ""
    for letter in guess_list:
        if int(letter[1]) == 1:
            letters_spot_known = letters_spot_known + letter[0]
        elif int(letter[1]) == 2:
            letters_spot_known = letters_spot_known + "?"
            letters_spot_unknown = letters_spot_unknown + letter[0]
        elif int(letter[1]) == 3:
            letters_spot_known = letters_spot_known + "?"

    print(letters_spot_known)
    print(letters_spot_unknown)
    # first search for words with the known letters and wildcard. return that set / list
    possible_words = fnmatch.filter(
        english_words_lower_alpha_set, letters_spot_known)
    # next search for words that contained the known order and letters that we know are in it but not in correct order
    next_guess_list = []
    for word in possible_words:
        if (re.search(letters_spot_unknown, word)):
            next_guess_list.append(word)
    return next_guess_list


def main():
    guess_list = get_users_guess()
    print_guess_after_user_prompt(guess_list)
    next_guess_list = check_if_in(guess_list)
    print(next_guess_list)
    #print("e" in "frame")


main()
# take guess from user
# (ex) adieu
# store guess from user
# ask if the word is in the right spot or wrong spot or not at all
# update string with letters, maintaining the right spot
# query english words for a 5-letter word that contains the letters
# output a word that might work and update a list of words that might work
