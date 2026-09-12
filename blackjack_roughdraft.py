
import random


def special_display(string):
    for i in list(string):
        print(i,end="")
        for i in range(3000):
            print("",end="")
    print()


input("Press Enter to start")
special_display("\nWelcome to three card poker! You have $10,000 to gamble, have fun!\n")
special_display("Minimum bet is $100 with $50 increments\nMaximum bet is $50,000, Maximum pair plus is $5,000\n")

balance = 10000

cards = {14 : "Ace", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten", 11 : "Jack", 12 : "Queen", 13 : "King"}
suite = ["Spades", "Hearts", "Diamonds", "Clubs"]
hands = {"Straight Flush" : 6, "Three of a kind" : 5, "Straight" : 4, "Flush" : 3, "Pair" : 2, "High Card" : 1}

def get_max(value):
    value.sort()
    return value[-1]

def straight(value):
    value.sort()
    if value[0] + 1 == value[1] and value[1] + 1 == value[2]:
        return True
    return False

def flush(suites):
    if suites[0] == suites[1] and suites[1] == suites[2]:
        return True
    return False

def value(hand):
    value = []
    suites = []
    for values in hand:
        x = values.split()
        suites.append(x[-1])
        for i in range(2,15):
            if cards[i] in values:
                    value.append(i)
    return (value, suites)
                    
def get_hand(value, suites):
    if value[0] == value[1] and value[0] == value[2]:
        return ("Three of a kind", sum(value), 5, 31)
    if straight(value) and flush(suites):
        return ("Straight Flush", sum(value), 6, 41)
    if straight(value):
        return ("Straight", sum(value), 2, 7)
    if flush(suites):
        return ("Flush", get_max(value), 2, 5)
    if value[0] == value[1] or value[1] == value[2] or value[0] == value[2]:
        if value[0] == value[1]:    
            return ("Pair", value[0], get_max(value), 2, 2)
        if value[1] == value[2]:
            return ("Pair", value[1], get_max(value), 2, 2)
        if value[0] == value[2]:
            return ("Pair", value[2], get_max(value), 2, 2)
    return ("High Card", get_max(value), 2, 0)

def display_bet(bet, balance):
    special_display(f"\n{balance}\n-{bet}")
    

                
                
                
while balance > 0:
    special_display(f"You have ${balance}")
    bet = input("Place your ante bet: ")
    all_in = False
    try:
        bet = int(bet)
    except ValueError:
        bet = 7
    
    while True:
        if bet % 50 != 0 or bet < 100:
            bet = int(input("Invalid bet, $100 minimum and increments: "))
        elif bet > balance or bet * 2 > balance:
            bet = int(input("You don't have that much money, try again: "))
        else:
            break
    
    if bet * 2 == balance:
        all_in = True
    
    if all_in:
        pair_plus = 0
    else:
        pair_plus = input("Place your pair plus: ")
        
        if pair_plus == "":
            pair_plus = 0
        
        try:
            pair_plus = int(pair_plus)
        except ValueError:
            pair_plus = 7
    
        
        
    while True:
        if pair_plus % 50 != 0:
            pair_plus = int(input("Invalid pair plus, $100 minimum and $50 increments: "))
        elif pair_plus + bet > balance:
            pair_plus = int(input("You don't have that much money, try again: "))
        else:
            break   
    balance -= (bet + pair_plus)
    special_display(f"\n{balance}\n-{bet + pair_plus}\n")
    cards_played = []
    hand = []
    dealer = []
    while len(cards_played) < 6:
        card = f"{cards[random.randint(2,14)]} of {random.choice(suite)}"
        if not(card in cards_played):
            cards_played.append(card)
            if len(hand) < 3:
                hand.append(card)
            else:
                dealer.append(card)
    special_display(f"You have {hand[0]}, {hand[1]}, {hand[2]}\n")
    
    your_value, your_suites = value(hand)
    your_hand = get_hand(your_value, your_suites)
    
    dealer_value, dealer_suites = value(dealer)
    dealer_hand = get_hand(dealer_value, dealer_suites)
    
    
    move = input("Fold or Play? ").capitalize()
    while True:
        if move != "Fold" and move != "Play":
            move = input("Invalid move! Type fold or play: ").capitalize()
        else:
            break
    if move == "Fold":
        special_display(f"You folded! The dealer has {dealer[0]}, {dealer[1]}, {dealer[2]}")
    elif move == "Play":
        balance -= bet
        special_display(f"\n{balance}\n-{bet}\n")
        bet *= 2
        special_display(f"The dealer has {dealer[0]}, {dealer[1]}, {dealer[2]}")
        if hands[dealer_hand[0]] > hands[your_hand[0]]:
            special_display(f"Your {your_hand[0]} against a {dealer_hand[0]}, You lose!")
            if balance < balance + pair_plus * your_hand[-1]:
                balance += pair_plus * your_hand[-1]
                special_display(f"\n{balance}\n+{pair_plus * your_hand}\n")
            
        elif hands[dealer_hand[0]] < hands[your_hand[0]] and dealer_hand[0] == "High Card" and dealer_hand[1] < 12:
            balance += (bet + pair_plus * your_hand[-1])
            special_display(f"Your {your_hand[0]} against a {dealer_hand[0]}, dealer folds and you win!")
            special_display(f"\n{balance}\n+{bet + pair_plus * your_hand[-1]}\n")
        elif hands[dealer_hand[0]] < hands[your_hand[0]]:
            balance += (bet * your_hand[-2] + pair_plus * your_hand[-1])
            special_display(f"Your {your_hand[0]} against a {dealer_hand[0]}, You win!")
            special_display(f"\n{balance}\n+{bet * your_hand[-2] + pair_plus * your_hand[-1]}\n")
        elif hands[dealer_hand[0]] == hands[your_hand[0]]:
            if hands[dealer_hand[0]] in [6, 5, 4]:
                if dealer_hand[1] > your_hand[1]:
                    special_display("The dealer's hand is heavier than yours. You lose!")
                    if balance < balance + pair_plus * your_hand[-1]:
                        balance += pair_plus * your_hand[-1]
                        special_display(f"\n{balance}\n+{pair_plus * your_hand}\n")
                elif dealer_hand[1] < your_hand[1]:
                    balance += (bet * your_hand[-2] + pair_plus * your_hand[-1])
                    special_display("Your hand is heavier than the dealer's. You win!")
                    special_display(f"\n{balance}\n+{bet * your_hand[-2] + pair_plus * your_hand[-1]}\n")
                elif dealer_hand[1] == your_hand[1]:
                    balance += bet + pair_plus * your_hand[-1]
                    special_display("TIE")
                    special_display(f"\n{balance}\n+{bet + pair_plus * your_hand}\n")
            elif hands[dealer_hand[0]] == 3:
                if dealer_hand[1] > your_hand[1]:
                    special_display("The dealer's hand is heavier than yours. You lose!")
                    if balance < balance + pair_plus * your_hand[-1]:
                        balance += pair_plus * your_hand[-1]
                        special_display(f"\n{balance}\n+{pair_plus * your_hand}\n")
                elif dealer_hand[1] < your_hand[1]:
                    balance += (bet * your_hand[-2] + pair_plus * your_hand[-1])
                    special_display("Your hand is heavier than the dealer's. You win!")
                    special_display(f"\n{balance}\n+{bet * your_hand[-2] + pair_plus * your_hand[-1]}\n")
                elif dealer_hand[1] == your_hand[1]:
                    balance += bet + pair_plus * your_hand[-1]
                    special_display("TIE")
                    special_display(f"\n{balance}\n+{bet + pair_plus * your_hand}\n")
            elif hands[dealer_hand[0]] == 2:
                if dealer_hand[1] > your_hand[1]:
                    special_display("The dealer's hand is heavier than yours. You lose!")
                    if balance < balance + pair_plus * your_hand[-1]:
                        balance += pair_plus * your_hand[-1]
                        special_display(f"\n{balance}\n+{pair_plus * your_hand}\n")
                elif dealer_hand[1] < your_hand[1]:
                    balance += (bet * your_hand[-2] + pair_plus * your_hand[-1])
                    special_display("Your hand is heavier than the dealer's. You win!")
                    special_display(f"\n{balance}\n+{bet * your_hand[-2] + pair_plus * your_hand[-1]}\n")
                elif dealer_hand[1] == your_hand[1]:
                    if dealer_hand[2] > your_hand[2]:
                        special_display("The dealer's hand is heavier than yours. You lose!")
                        if balance < balance + pair_plus * your_hand[-1]:
                            balance += pair_plus * your_hand[-1]
                            special_display(f"\n{balance}\n+{pair_plus * your_hand}\n")
                    elif dealer_hand[2] < your_hand[2]:
                        balance += (bet * your_hand[-2] + pair_plus * your_hand[-1])
                        special_display("Your hand is heavier than the dealer's. You win!")
                        special_display(f"\n{balance}\n+{bet * your_hand[-2] + pair_plus * your_hand[-1]}\n")
                    elif dealer_hand[2] == your_hand[2]:
                        balance += bet + pair_plus * your_hand[-1]
                        special_display("TIE")
                        special_display(f"\n{balance}\n+{bet + pair_plus * your_hand}\n")
            else:
                if dealer_hand[1] > your_hand[1]:
                    special_display(f"Your {cards[your_hand[1]]} high card against a {cards[dealer_hand[1]]} high card. You lose!")
                elif dealer_hand[1] < your_hand[1]:
                    balance += (bet * your_hand[-2] + pair_plus * your_hand[-1])
                    special_display(f"Your {cards[your_hand[1]]} high card against a {cards[dealer_hand[1]]} high card. You win!")
                    special_display(f"\n{balance}\n+{bet * your_hand[-2] + pair_plus * your_hand[-1]}\n")
                elif dealer_hand[1] == your_hand[1]:
                    balance += bet + pair_plus * your_hand[-1]
                    special_display("TIE")
                    special_display(f"\n{balance}\n+{bet + pair_plus * your_hand}\n")
            
    
    # your_hand = value(hand)
    # dealer_hand = value(dealer)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if your_hand == 21 and dealer_hand != 21:
    #     balance = int(balance + bet * 2.5)
    #     special_display(f"The dealer has {dealer[0]} and {dealer[1]}\n")
    #     special_display("BLACKJACK\n")
    #     special_display(f"{balance}\n+{int(bet*2.5)}\n")
    #     continue
    # if your_hand == 21 and dealer_hand == 21:
    #     balance = balance + bet
    #     special_display(f"The dealer has {dealer[0]} and {dealer[1]}\n")
    #     special_display(f"{balance}\n+{bet}\n")
    #     continue
    
    # while True:
    #     move = input("Hit or stand? ").capitalize()
    #     if move != "Hit" and move != "Stand":
    #         while True:
    #             move = input("Invalid input bub, type 'Hit' or 'Stand' ").capitalize()
    #             if move == "Hit" or move == "Stand":
    #                 break
                
    #     if move == "Hit":
    #         while True:
    #             card = f"{cards[random.randint(1,13)]} of {random.choice(suite)}"
    #             if not(card in cards_played):
    #                 cards_played.append(card)
    #                 hand.append(card)
    #                 print("You now have", end = " ")
    #                 for each_card in hand:
    #                     print(":", end = " ")
    #                     print(each_card, end = " ")
    #                 your_hand = value(hand)
    #                 print()
    #                 break
                
    #         if your_hand > 21:
    #             special_display("\n\nBUST")
    #             break
    #     elif move == "Stand":
    #         special_display(f"\nThe dealer has {dealer[0]} and {dealer[1]}\n")
    #         # if your_hand < dealer_hand:
    #         #     special_display(f"\n\nYour {your_hand} against {dealer_hand} You lose!")
    #         #     break
    #         if dealer_hand >= 16 and your_hand > dealer_hand:
    #             balance = balance + bet * 2
    #             special_display(f"\n\nYour {your_hand} against {dealer_hand} You Win!\n")
    #             special_display(f"{balance}\n+{bet*2}\n")
    #             break
    #         if your_hand == dealer_hand:
    #             balance = balance + bet
    #             special_display("\n\nTie!")
    #             special_display(f"\n{balance}\n+{bet}\n")
    #             break
    #         while dealer_hand < 17:
    #             special_display("The dealer hits\n")
    #             while True:
    #                 card = f"{cards[random.randint(1,13)]} of {random.choice(suite)}"
    #                 if not(card in cards_played):
    #                     cards_played.append(card)
    #                     dealer.append(card)
    #                     print("The dealer now has", end = " ")
    #                     for each_card in dealer:
    #                         print(":", end = " ")
    #                         print(each_card, end = " ")
    #                     dealer_hand = value(dealer)
    #                     print()
    #                     break
    #         if dealer_hand > 21:
    #             balance = balance + bet * 2
    #             special_display("\n\nDealer BUST")
    #             special_display("You Win!\n")
    #             special_display(f"{balance}\n+{bet*2}\n")
    #             break
    #         if your_hand < dealer_hand:
    #             special_display(f"\n\nYour {your_hand} against {dealer_hand} You lose!")
    #             break
    #         if dealer_hand >= 16 and your_hand > dealer_hand:
    #             balance = balance + bet * 2
    #             special_display(f"\n\nYour {your_hand} against {dealer_hand} You Win!\n")
    #             special_display(f"{balance}\n+{bet*2}\n")
    #             break
    #         if your_hand == dealer_hand:
    #             balance = balance + bet
    #             special_display("\n\nTie!")
    #             special_display(f"\n{balance}\n+{bet}\n")
    #             break
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    