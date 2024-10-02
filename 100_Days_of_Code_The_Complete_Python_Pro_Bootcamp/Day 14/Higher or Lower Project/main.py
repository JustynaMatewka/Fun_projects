from art import logo, vs
import game_data
import random
random.seed()


def random_game_data():
    """Returns random data from given database (dictionary)"""
    return random.choice(game_data.data)


def check_user_guess(A, B):
    """Takes compare_A and compare_B values and returns if user guessed which of them have more followers
    (returns boolean and value A/B with more followers)"""
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if A['follower_count'] > B['follower_count']:
        return [user_guess == 'A', A]
    else:
        return [user_guess == 'B', B]


def game(compare_A, user_score):
    """Takes random compare_A and 0 as beginner user score
    and recurrently process game main functionalities until user give failure answer"""
    compare_B = random_game_data()

    print(logo)
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(vs)
    print(f"Compare B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")

    answer = check_user_guess(compare_A, compare_B)
    if answer[0]:
        user_score += 1
        print(f"You're right! Current score: {user_score}")
        game(answer[1], user_score)
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        return


game(random_game_data(), 0)
