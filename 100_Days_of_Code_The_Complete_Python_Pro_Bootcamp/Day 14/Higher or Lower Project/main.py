from art import logo, vs
import game_data
import random


def random_game_data():
    random.seed()
    return random.choice(game_data.data)


def check_user_guess(A, B):
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    answer = 'A'
    greater_dict = A

    if A['follower_count'] < B['follower_count']:
        answer = 'B'
        greater_dict = B

    if user_guess == answer:
        return [True, greater_dict]

    return [False, greater_dict]


def game(compare_A, user_score):
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
