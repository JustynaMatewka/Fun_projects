from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

def game_over(user_cards, computer_cards):
    print(f"Your final hand: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, current score: {sum(computer_cards)}")

def user_game_over():
    print("You lose :(")
    return False

def bust_user_game_over():
    print("You went over. You lose :(")
    return False

def bust_computer_game_over():
    print("Computer went over. You win :)")
    return False

def computer_game_over():
    print("You win :)")
    return False

def game():
    print(logo)

    user_cards = [draw_card(), draw_card()]
    computer_cards = [draw_card(), draw_card()]
    not_the_end = True

    while not_the_end:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            if sum(user_cards) > 21:
                game_over(user_cards, computer_cards)
                not_the_end = bust_user_game_over()
            else:
                user_cards.append(draw_card())
                if sum(user_cards) > 21:
                    game_over(user_cards, computer_cards)
                    not_the_end = bust_user_game_over()

        else:
            if sum(user_cards) < 17:
                user_cards.append(draw_card())
                print(f"You needed to draw a card.\nYour cards: {user_cards}, current score: {sum(user_cards)}")

                if sum(user_cards) > 21:
                    game_over(user_cards, computer_cards)
                    not_the_end = bust_user_game_over()

            if sum(computer_cards) < 17:
                computer_cards.append(draw_card())
                if sum(computer_cards) > 21:
                    game_over(user_cards, computer_cards)
                    not_the_end = bust_computer_game_over()
            elif sum(computer_cards) > 21:
                game_over(user_cards, computer_cards)
                not_the_end = computer_game_over()

            if sum(user_cards) > sum(computer_cards) and sum(user_cards) < 17 and sum(user_cards) < 17:
                game_over(user_cards, computer_cards)
                not_the_end = computer_game_over()
            else:
                game_over(user_cards, computer_cards)
                not_the_end = user_game_over()


continue_the_game = True
while continue_the_game:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        game()
    else:
        print("THE END, bye bye")
        continue_the_game = False