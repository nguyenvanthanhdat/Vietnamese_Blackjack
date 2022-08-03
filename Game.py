import numpy as np

# create a deck of cards
deck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 16]
known_cards = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
token_cards = 0
num_players = 0
min_dealer_score = -1

# nó thắng thằng 17 nó sẽ từ 18 -> 21 sẽ tính xác suất từ 18 -> 21 tính kì vọng
# cần nhập min_dealer_score


def input_game():
    my_cards = input("Nhập bài trên tay của bạn: ")
    my_cards = [min(int(x), 10) for x in my_cards.split()]
    for i in my_cards:
        deck[i - 1] -= 1
        known_cards[i - 1] += 1
    your_cards = input("Nhập bài đã biết: ")  # không tính trên tay mình
    your_cards = [min(int(x), 10) for x in your_cards.split()]
    for i in your_cards:
        deck[i - 1] -= 1
        known_cards[i - 1] += 1
    token_cards = int(input("Số lá đã rút: "))
    num_players = int(input("Số người chơi: "))
    min_dealer_score = int(input("Điểm tối thiểu của người đặt: "))
    return token_cards, num_players, min_dealer_score


# Test

token_cards, num_players, min_dealer_score = input_game()
print(52 - 2 * num_players - token_cards)
print(known_cards)
print(deck)
print(min_dealer_score)
