import random
from blackjack.logo import logo
print(logo)
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]

dealer_cards = []
your_cards = []

for i in range(0,2):
    dealer_cards.append(cards[random.randint(0, len(cards)-1)])
    your_cards.append(cards[random.randint(0, len(cards))-1])

if sum(dealer_cards) < 17:
    dealer_cards.append(cards[random.randint(0, len(cards)-1)])

print("Your cards : ",  your_cards)
print(f"Dealers first card : {dealer_cards[0]}")

choice = input("Type Y if you want to choose another card else type N ")
if choice == "Y":
    your_cards.append(cards[random.randint(0, len(cards))])
    print("Your cards ", your_cards)

if sum(your_cards) > 21 or sum(dealer_cards) > sum(your_cards):
    print("You lose")
    print(dealer_cards)
elif sum(your_cards) < 21 and sum(dealer_cards) > 21:
    print("You won")
    print(dealer_cards)
else:
    print("You win")
    print(dealer_cards)



