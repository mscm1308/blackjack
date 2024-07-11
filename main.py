import random

print("="*10+"Blackjack"+"="*10+"\n")

print("Starting Game...\n")

suits = ("Clubs","Spades","Hearts","Diamonds")

numbered_cards = ("2","3","4","5","6","7","8","9")

face_cards = ("King", "Queen", "Jack", "Ace")

deck = {}

for i in range(4):
    for j in range(4):
        if face_cards[i] == "Ace":
            deck.update({f"{face_cards[i]} of {suits[j]}":1})
        else:
            deck.update({f"{face_cards[i]} of {suits[j]}":10})

for i in range(8):
    for j in range(4):
        deck.update({f"{numbered_cards[i]} of {suits[j]}":int(numbered_cards[i])})

#print(deck)

computer_hand = {}
user_hand = {}

def print_hand(player,hand):
    print(f"{player} has: {sum(hand.values())}")
    for k in hand.keys():
        print(k)
    print("")

print("Dealing Cards!\n")

for i in range(4):
    random_card_key = random.choice(list(deck.keys()))
    random_card = {f"{random_card_key}":deck.pop(random_card_key)}
    if i % 2:
        computer_hand.update(random_card)
        print(f"Dealer gets {random_card_key}\n")
    else:
        user_hand.update(random_card)
        print(f"Player gets {random_card_key}\n")
'''
for i in range(2):
    random_card = random.choice(list(deck.keys()))
    computer_hand.update({f"{random_card}":deck.pop(random_card)})

for i in range(2):
     random_card = random.choice(list(deck.keys()))
     player_hand.update({f"{random_card}":deck.pop(random_card)})
'''
#computer_hand.update(deck.pop(random.choice(deck_cards)))
#computer_hand.update(deck.pop(random.choice(list(deck.keys()))))

#print(f"Dealer has: {sum(computer_hand.values())} {list(computer_hand.keys())}")
#print(f"Player has: {sum(player_hand.values())} {list(player_hand.keys())}")

game_over = False

while game_over != True:
#    print(f"Dealer has: {sum(computer_hand.values())} {list(computer_hand.keys())}")
#    print(f"Player has: {sum(user_hand.values())} {list(user_hand.keys())}")

    print_hand("Dealer",computer_hand)
    print_hand("Player",user_hand)

    computer_skipped = False
    
    user_choice = input("Do you want to Hit (h) or Stay (s): ").lower()

    if user_choice == 'h':
        random_card = random.choice(list(deck.keys()))
        user_hand.update({f"{random_card}":deck.pop(random_card)})
        print(f"\n+Player gets {random_card}\n")

    if random.choice(range(2)):
        random_card = random.choice(list(deck.keys()))
        computer_hand.update({f"{random_card}":deck.pop(random_card)})
        print(f"\n+Dealer gets {random_card}")
    else:
        computer_skipped == True
        print("\n|Dealer stayed")

    if sum(user_hand.values()) == 21 or sum(computer_hand.values()) == 21:
        game_over = True

    if sum(user_hand.values()) > 21 or sum(computer_hand.values()) > 21:
        game_over = True

    if computer_skipped and user_choice == 's':
        game_over = True
        print("Both skipped")

print("\nFinal score\n")

#print(f"Dealer has: {sum(computer_hand.values())} {list(computer_hand.keys())}")
#print(f"Player has: {sum(user_hand.values())} {list(user_hand.keys())}")

print_hand("Dealer",computer_hand)
print_hand("Player", user_hand)

