from wordle import print_guess_after_user_prompt, check_if_in, determine_next_guess, find_guess_results


def test_wordle(answer, first_guess="crane"):
    i = 0
    guess_history = []
    next_guess = first_guess

    while (i < 6):
        guess_list, guess = find_guess_results(answer, next_guess)
        guess_history.append(guess)
        print_guess_after_user_prompt(guess_list)
        next_guess_list = check_if_in(guess_list, guess)
        next_guess_list, length = determine_next_guess(
            next_guess_list, guess_history)
        next_guess = next_guess_list[0]
        print("words remaining:", length)
        i = i + 1


def main():
    test_wordle("caulk")


main()
