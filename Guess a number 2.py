def user_answer():
    """Function takes a statement from the user to define if the guessed number was correct:
    :rtype: str
    :return: user answer from ["too small", "too big", "you won"]"""

    possible_answers = ["too small", "too big", "you won"]
    while True:
        user = input().lower()
        if user in possible_answers:
            break
        print("User answer doesn't match ['too small', 'too big', 'you won']")

    return user


def guess_a_number():
    """Function checks whether number chosen by a computer matches user's choice"""
    print("Imagine number between 0 and 1000!")
    print("Press 'Enter' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_reply = ""
    while user_reply != "you won":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Your number is {guess}")
        user_reply = user_answer()
        if user_reply == "too big":
            max_number = guess
        elif user_reply == "too small":
            min_number = guess

    print("Hurrah I guessed!")


if __name__ == '__main__':
    guess_a_number()




