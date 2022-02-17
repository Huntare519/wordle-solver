from email.headerregistry import ContentTransferEncodingHeader
import emoji
import fnmatch
import re
from english_words import english_words_lower_alpha_set
from read_json import get_frequency_based_priors


def get_users_guess():
    guess_list = []
    users_input = input("please enter your wordle guess: ")

    # create dictionary with [char]:[information]
    for char in users_input:
        guess_list.append([char, 3])

    for letter in guess_list:
        # show prompt each time
        print("for each letter in your guess, please enter: ")
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
    return users_input, guess_list


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


def check_if_in(guess_list, users_input):
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


def determine_next_guess(users_input, next_guess_list, guess_history):
    word_prob_dictionary = get_frequency_based_priors()
    # returns something like {shake: 0.909091}
    final_dict = {}

    # can we assign a probability to each word here and return the highest one
    for guess in next_guess_list:
        if (guess in guess_history):
            next_guess_list.remove(guess)
        try:
            final_dict.update({guess: word_prob_dictionary[guess]})
        except KeyError:
            # handle differences in list gracefully / silently
            continue
    # reverse the dict for highest probability first
    final_list = sorted(final_dict, key=final_dict.get, reverse=True)
    for previous in guess_history:
        if previous in final_list:
            final_list.remove(previous)
    return final_list


def main():
    i = 0
    guess_history = []
    while (i < 6):
        print("Guess Number:", i)
        users_input, guess_list = get_users_guess()
        guess_history.append(users_input)
        print_guess_after_user_prompt(guess_list)
        next_guess_list = check_if_in(guess_list, users_input)

        # need to parse out the old guess
        next_guess = determine_next_guess(
            users_input, next_guess_list, guess_history)
        print("Your next guess should be:", next_guess[0])
        i = i + 1


main()
