from email.headerregistry import ContentTransferEncodingHeader
from english_words import english_words_lower_alpha_set


def get_users_guess():
    i = 0
    guess_dictionary = {}
    users_input = input("please enter your wordle guess:")

    # create dictionary with [char]:[information]
    for char in users_input:
        guess_dictionary.update({char: 3})

    # for key, value in guess_dictionary.items():
    #     print("k->", key, "v->", value)

    for key, value in guess_dictionary.items():
        # show prompt each time
        print("for each letter in your guess, please enter:")
        print("(1) if the letter is in the correct spot (i.e. green box emoji)")
        print("(2) if the letter is correct but it is in the wrong spot (i.e.yellow emoji)")
        print("(3) if the letter is not correct (i.e.grey emoji)")
        # show user letter in guess
        print(key)
        char_information = input("enter a number: ")
        guess_dictionary[i] = char_information
        i = i + 1


def check_if_in(wordle):
    is_in = "frame" in english_words_lower_alpha_set
    return is_in


def main():
    get_users_guess()


main()
# take guess from user
# (ex) adieu
# store guess from user
# ask if the word is in the right spot or wrong spot or not at all
# update string with letters, maintaining the right spot
# query english words for a 5-letter word that contains the letters
# output a word that might work and update a list of words that might work
