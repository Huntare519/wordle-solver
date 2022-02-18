from wordle import print_guess_after_user_prompt, check_if_in, determine_next_guess, find_guess_results, parse_final_list


def test_wordle(answer, first_guess="crane"):
    i = 0
    guess_history = []
    letter_strings = []
    next_guess = first_guess

    while (i < 6):
        current_guess_list, guess = find_guess_results(answer, next_guess)
        guess_history.append(guess)
        print_guess_after_user_prompt(current_guess_list)
        next_guesses_list = check_if_in(current_guess_list, guess)
        next_guess_list, length = determine_next_guess(
            next_guesses_list, guess_history)
        parse_final_list(current_guess_list,
                         next_guesses_list,  letter_strings)
        next_guess = next_guess_list[0]
        print("words remaining:", length)
        i = i + 1


def main():
    test_wordle("dodge")


main()
