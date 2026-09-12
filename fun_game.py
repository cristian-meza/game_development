
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Sahith Yamani
# Cristian Meza
# Aynur Asan
# Ryan Sperling
# Section: 504
# Assignment: LAB 13
# Date: 11/30/2025

import pygame
import random
from math import pi

pygame.init()
screen = pygame.display.set_mode((760, 935)) 
run = True

card_font = pygame.font.SysFont(None, 15)
text_font = pygame.font.SysFont(None, 20)
rule_text = pygame.font.SysFont(None, 30)
bet_font = pygame.font.SysFont(None, 50)

cards = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "Jack" : 11, "Queen" : 12, "King" : 13, "Ace" : 14}
v_c = {value : card for card, value in cards.items()}
card_number = [x for x in cards]
suite = ["Spades", "Hearts", "Diamonds", "Clubs"]
hands = {"Straight Flush" : 6, "Three of a kind" : 5, "Straight" : 4, "Flush" : 3, "Pair" : 2, "High Card" : 1}
ante_bonus = {"Straight Flush" : 5, "Three of a kind" : 4, "Straight" : 1, "Flush" : 0, "Pair" : 0, "High Card" : 0}
pp_bonus = {"Straight Flush" : 41, "Three of a kind" : 31, "Straight" : 7, "Flush" : 5, "Pair" : 2, "High Card" : 0}

position = {1 : (15, 5), 2 : (35, 5), 3 : (55, 5), 4 : (35, 30), 5 : (15, 55), 6 : (55, 55), 7 : (35, 70), 8 : (15, 85), 9 : (55, 85), 10 : (35, 110), 11 : (15, 135), 12 : (35, 135), 13 : (55, 135), 14 : (15, 70), 15: (55, 70)}

card_pos = [(142.5, 715), (285, 715), (427.5, 715)]
dealer_pos = [(142.5, 55 + 35), (285, 55 + 35), (427.5, 55 + 35)]

#### Graphics Functions ####

def draw_text(text, font, text_col, x, y):
    '''draw_text will take in a string input, font, color, and coordinates to display text'''
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
def draw_chip(amount, bet):
    '''draw_chip will take in the Ante, Play, and Pair Plus bet amounts and display a chip in their respective positions'''
    if bet == "pair plus":
        pygame.draw.circle(screen, (255, 255, 255), (332.5, 405), 40)
        for i in range(12):
            if i % 2 == 0:   
                pygame.draw.arc(screen, (220, 220, 0), pygame.Rect(292.5, 365, 80, 80), 0 + i * pi / 6, pi / 6 + i * pi / 6, 10) 
            else:
                pygame.draw.arc(screen, (0, 0, 0), pygame.Rect(292.5, 365, 80, 80), 0 + i * pi / 6, pi / 6 + i * pi / 6, 10)
        
        if len(amount) == 3:
            draw_text(amount, text_font, (0,0,255), 320, 397)
        else:
            draw_text(amount, text_font, (0,0,255), 315, 397)
    
    elif bet == "ante":
        if int(amount) < 10000:
            pygame.draw.circle(screen, (255, 255, 255), (332.5, 405 + 103), 40)
            for i in range(12):
                if i % 2 == 0:   
                    pygame.draw.arc(screen, (220, 220, 0), pygame.Rect(292.5, 365 + 103, 80, 80), 0 + i * pi / 6, pi / 6 + i * pi / 6, 10) 
                else:
                    pygame.draw.arc(screen, (0, 0, 0), pygame.Rect(292.5, 365 + 103, 80, 80), 0 + i * pi / 6, pi / 6 + i * pi / 6, 10)
            
            
            draw_text(amount, text_font, (0,0, 255), 315, 397 + 103)
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(260, 365 + 103, 145, 80))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 365 + 103, 145, 80), 13)
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(284 + 1/6, 468, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(320 + 5/12, 468, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(356 + 2/3, 468, 24 + 1/6, 8))
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(284 + 1/6, 540, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(320 + 5/12, 540, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(356 + 2/3, 540, 24 + 1/6, 8))
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(260, 484, 8, 16)) 
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(260, 516, 8, 16)) 
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(397, 484, 8, 16)) 
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(397, 516, 8, 16)) 
            
            
            draw_text(amount, pygame.font.SysFont(None, 55), (0,0,255), 277, 490)
            
    elif bet == "play":
        if int(amount) < 10000:
            pygame.draw.circle(screen, (255, 255, 255), (332.5, 405 + 217), 40)
            for i in range(12):
                if i % 2 == 0:   
                    pygame.draw.arc(screen, (220, 220, 0), pygame.Rect(292.5, 365 + 217, 80, 80), 0 + i * pi / 6, pi / 6 + i * pi / 6, 10) 
                else:
                    pygame.draw.arc(screen, (0, 0, 0), pygame.Rect(292.5, 365 + 217, 80, 80), 0 + i * pi / 6, pi / 6 + i * pi / 6, 10)
            
            
            draw_text(amount, text_font, (0,0,0), 315, 397 + 217)
        else:
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 365 + 217, 145, 80), 10)
        
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(260, 365 + 217, 145, 80))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(260, 365 + 217, 145, 80), 13)
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(284 + 1/6, 468 + 114, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(320 + 5/12, 468 + 114, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(356 + 2/3, 468 + 114, 24 + 1/6, 8))
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(284 + 1/6, 540 + 114, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(320 + 5/12, 540 + 114, 24 + 1/6, 8))
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(356 + 2/3, 540 + 114, 24 + 1/6, 8))
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(260, 484 + 114, 8, 16)) 
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(260, 516 + 114, 8, 16)) 
            
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(397, 484 + 114, 8, 16)) 
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(397, 516 + 114, 8, 16)) 
            
            
            draw_text(amount, pygame.font.SysFont(None, 55), (0,0,255), 277, 490 + 114)




def face(hand, group, position = position[7]):
    '''the function face will display the face cards of each suit in the player hand and dealer positions'''
    if group == "Hearts" or group == "Diamonds":
        color = (255, 0, 0)
    else:
        color = (0, 0, 0)
    x,y = hand
    x1,y1 = position
    xt = x + x1
    yt = y + y1
    if value == "Jack":
        draw_text("J", bet_font, color, xt, yt)
    if value == "Queen":
        draw_text("Q", bet_font, color, xt, yt)
    if value == "King":
        draw_text("K", bet_font, color, xt, yt)
 
def card_label(hand):
    '''This function will assign the suit and number of a card in the labelling position'''
    if group == "Hearts" or group == "Diamonds":
        color = (255, 0, 0)
    else:
        color = (0, 0, 0)
    x,y = hand
    if value != "Ace":    
        draw_text(str(cards[value]), text_font, color, 2 + x, 1 + y)
    else:
        draw_text("A", text_font, color, 5 + x, 5 + y)

def heart(hand, position):
    '''This function draws a heart'''
    x,y = hand
    x1,y1 = position
    xt = x + x1
    yt = y + y1
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((5 + xt, yt, 5, 5)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((15 + xt, yt, 5, 5)))
    
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((0 + xt, 5 + yt, 25, 10)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((5 + xt, 15 + yt, 15, 5)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((10 + xt, 20 + yt, 5, 5)))

def spade(hand, position):
    '''This function draws a spade'''
    x,y = hand
    x1,y1 = position
    xt = x + x1
    yt = y + y1
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((10 + xt, 0 + yt, 5, 5)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((5 + xt, 5 + yt, 15, 5)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0 + xt, 10 + yt, 25, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((10 + xt, 20 + yt, 5, 5)))
    
def diamond(hand, position):
    '''This function draws a diamond'''
    x,y = hand
    x1,y1 = position
    xt = x + x1
    yt = y + y1
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((5 + xt, 5 + yt, 15, 15)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((10 + xt, 0 + yt, 5, 5)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((0 + xt, 10 + yt, 5, 5)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((10 + xt, 20 + yt, 5, 5)))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((20 + xt, 10 + yt, 5, 5)))
    
def club(hand, position):
    '''This function draws a club'''
    x,y = hand
    x1,y1 = position
    xt = x + x1
    yt = y + y1
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((5 + xt, 0 + yt, 15, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0 + xt, 10 + yt, 25, 10)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((0 + xt, 20 + yt, 10, 5)))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((15 + xt, 20 + yt, 10, 5)))    

def display_2(hand, suite_id):
    '''This function displays a 2 of a given suit. This will also be used to display 3 of a given suit as well'''
    positions = [position[2], position[12]]
    if suite_id == "Hearts":
        for i in positions:
            heart(hand, i)
    if suite_id == "Spades":
        for i in positions:
            spade(hand, i)
    if suite_id == "Diamonds":
        for i in positions:
            diamond(hand, i)
    if suite_id == "Clubs":
        for i in positions:
            club(hand, i)

def display_4(hand, suite_id):
    '''This function displays a 4 of a given suit. It will also be used to display a 10, 9, 8, 7, 6, and 5 of a given suit'''
    positions = [position[1], position[3], position[11], position[13]]
    if suite_id == "Hearts":
        for i in positions:
            heart(hand, i)
    if suite_id == "Spades":
        for i in positions:
            spade(hand, i)
    if suite_id == "Diamonds":
        for i in positions:
            diamond(hand, i)
    if suite_id == "Clubs":
        for i in positions:
            club(hand, i)

def display_middle(hand, suite_id):
    '''This function displays an Ace of a given suit. It will also be used to display a 3 and 5 of a given suit'''
    if suite_id == "Hearts":
        heart(hand, position[7])
    if suite_id == "Spades":
        spade(hand, position[7])
    if suite_id == "Diamonds":
        diamond(hand, position[7])
    if suite_id == "Clubs":
        club(hand, position[7])

def display_middle2(hand, suite_id):
    '''This function will display the middle 2 suits of a given card number. It will be used to display a 6 and 7 of a given suit.'''
    positions = [position[14], position[15]]
    if suite_id == "Hearts":
        for i in positions:
            heart(hand, i)
    if suite_id == "Spades":
        for i in positions:
            spade(hand, i)
    if suite_id == "Diamonds":
        for i in positions:
            diamond(hand, i)
    if suite_id == "Clubs":
        for i in positions:
            club(hand, i)

def display_middle4(hand, suite_id):
    '''This function will display the middle 4 suits of a given card number. It will be used to display a 10, 9, and 8 of a given suit'''
    positions = [position[5], position[6], position[8], position[9]]
    if suite_id == "Hearts":
        for i in positions:
            heart(hand, i)
    if suite_id == "Spades":
        for i in positions:
            spade(hand, i)
    if suite_id == "Diamonds":
        for i in positions:
            diamond(hand, i)
    if suite_id == "Clubs":
        for i in positions:
            club(hand, i)
             
#### Calculation Functions ####        

def straight(num_set):
    '''This function checks if a hand is a straight. It will also be used to help determine if a hand is a straight flush as well'''
    num_set.sort()
    if num_set[0] + 1 == num_set[1] and num_set[1] + 1 == num_set[2]:
        return True
    return False

def flush(suite_set):
    '''This function checks if a hand is a flush or a three of a kind. It will also be used to help determine if a hand is a straight flush as well'''
    if suite_set[0] == suite_set[1] and suite_set[1] == suite_set[2]:
        return True
    return False
            
def get_hand(card_set): # takes input of the original card string
    '''This function assigns the exact hand ranking of set of cards'''
    suites = [suit.split()[-1] for suit in card_set]
    card_nums = [cards[card.split()[0]] for card in card_set] # inputs each card value in a list and then sorts it in decending value
    card_nums.sort(reverse = True)
    value = tuple(v_c[card] for card in card_nums) # Tuple for the card names given their value
    if straight(card_nums) and flush(suites):
        return ("Straight Flush", value)
    if flush(card_nums): # CHECKS FOR THREE OF A KIND
        return ("Three of a kind", value)
    if straight(card_nums):
        return ("Straight", value)
    if flush(suites):
        return ("Flush", value)
    if card_nums[0] == card_nums[1] or card_nums[0] == card_nums[2] or card_nums[1] == card_nums[2]:
        return ("Pair", value)
    return ("High Card", value)

def calc(hand, dealer):
    '''This function determines if the player hand wins, loses, or ties against the dealer hand'''
    hand_value = hands[hand[0]]
    dealer_value = hands[dealer[0]]
    hvalues = hand[1] 
    dvalues = dealer[1]
    if dealer_value == 1 and cards[dvalues[0]] < 12:
        return True
    if hand_value > dealer_value:
        return True
    if hand_value < dealer_value:
        return False
    if hand_value != 2:
        for i in range(3):
            if cards[hvalues[i]] > cards[dvalues[i]]:
                return True
            if cards[hvalues[i]] < cards[dvalues[i]]:
                return False
        return "TIE"
    for i in range(2):
        if cards[hvalues[i]] == cards[hvalues[i + 1]]:
            hpair = hvalues[i]
    for i in range(2):
        if cards[dvalues[i]] == cards[dvalues[i + 1]]:
            dpair = dvalues[i]
    if cards[hpair] > cards[dpair]:
        return True
    if cards[hpair] < cards[dpair]:
        return False
    for i in range(3):
        if cards[hpair] != cards[hvalues[i]]:
            hhigh = hvalues[i]
    for i in range(3):
        if cards[dpair] != cards[dvalues[i]]:
            dhigh = dvalues[i]
    if cards[hhigh] > cards[dhigh]:
        return True
    if cards[hhigh] < cards[dhigh]:
        return False
    return "TIE"
            
            
balance = 10000
ante_bet = 1000
bet = 500

#### KEY COUNTERS ####

counter = 0
skipper = 0
ante_display = 0
pp_display = 0
play_display = 0
reveal_display = 0
move_counter = 0

#### GAME STAGE VARIABLES ####

option1 = True
option_counter = 0
select_counter = 0


starter = True

rules = False
one = True
two = False
three = False


ante = False
bet_ante = False

pair_plus = False
bet_pp = False

menu = False

dealing = False

cards_played = []
hand = []
dealer = []

deck = [pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165))]


play = False

played = False
played2 = False

reveal = False

loser = False


try:
    file = open("poker_players.txt","r")
    
    compare = int(file.readline())
    file.close()
except:
    file = open("poker_players.txt", "w")
    compare = 10000
    file.write("10000")
    file.close()

while run:


    screen.fill((0, 100, 0))
    
    if starter:
        
        draw_text(f"HIGH SCORE: {compare}", rule_text, (255,255,255), 275, 330)
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(10, 10, 110, 19))
        draw_text("Hold esc to quit", text_font, (255,255,255), 12, 12)
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(540, 900, 215, 19))
        draw_text("press s to toggle | enter to select", text_font, (255,255,255), 542, 902)
        
        select = pygame.key.get_pressed()
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(75, 175, 617, 120), 10)
        draw_text("Three Card Poker", pygame.font.SysFont(None, 100), (200, 200, 200), 90, 200)
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(300, 540, 152, 53))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(300, 390, 152, 53))
        draw_text("Play", bet_font, (200, 200, 200), 340, 400)
        draw_text("Rules", bet_font, (200, 200, 200), 329.5, 550)
        
        if select[pygame.K_ESCAPE] == True:
            option_counter += 1
            if option_counter > 300:
                run = False
        
        if option1:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(295, 385, 162, 63), 5)
        else:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(295, 535, 162, 63), 5)
        
        if select[pygame.K_s] == True:
            option_counter += 1
            if option_counter > 30:
                if option1:
                    option1 = False
                else:
                    option1 = True
                option_counter = 0
        if select[pygame.K_RETURN] == True:
            select_counter += 1
            if select_counter > 30:
                if option1:
                    ante = True
                    starter = False
                else:
                    rules = True
                select_counter = 0
                
        if rules:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 40, 120, 19))
            draw_text("press  E  to return", text_font, (255,255,255), 92, 42)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 60, 600, 700), 10)
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 70, 580, 680))
            if one:
                draw_text("Welcome to Three Card Poker!", bet_font, (0,0,0), 105, 75)
                draw_text("The objective is to make the best three card", rule_text, (0,0,0), 105, 125)
                draw_text("hand possible and beat the dealer.", rule_text, (0,0,0), 105, 155)
                draw_text("If you run out of chips (displayed on the top right in game)", rule_text, (0,0,0), 105, 190)
                draw_text("you lose!", rule_text, (255,0,0), 105, 220)
                draw_text("Try to beat the", rule_text, (0,0,0), 105, 260)
                draw_text("HIGH SCORE", rule_text, (0,255,0), 250, 260)
                draw_text("Hand Rankings from Best to Worst:", rule_text, (0,0,0), 105, 300 + 40)
                draw_text("Straight Flush: Three consecutive cards of the same suit", rule_text, (0,0,0), 105, 330 + 50)
                draw_text("Three of a kind: Three cards of the same rank", rule_text, (0,0,0), 105, 360 + 50)
                draw_text("Straight: Three consecutive cards of different suits", rule_text, (0,0,0), 105, 390 + 50)
                draw_text("Flush: Three cards of the same suit", rule_text, (0,0,0), 105, 420 + 50)
                draw_text("Pair: Two cards of the same rank", rule_text, (0,0,0), 105, 450 + 50)
                draw_text("High Card: Highest ranked card in hand", rule_text, (0,0,0), 105, 480 + 50)
                draw_text("Press d", rule_text, (0,0,0), 600, 730)
                if select[pygame.K_d] == True:
                    option_counter += 1
                    if option_counter > 30:
                        one = False
                        two = True
                        option_counter = 0
            if two:
                draw_text("Stage 1: Betting", bet_font, (0,0,0), 105, 75)
                draw_text("The first step of Three Card Poker is betting.", rule_text, (0,0,0), 105, 125)
                draw_text("The Ante & Play bets compete against the dealer.", rule_text, (0,0,0), 105, 155)
                draw_text("The pair plus is a side bet that pays based", rule_text, (0,0,0), 105, 195)
                draw_text("on your hand, regardless of the dealer's hand.", rule_text, (0,0,0), 105, 225)
                draw_text("In this stage, place an Ante bet or Pair Plus.", rule_text, (0,0,0), 105, 265)
                draw_text("You can choose between either bet, or use both!", rule_text, (0,0,0), 105, 295)
                draw_text("Press d", rule_text, (0,0,0), 600, 730)
                draw_text("Press a", rule_text, (0,0,0), 105, 730)
                draw_text("Stage 2: Dealing", bet_font, (0,0,0), 105, 330)
                draw_text("After betting, you and the dealer will receive three cards.", rule_text, (0,0,0), 105, 380)
                draw_text("You review your hand and decide one of two moves:", rule_text, (0,0,0), 105, 410)
                draw_text("Play - Place an additional Play bet equal to the Ante bet.", rule_text, (0,0,0), 105, 460)
                draw_text("Fold - If you don't like your hand, forfeit the Ante bet.", rule_text, (0,0,0), 105, 490)
                draw_text("These moves only apply if you placed an Ante bet.", rule_text, (0,0,0), 105, 540)
                if select[pygame.K_d] == True:
                    option_counter += 1
                    if option_counter > 30:
                        three = True
                        two = False
                        option_counter = 0
                if select[pygame.K_a] == True:
                    option_counter += 1
                    if option_counter > 30:
                        one = True
                        two = False
                        option_counter = 0
            if three:
                draw_text("Stage 3: Showdown", bet_font, (0,0,0), 105, 75)
                draw_text("The showdown only occurs if you placed an Ante bet.", rule_text, (0,0,0), 105, 125)
                draw_text("The dealer must have at least a Queen high to play.", rule_text, (0,0,0), 105, 155)
                draw_text("If not, the Ante bet automatically wins even money", rule_text, (0,0,0), 105, 185)
                draw_text("and the your Play bet is returned.", rule_text, (0,0,0), 105, 215)
                draw_text("If so and you win, both Ante and Play bets win even money.", rule_text, (0,0,0), 105, 245)
                draw_text("If your hand ties with the dealer, both Ante and Play", rule_text, (0,0,0), 105, 275)
                draw_text("bets are returned", rule_text, (0,0,0), 105, 305)
                draw_text("The game then continues with a new round of betting.", rule_text, (0,0,0), 105, 335)
                draw_text("Bonus Payouts:", rule_text, (0,0,0), 105, 390 - 30)
                draw_text("These hands pay a bonus regardless of the dealer's hand.", rule_text, (0,0,0), 105, 420 - 30)
                draw_text("Ante Bonus:", rule_text, (0,0,0), 105, 460 - 40)
                draw_text("Straight Flush .................................... 5:1", rule_text, (0,0,0), 105, 490 - 40)
                draw_text("Three of a Kind .................................. 4:1", rule_text, (0,0,0), 105, 520 - 40)
                draw_text("Straight .............................................. 1:1", rule_text, (0,0,0), 105, 550 - 40)
                draw_text("Pair Plus Bonus:", rule_text, (0,0,0), 105, 550)
                draw_text("Straight Flush .................................... 40:1", rule_text, (0,0,0), 105, 580)
                draw_text("Three of a Kind .................................. 30:1", rule_text, (0,0,0), 105, 610)
                draw_text("Straight .............................................. 6:1", rule_text, (0,0,0), 105, 640)
                draw_text("Flush .................................................. 4:1", rule_text, (0,0,0), 105, 670)
                draw_text("Pair ..................................................... 1:1", rule_text, (0,0,0), 105, 700)
                draw_text("Press a", rule_text, (0,0,0), 105, 730)
                if select[pygame.K_a] == True:
                    option_counter += 1
                    if option_counter > 30:
                        three = False
                        two = True
                        option_counter = 0
            if select[pygame.K_e] == True:
                option_counter += 1
                if option_counter > 50:
                    rules = False
                    option_counter = 0
                
                
    
    if not(starter):
        # Card outlines
        
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((112.5, 685, 425, 15)))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((112.5, 685, 15, 225)))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((112.5, 895, 425, 15)))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((537.5, 685, 15, 225)))
        
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((112.5, 685 - 625, 425, 15)))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((112.5, 685 - 625, 15, 225)))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((112.5, 895 - 625, 425, 15)))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((537.5, 685 - 625, 15, 225)))
        
        # Bet outlines
        
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((250, 665, 165, 10)))
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((250, 570, 165, 10)))
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((250, 570, 10, 95)))
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((405, 570, 10, 95)))
        draw_text("PLAY", bet_font, (200, 200, 0), 287, 605)
        
        
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((250, 665 - 115, 165, 10)))
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((250, 570 - 115, 165, 10)))
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((250, 570 - 115, 10, 95)))
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect((405, 570 - 115, 10, 95)))
        draw_text("ANTE", bet_font, (200, 200, 0), 280, 605 - 115)
        
        
        pygame.draw.circle(screen, (200, 200, 0), (332.5, 405), 45, 5)
        draw_text("PAIR", rule_text, (200, 200, 0), 307, 385)
        draw_text("PLUS", rule_text, (200, 200, 0), 305, 405)
        
        # Card Placeholders
        
        for i in range(7):
            pygame.draw.rect(screen, (255, 255, 255), deck[i])
        
        file = open("poker_players.txt","r")
        compare = int(file.readline())
        file.close()
        
        draw_text(f"High Score: {compare}", text_font, (255,255,255), 600, 20)
        draw_text(f"{balance}", rule_text, (255,255,255), 620, 55)
    
    

    
    if ante:
        draw_text("DEALER", bet_font, (0,0,255), 260, 150)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(6, 22, 195, 31))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(195, 913, 540, 19))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(560, 821, 135, 30))
        
        draw_text("Place an Ante bet to receive a hand ", card_font, (255,255,255), 10, 25)
        draw_text("that can be played against the dealer", card_font, (255,255,255), 10, 40)
        
        draw_text("Max bet: TAB | Adjust bet: W & S | Place bet: ENTER | Decline bet: SPACE | Menu: M", text_font, (255,255,255), 200, 915)
        draw_text(f"Ante: {ante_bet}", rule_text, (255,255,255), 570, 825)
        key = pygame.key.get_pressed()
        place = pygame.key.get_pressed()
        if key[pygame.K_s] == True:
            counter += 1
            if ante_bet > 1000 and counter > 100:
                ante_bet -= 500
                draw_text(f"Ante: {ante_bet}", rule_text, (255,255,255), 570, 825)
                counter = 0
                
        if key[pygame.K_w] == True:
            counter += 1
            if (ante_bet < 50000 and ante_bet < balance // 2) and counter > 100:
                ante_bet += 500
                draw_text(f"Ante: {ante_bet}", rule_text, (255,255,255), 570, 825)
                counter = 0
        
        if key[pygame.K_m] == True:
            counter += 1
            if counter > 100:
                menu = True
                counter = 0
        
        if place[pygame.K_RETURN] == True and ante_bet >= 1000:
            counter += 1
            if counter > 70:
                pair_plus = True
                ante = False
                bet_ante = True
                balance -= ante_bet
                counter = 0
                
        if place[pygame.K_TAB] == True:
            counter += 1
            if counter > 70:
                if balance // 2 < 50000:
                    ante_bet = balance // 2
                else:
                    ante_bet = 50000
                draw_text(f"Ante: {ante_bet}", rule_text, (0,0,0), 560, 825)
                counter = 0
                
        if place[pygame.K_SPACE] == True:
            skipper += 1
            if skipper > 70:
                ante_bet = 0
                pair_plus = True
                ante = False
                skipper = 0
                
                
    if bet_ante and ante_display < 2000 and ante_bet != 0 and not(bet_pp):
        draw_text(f"-{ante_bet}", rule_text, (255,0,0), 620, 85)
        ante_display += 1
        
    if ante_bet == (balance + ante_bet) / 2 and pair_plus:
        pair_plus = False
        dealing = True
        
    if pair_plus:
        draw_text("DEALER", bet_font, (0,0,255), 260, 150)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(6, 22, 195, 31))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(195, 913, 540, 19))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(560, 821, 165, 30))
        
        draw_text("Pair Plus is a side bet. This will", card_font, (255,255,255), 10, 25)
        draw_text("win if your hand has a Pair or higher", card_font, (255,255,255), 10, 40)
        
        draw_text(f"Pair Plus: {bet}", rule_text, (255,255,255), 570, 825)
        draw_text("Max bet: TAB | Adjust bet: W & S | Place bet: ENTER | Decline bet: SPACE | Menu: M", text_font, (255,255,255), 200, 915)
        key = pygame.key.get_pressed()
        place = pygame.key.get_pressed()
        decline = pygame.key.get_pressed()
        if key[pygame.K_s] == True:
            counter += 1
            if bet > 500 and counter > 100:
                bet -= 500
                draw_text(f"Pair Plus: {bet}", rule_text, (0,0,0), 560, 825)
                counter = 0
        
        if place[pygame.K_TAB] == True:
            counter += 1
            if counter > 70:
                if (balance - ante_bet) < 5000:
                    bet = balance - ante_bet
                else:
                    bet = 5000
                draw_text(f"Pair Plus: {bet}", rule_text, (0,0,0), 560, 825)
                counter = 0
                
        if place[pygame.K_m] == True:
            counter += 1
            if counter > 70:
                menu = True
                counter = 0
        
        if key[pygame.K_w] == True:
            counter += 1
            if (bet < 5000 and bet < balance - ante_bet) and counter > 100:
                bet += 500
                draw_text(f"Pair Plus: {bet}", rule_text, (0,0,0), 560, 825)
                counter = 0
        
        if place[pygame.K_RETURN] == True:
            counter += 1
            if counter > 100:               
                balance -= bet
                pair_plus = False
                bet_pp = True
                dealing = True
        
        if place[pygame.K_SPACE] == True and bet_ante:
            counter += 1
            if counter > 70:
                bet = 0
                pair_plus = False
                dealing = True

    if bet_pp and pp_display < 2000 and not(played):
        draw_text(f"-{bet}", rule_text, (255,0,0), 620, 85)
        pp_display += 1
        
    if bet_ante:
        draw_chip(str(ante_bet), "ante")
        # draw_chip(str(ante_bet), "play")
    
    if bet_pp:
        draw_chip(str(bet), "pair plus")
    
    if dealing:
        while len(cards_played) < 6:
            card = f"{random.choice(card_number)} of {random.choice(suite)}"
            if not(card in cards_played):
                cards_played.append(card)
                if len(hand) < 3:
                    hand.append(card)
                else:
                    dealer.append(card)         
        deck[1].move_ip(-437.5, 330)
        deck[2].move_ip(-295, 330)
        deck[3].move_ip(-152.5, 330)
    
        deck[4].move_ip(-437.5, -330 + 35)
        deck[5].move_ip(-295, -330 + 35)
        deck[6].move_ip(-152.5, -330 + 35)
        
        if bet_ante:
            play = True
        else:
            reveal = True
            your_hand = get_hand(hand)
        dealing = False
    
    if play and bet_ante:
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(6, 22, 62, 31))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(498, 913, 250, 18))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(556, 821, 190, 30))
        
        your_hand = get_hand(hand)
        dealer_hand = get_hand(dealer)
        if your_hand[0] == "High Card":
            draw_text("You have:", card_font, (255,255,255), 10, 25)
            draw_text(f"{your_hand[1][0]} High", card_font, (255,255,255), 10, 40)
        elif your_hand[0] == "Pair":
            hvalues = your_hand[1]
            for i in range(3):
                for j in range(3):
                    if cards[hvalues[i]] == cards[hvalues[j]] and i != j:
                        hpair = hvalues[i]
            draw_text("You have:", card_font, (255,255,255), 10, 25)
            draw_text(f"{hpair} pair", card_font, (255,255,255), 10, 40)
        else:
            draw_text("You have:", card_font, (255,255,255), 10, 25)
            draw_text(f"{your_hand[0]}", card_font, (255,255,255), 10, 40)
        
        draw_text("Play: ENTER | Fold: SPACE | Menu: M", text_font, (255,255,255), 500, 915)
        draw_text(f"Play Wager: {ante_bet}", rule_text, (255,255,255), 560, 825)
        for pos, i in enumerate(hand):
            value = i.split()[0]
            group = i.split()[-1]
            if value == "Two":
                card_label(card_pos[pos])
                display_2(card_pos[pos], group)
                
            if value == "Three":
                card_label(card_pos[pos])
                display_2(card_pos[pos], group)
                display_middle(card_pos[pos], group)
                
            if value == "Four":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                
            if value == "Five":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle(card_pos[pos], group)
                
            if value == "Six":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle2(card_pos[pos], group)
                
            if value == "Seven":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle2(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], (35, 35))
                if group == "Spades":
                    spade(card_pos[pos], (35, 35))
                if group == "Diamonds":
                    diamond(card_pos[pos], (35, 35))
                if group == "Clubs":
                    club(card_pos[pos], (35, 35))
                    
            if value == "Eight":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle4(card_pos[pos], group)
                
            if value == "Nine":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle4(card_pos[pos], group)   
                if group == "Hearts":
                    heart(card_pos[pos], position[4])
                if group == "Spades":
                    spade(card_pos[pos], position[4])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[4])
                if group == "Clubs":
                    club(card_pos[pos], position[4])
                    
            if value == "Ten":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle4(card_pos[pos], group)   
                if group == "Hearts":
                    heart(card_pos[pos], position[4])
                    heart(card_pos[pos], position[10])
                if group == "Spades":
                    spade(card_pos[pos], position[4])
                    spade(card_pos[pos], position[10])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[4])
                    diamond(card_pos[pos], position[10])
                if group == "Clubs":
                    club(card_pos[pos], position[4])
                    club(card_pos[pos], position[10])
                    
            if value == "Jack":
                face(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], position[1])
                    heart(card_pos[pos], position[13])
                if group == "Spades":
                    spade(card_pos[pos], position[1])
                    spade(card_pos[pos], position[13])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[1])
                    diamond(card_pos[pos], position[13])
                if group == "Clubs":
                    club(card_pos[pos], position[1])
                    club(card_pos[pos], position[13])
                    
            if value == "Queen":
                face(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], position[1])
                    heart(card_pos[pos], position[13])
                if group == "Spades":
                    spade(card_pos[pos], position[1])
                    spade(card_pos[pos], position[13])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[1])
                    diamond(card_pos[pos], position[13])
                if group == "Clubs":
                    club(card_pos[pos], position[1])
                    club(card_pos[pos], position[13]) 
                    
            if value == "King":
                face(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], position[1])
                    heart(card_pos[pos], position[13])
                if group == "Spades":
                    spade(card_pos[pos], position[1])
                    spade(card_pos[pos], position[13])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[1])
                    diamond(card_pos[pos], position[13])
                if group == "Clubs":
                    club(card_pos[pos], position[1])
                    club(card_pos[pos], position[13])  
                    
            if value == "Ace":
                card_label(card_pos[pos])
                display_middle(card_pos[pos], group)
        
        move = pygame.key.get_pressed()
        if move[pygame.K_RETURN] == True:
            move_counter += 1
            if move_counter > 100:
                balance -= ante_bet
                played = True
                played2 = True
                reveal = True
                play = False
        if move[pygame.K_SPACE] == True:
            move_counter += 1
            if move_counter > 100:
                reveal = True
                play = False
        if move[pygame.K_m] == True:
            move_counter += 1
            if move_counter > 100:
                menu = True
                move_counter = 0



    if played == True and play_display < 1000:
        draw_text(f"-{ante_bet}", rule_text, (255,0,0), 620, 85)
        play_display += 1
    
    if played == True:
        draw_chip(str(ante_bet), "play")
        
    if reveal and reveal_display < 4000:
        
        if played2 and reveal_display > 2000:
            if calc(your_hand, dealer_hand) == "TIE":
                balance += ante_bet * 2 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]
            elif calc(your_hand, dealer_hand):
                if hands[dealer_hand[0]] == 1 and cards[dealer_hand[1][0]] < 12:
                    balance += ante_bet * 3 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]
                else:
                    balance += ante_bet * 4 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]
            else:
                balance += ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]
            played2 = False
        
        if reveal_display > 2000 and played:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(6, 22, 200, 31))
            if calc(your_hand, dealer_hand) == "TIE":
                draw_text(f"+{ante_bet * 2 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]}", rule_text, (0,255,0), 620, 85)
                if dealer_hand[0] == "High Card":
                    draw_text(f"The dealer has {dealer_hand[1][0]} High", card_font, (255,255,255), 10, 25)
                    draw_text("TIE!", card_font, (255,255,255), 10, 40)
                elif dealer_hand[0] == "Pair":
                    dvalues = dealer_hand[1]
                    for i in range(3):
                        for j in range(3):
                            if cards[dvalues[i]] == cards[dvalues[j]] and i != j:
                                dpair = dvalues[i]
                    draw_text(f"The dealer has {dpair} pair", card_font, (255,255,255), 10, 25)
                    draw_text("TIE!", card_font, (255,255,255), 10, 40)
                else:
                    draw_text(f"The dealer has {dealer_hand[0]}", card_font, (255,255,255), 10, 25)
                    draw_text("TIE!", card_font, (255,255,255), 10, 40)
            elif calc(your_hand, dealer_hand):
                if hands[dealer_hand[0]] == 1 and cards[dealer_hand[1][0]] < 12:
                    draw_text(f"+{ante_bet * 3 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]}", rule_text, (0,255,0), 620, 85)
                    draw_text("The dealer has less than a Queen high", card_font, (255,255,255), 10, 25)
                    draw_text(f"You win {ante_bet * 3 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]} Chips!", card_font, (255,255,255), 10, 40)
                else:
                    draw_text(f"+{ante_bet * 4 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]}", rule_text, (0,255,0), 620, 85)
                    if your_hand[0] == "High Card":
                        draw_text(f"You have {your_hand[1][0]} High", card_font, (255,255,255), 10, 25)
                        draw_text(f"You win {ante_bet * 4 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]} Chips!", card_font, (255,255,255), 10, 40)
                    elif your_hand[0] == "Pair":
                        hvalues = your_hand[1]
                        for i in range(3):
                            for j in range(3):
                                if cards[hvalues[i]] == cards[hvalues[j]] and i != j:
                                    hpair = hvalues[i]
                        draw_text(f"You have {hpair} pair", card_font, (255,255,255), 10, 25)
                        draw_text(f"You win {ante_bet * 4 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]} Chips!", card_font, (255,255,255), 10, 40)
                    else:
                        draw_text(f"You have {your_hand[0]}", card_font, (255,255,255), 10, 25)
                        draw_text(f"You win {ante_bet * 4 + ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]} Chips!", card_font, (255,255,255), 10, 40)
            else:
                if dealer_hand[0] == "High Card":
                    draw_text(f"The dealer has {dealer_hand[1][0]} High", card_font, (255,255,255), 10, 25)
                    draw_text("You lose", card_font, (255,255,255), 10, 40)
                elif dealer_hand[0] == "Pair":
                    dvalues = dealer_hand[1]
                    for i in range(3):
                        for j in range(3):
                            if cards[dvalues[i]] == cards[dvalues[j]] and i != j:
                                dpair = dvalues[i]
                    draw_text(f"The dealer has {dpair} pair", card_font, (255,255,255), 10, 25)
                    draw_text("You lose", card_font, (255,255,255), 10, 40)
                else:
                    draw_text(f"The dealer has {dealer_hand[0]}", card_font, (255,255,255), 10, 25)
                    draw_text("You lose", card_font, (255,255,255), 10, 40)
                    
                if hands[your_hand[0]] >= 2:
                    draw_text(f"+{ante_bet * ante_bonus[your_hand[0]] + bet * pp_bonus[your_hand[0]]}", rule_text, (0,255,0), 620, 85)
                
        if not(played) and bet_ante:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(6, 22, 170, 31))
            if dealer_hand[0] == "High Card":
                draw_text(f"The dealer has {dealer_hand[1][0]} High", card_font, (255,255,255), 10, 25)
                draw_text("You folded your hand. You lose", card_font, (255,255,255), 10, 40)
            elif dealer_hand[0] == "Pair":
                dvalues = dealer_hand[1]
                for i in range(3):
                    for j in range(3):
                        if cards[dvalues[i]] == cards[dvalues[j]] and i != j:
                            dpair = dvalues[i]
                draw_text(f"The dealer has {dpair} pair", card_font, (255,255,255), 10, 25)
                draw_text("You folded your hand. You lose", card_font, (255,255,255), 10, 40)
            else:
                draw_text(f"The dealer has {dealer_hand[0]}", card_font, (255,255,255), 10, 25)
                draw_text("You folded your hand. You lose", card_font, (255,255,255), 10, 40)
        
        if not(bet_ante) and reveal_display == 10:
            balance += bet * pp_bonus[your_hand[0]]
            
        if not(bet_ante):
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(6, 22, 200, 31))
            if hands[your_hand[0]] >= 2:
                draw_text(f"+{bet * pp_bonus[your_hand[0]]}", rule_text, (0,255,0), 620, 85)
                if your_hand[0] == "Pair":
                    hvalues = your_hand[1]
                    for i in range(3):
                        for j in range(3):
                            if cards[hvalues[i]] == cards[hvalues[j]] and i != j:
                                hpair = hvalues[i]
                    draw_text(f"You have {hpair} pair", card_font, (255,255,255), 10, 25)
                    draw_text(f"You win {bet * pp_bonus[your_hand[0]]} Chips!", card_font, (255,255,255), 10, 40)
                else:
                    draw_text(f"You have {your_hand[0]}", card_font, (255,255,255), 10, 25)
                    draw_text(f"You win {bet * pp_bonus[your_hand[0]]} Chips!", card_font, (255,255,255), 10, 40)
            else:
                draw_text("Your hand is less than", card_font, (255,255,255), 10, 25)
                draw_text("a pair. You lose", card_font, (255,255,255), 10, 40)
        
        for pos, i in enumerate(hand):
            value = i.split()[0]
            group = i.split()[-1]
            if value == "Two":
                card_label(card_pos[pos])
                display_2(card_pos[pos], group)
                
            if value == "Three":
                card_label(card_pos[pos])
                display_2(card_pos[pos], group)
                display_middle(card_pos[pos], group)
                
            if value == "Four":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                
            if value == "Five":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle(card_pos[pos], group)
                
            if value == "Six":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle2(card_pos[pos], group)
                
            if value == "Seven":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle2(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], (35, 35))
                if group == "Spades":
                    spade(card_pos[pos], (35, 35))
                if group == "Diamonds":
                    diamond(card_pos[pos], (35, 35))
                if group == "Clubs":
                    club(card_pos[pos], (35, 35))
                    
            if value == "Eight":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle4(card_pos[pos], group)
                
            if value == "Nine":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle4(card_pos[pos], group)   
                if group == "Hearts":
                    heart(card_pos[pos], position[4])
                if group == "Spades":
                    spade(card_pos[pos], position[4])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[4])
                if group == "Clubs":
                    club(card_pos[pos], position[4])
                    
            if value == "Ten":
                card_label(card_pos[pos])
                display_4(card_pos[pos], group)
                display_middle4(card_pos[pos], group)   
                if group == "Hearts":
                    heart(card_pos[pos], position[4])
                    heart(card_pos[pos], position[10])
                if group == "Spades":
                    spade(card_pos[pos], position[4])
                    spade(card_pos[pos], position[10])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[4])
                    diamond(card_pos[pos], position[10])
                if group == "Clubs":
                    club(card_pos[pos], position[4])
                    club(card_pos[pos], position[10])
                    
            if value == "Jack":
                face(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], position[1])
                    heart(card_pos[pos], position[13])
                if group == "Spades":
                    spade(card_pos[pos], position[1])
                    spade(card_pos[pos], position[13])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[1])
                    diamond(card_pos[pos], position[13])
                if group == "Clubs":
                    club(card_pos[pos], position[1])
                    club(card_pos[pos], position[13])
                    
            if value == "Queen":
                face(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], position[1])
                    heart(card_pos[pos], position[13])
                if group == "Spades":
                    spade(card_pos[pos], position[1])
                    spade(card_pos[pos], position[13])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[1])
                    diamond(card_pos[pos], position[13])
                if group == "Clubs":
                    club(card_pos[pos], position[1])
                    club(card_pos[pos], position[13]) 
                    
            if value == "King":
                face(card_pos[pos], group)
                if group == "Hearts":
                    heart(card_pos[pos], position[1])
                    heart(card_pos[pos], position[13])
                if group == "Spades":
                    spade(card_pos[pos], position[1])
                    spade(card_pos[pos], position[13])
                if group == "Diamonds":
                    diamond(card_pos[pos], position[1])
                    diamond(card_pos[pos], position[13])
                if group == "Clubs":
                    club(card_pos[pos], position[1])
                    club(card_pos[pos], position[13])  
                    
            if value == "Ace":
                card_label(card_pos[pos])
                display_middle(card_pos[pos], group)
        
        tracker = 0
        
        for pos, i in enumerate(dealer):
            tracker += 1
            value = i.split()[0]
            group = i.split()[-1]
            if reveal_display < 1000:
                if value == "Two":
                    card_label(dealer_pos[pos])
                    display_2(dealer_pos[pos], group)
                    
                if value == "Three":
                    card_label(dealer_pos[pos])
                    display_2(dealer_pos[pos], group)
                    display_middle(dealer_pos[pos], group)
                    
                if value == "Four":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    
                if value == "Five":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle(dealer_pos[pos], group)
                    
                if value == "Six":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle2(dealer_pos[pos], group)
                    
                if value == "Seven":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle2(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], (35, 35))
                    if group == "Spades":
                        spade(dealer_pos[pos], (35, 35))
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], (35, 35))
                    if group == "Clubs":
                        club(dealer_pos[pos], (35, 35))
                        
                if value == "Eight":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)
                    
                if value == "Nine":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)   
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[4])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[4])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[4])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[4])
                        
                if value == "Ten":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)   
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[4])
                        heart(dealer_pos[pos], position[10])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[4])
                        spade(dealer_pos[pos], position[10])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[4])
                        diamond(dealer_pos[pos], position[10])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[4])
                        club(dealer_pos[pos], position[10])
                        
                if value == "Jack":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13])
                        
                if value == "Queen":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13]) 
                        
                if value == "King":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13])  
                        
                if value == "Ace":
                    card_label(dealer_pos[pos])
                    display_middle(dealer_pos[pos], group)
                
                if tracker == 1:
                    reveal_display += 1
                    break
                    
            elif reveal_display < 2000:
                if value == "Two":
                    card_label(dealer_pos[pos])
                    display_2(dealer_pos[pos], group)
                    
                if value == "Three":
                    card_label(dealer_pos[pos])
                    display_2(dealer_pos[pos], group)
                    display_middle(dealer_pos[pos], group)
                    
                if value == "Four":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    
                if value == "Five":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle(dealer_pos[pos], group)
                    
                if value == "Six":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle2(dealer_pos[pos], group)
                    
                if value == "Seven":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle2(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], (35, 35))
                    if group == "Spades":
                        spade(dealer_pos[pos], (35, 35))
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], (35, 35))
                    if group == "Clubs":
                        club(dealer_pos[pos], (35, 35))
                        
                if value == "Eight":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)
                    
                if value == "Nine":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)   
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[4])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[4])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[4])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[4])
                        
                if value == "Ten":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)   
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[4])
                        heart(dealer_pos[pos], position[10])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[4])
                        spade(dealer_pos[pos], position[10])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[4])
                        diamond(dealer_pos[pos], position[10])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[4])
                        club(dealer_pos[pos], position[10])
                        
                if value == "Jack":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13])
                        
                if value == "Queen":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13]) 
                        
                if value == "King":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13])  
                        
                if value == "Ace":
                    card_label(dealer_pos[pos])
                    display_middle(dealer_pos[pos], group)
                if tracker == 2:
                    reveal_display += 1
                    break
                    
            elif reveal_display >= 2000:
                if value == "Two":
                    card_label(dealer_pos[pos])
                    display_2(dealer_pos[pos], group)
                    
                if value == "Three":
                    card_label(dealer_pos[pos])
                    display_2(dealer_pos[pos], group)
                    display_middle(dealer_pos[pos], group)
                    
                if value == "Four":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    
                if value == "Five":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle(dealer_pos[pos], group)
                    
                if value == "Six":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle2(dealer_pos[pos], group)
                    
                if value == "Seven":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle2(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], (35, 35))
                    if group == "Spades":
                        spade(dealer_pos[pos], (35, 35))
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], (35, 35))
                    if group == "Clubs":
                        club(dealer_pos[pos], (35, 35))
                        
                if value == "Eight":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)
                    
                if value == "Nine":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)   
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[4])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[4])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[4])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[4])
                        
                if value == "Ten":
                    card_label(dealer_pos[pos])
                    display_4(dealer_pos[pos], group)
                    display_middle4(dealer_pos[pos], group)   
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[4])
                        heart(dealer_pos[pos], position[10])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[4])
                        spade(dealer_pos[pos], position[10])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[4])
                        diamond(dealer_pos[pos], position[10])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[4])
                        club(dealer_pos[pos], position[10])
                        
                if value == "Jack":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13])
                        
                if value == "Queen":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13]) 
                        
                if value == "King":
                    face(dealer_pos[pos], group)
                    if group == "Hearts":
                        heart(dealer_pos[pos], position[1])
                        heart(dealer_pos[pos], position[13])
                    if group == "Spades":
                        spade(dealer_pos[pos], position[1])
                        spade(dealer_pos[pos], position[13])
                    if group == "Diamonds":
                        diamond(dealer_pos[pos], position[1])
                        diamond(dealer_pos[pos], position[13])
                    if group == "Clubs":
                        club(dealer_pos[pos], position[1])
                        club(dealer_pos[pos], position[13])  
                        
                if value == "Ace":
                    card_label(dealer_pos[pos])
                    display_middle(dealer_pos[pos], group)
                    
        reveal_display += 1
    
    if menu:
        select = pygame.key.get_pressed()
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(230, 350, 300, 200), 10)
        pygame.draw.rect(screen, (0,120,0), pygame.Rect(240, 360, 280, 180))
        draw_text("MENU", rule_text, (0,0,0), 350, 370)
        draw_text("E to return", text_font, (0,0,0), 242, 362)
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(280, 400, 200, 30))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(280, 445, 200, 30))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(280, 490, 200, 30))
        draw_text("RULES", text_font, (0,0,0), 360, 410)
        draw_text("RESTART", text_font, (0,0,0), 355, 455)
        draw_text("HOLD ESC TO QUIT", text_font, (0,0,0), 320, 500)
        
        if select[pygame.K_e] == True:
            option_counter += 1
            if option_counter > 50:
                menu = False
                option_counter = 0
        
        if select[pygame.K_ESCAPE] == True:
            option_counter += 1
            if option_counter > 300:
                run = False
        
        if option1:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(275, 395, 210, 40), 5)
        else:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(275, 440, 210, 40), 5)
        
        if select[pygame.K_s] == True:
            option_counter += 1
            if option_counter > 30:
                if option1:
                    option1 = False
                else:
                    option1 = True
                option_counter = 0
        if select[pygame.K_RETURN] == True:
            select_counter += 1
            if select_counter > 30:
                if option1:
                    rules = True
                else:
                    starter = True
                    menu = False
                    balance = 10000
                    reveal_display = 4000
                select_counter = 0
    
        if rules:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 40, 120, 19))
            draw_text("press  E  to return", text_font, (255,255,255), 92, 42)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 60, 600, 700), 10)
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 70, 580, 680))
            if one:
                draw_text("Welcome to Three Card Poker!", bet_font, (0,0,0), 105, 75)
                draw_text("The objective is to make the best three card", rule_text, (0,0,0), 105, 125)
                draw_text("hand possible and beat the dealer.", rule_text, (0,0,0), 105, 155)
                draw_text("If you run out of chips (displayed on the top right in game)", rule_text, (0,0,0), 105, 190)
                draw_text("you lose!", rule_text, (255,0,0), 105, 220)
                draw_text("Try to beat the", rule_text, (0,0,0), 105, 260)
                draw_text("HIGH SCORE", rule_text, (0,255,0), 250, 260)
                draw_text("Hand Rankings from Best to Worst:", rule_text, (0,0,0), 105, 300 + 40)
                draw_text("Straight Flush: Three consecutive cards of the same suit", rule_text, (0,0,0), 105, 330 + 50)
                draw_text("Three of a kind: Three cards of the same rank", rule_text, (0,0,0), 105, 360 + 50)
                draw_text("Straight: Three consecutive cards of different suits", rule_text, (0,0,0), 105, 390 + 50)
                draw_text("Flush: Three cards of the same suit", rule_text, (0,0,0), 105, 420 + 50)
                draw_text("Pair: Two cards of the same rank", rule_text, (0,0,0), 105, 450 + 50)
                draw_text("High Card: Highest ranked card in hand", rule_text, (0,0,0), 105, 480 + 50)
                draw_text("Press d", rule_text, (0,0,0), 600, 730)
                if select[pygame.K_d] == True:
                    option_counter += 1
                    if option_counter > 30:
                        one = False
                        two = True
                        option_counter = 0
            if two:
                draw_text("Stage 1: Betting", bet_font, (0,0,0), 105, 75)
                draw_text("The first step of Three Card Poker is betting.", rule_text, (0,0,0), 105, 125)
                draw_text("The Ante & Play bets compete against the dealer.", rule_text, (0,0,0), 105, 155)
                draw_text("The pair plus is a side bet that pays based", rule_text, (0,0,0), 105, 195)
                draw_text("on your hand, regardless of the dealer's hand.", rule_text, (0,0,0), 105, 225)
                draw_text("In this stage, place an Ante bet or Pair Plus.", rule_text, (0,0,0), 105, 265)
                draw_text("You can choose between either bet, or use both!", rule_text, (0,0,0), 105, 295)
                draw_text("Press d", rule_text, (0,0,0), 600, 730)
                draw_text("Press a", rule_text, (0,0,0), 105, 730)
                draw_text("Stage 2: Dealing", bet_font, (0,0,0), 105, 330)
                draw_text("After betting, you and the dealer will receive three cards.", rule_text, (0,0,0), 105, 380)
                draw_text("You review your hand and decide one of two moves:", rule_text, (0,0,0), 105, 410)
                draw_text("Play - Place an additional Play bet equal to the Ante bet.", rule_text, (0,0,0), 105, 460)
                draw_text("Fold - If you don't like your hand, forfeit the Ante bet.", rule_text, (0,0,0), 105, 490)
                draw_text("These moves only apply if you placed an Ante bet.", rule_text, (0,0,0), 105, 540)
                if select[pygame.K_d] == True:
                    option_counter += 1
                    if option_counter > 30:
                        three = True
                        two = False
                        option_counter = 0
                if select[pygame.K_a] == True:
                    option_counter += 1
                    if option_counter > 30:
                        one = True
                        two = False
                        option_counter = 0
            if three:
                draw_text("Stage 3: Showdown", bet_font, (0,0,0), 105, 75)
                draw_text("The showdown only occurs if you placed an Ante bet.", rule_text, (0,0,0), 105, 125)
                draw_text("The dealer must have at least a Queen high to play.", rule_text, (0,0,0), 105, 155)
                draw_text("If not, the Ante bet automatically wins even money", rule_text, (0,0,0), 105, 185)
                draw_text("and the your Play bet is returned.", rule_text, (0,0,0), 105, 215)
                draw_text("If so and you win, both Ante and Play bets win even money.", rule_text, (0,0,0), 105, 245)
                draw_text("If your hand ties with the dealer, both Ante and Play", rule_text, (0,0,0), 105, 275)
                draw_text("bets are returned", rule_text, (0,0,0), 105, 305)
                draw_text("The game then continues with a new round of betting.", rule_text, (0,0,0), 105, 335)
                draw_text("Bonus Payouts:", rule_text, (0,0,0), 105, 390 - 30)
                draw_text("These hands pay a bonus regardless of the dealer's hand.", rule_text, (0,0,0), 105, 420 - 30)
                draw_text("Ante Bonus:", rule_text, (0,0,0), 105, 460 - 40)
                draw_text("Straight Flush .................................... 5:1", rule_text, (0,0,0), 105, 490 - 40)
                draw_text("Three of a Kind .................................. 4:1", rule_text, (0,0,0), 105, 520 - 40)
                draw_text("Straight .............................................. 1:1", rule_text, (0,0,0), 105, 550 - 40)
                draw_text("Pair Plus Bonus:", rule_text, (0,0,0), 105, 550)
                draw_text("Straight Flush .................................... 40:1", rule_text, (0,0,0), 105, 580)
                draw_text("Three of a Kind .................................. 30:1", rule_text, (0,0,0), 105, 610)
                draw_text("Straight .............................................. 6:1", rule_text, (0,0,0), 105, 640)
                draw_text("Flush .................................................. 4:1", rule_text, (0,0,0), 105, 670)
                draw_text("Pair ..................................................... 1:1", rule_text, (0,0,0), 105, 700)
                draw_text("Press a", rule_text, (0,0,0), 105, 730)
                if select[pygame.K_a] == True:
                    option_counter += 1
                    if option_counter > 30:
                        three = False
                        two = True
                        option_counter = 0
            if select[pygame.K_e] == True:
                option_counter += 1
                if option_counter > 50:
                    rules = False
                    option_counter = 0
    
    if reveal_display == 4000 and balance > 0:
        
        file = open("poker_players.txt","r")
        compare = int(file.readline())
        file.close()
        if balance > compare:
            file = open("poker_players.txt","w")
            file.write(str(balance))
            file.close()
        
        ante = True
        
        if starter:
            ante = False
        
        if ante_bet < 1000:
            ante_bet = 1000
        if bet < 500:
            bet = 500
            
        bet_ante = False

        pair_plus = False
        bet_pp = False

        dealing = False

        cards_played = []
        hand = []
        dealer = []

        deck = [pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165))]


        play = False

        played = False
        played2 = False

        reveal = False
        
        counter = 0
        skipper = 0
        ante_display = 0
        pp_display = 0
        play_display = 0
        reveal_display = 0
        move_counter = 0
        
        if ante_bet * 2 > balance:
            ante_bet = balance // 2
            
            
    
    
    
    if reveal_display == 4000 and balance <= 0:
        loser = True
        
    if loser:
        select = pygame.key.get_pressed()
        
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(230, 350, 300, 200), 10)
        pygame.draw.rect(screen, (0,120,0), pygame.Rect(240, 360, 280, 180))
        draw_text("You Lost", rule_text, (0,0,0), 350, 370)
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(280, 400, 200, 30))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(280, 445, 200, 30))
        pygame.draw.rect(screen, (0,0,255), pygame.Rect(280, 490, 200, 30))
        draw_text("RULES", text_font, (0,0,0), 360, 410)
        draw_text("RESTART", text_font, (0,0,0), 355, 455)
        draw_text("HOLD ESC TO QUIT", text_font, (0,0,0), 320, 500)
        
        if select[pygame.K_ESCAPE] == True:
            option_counter += 1
            if option_counter > 300:
                run = False
        
        if option1:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(275, 395, 210, 40), 5)
        else:
            pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(275, 440, 210, 40), 5)
        
        if select[pygame.K_s] == True:
            option_counter += 1
            if option_counter > 30:
                if option1:
                    option1 = False
                else:
                    option1 = True
                option_counter = 0
        if select[pygame.K_RETURN] == True:
            select_counter += 1
            if select_counter > 30:
                if option1:
                    rules = True
                else:
                    starter = True
                    loser = False
                    balance = 10000
                    bet_ante = False

                    pair_plus = False
                    bet_pp = False

                    dealing = False

                    cards_played = []
                    hand = []
                    dealer = []

                    deck = [pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165)), pygame.Rect((580, 385, 95, 165))]


                    play = False

                    played = False
                    played2 = False

                    reveal = False
                    
                    counter = 0
                    skipper = 0
                    ante_display = 0
                    pp_display = 0
                    play_display = 0
                    reveal_display = 0
                    move_counter = 0
            
                select_counter = 0
    
        if rules:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 40, 120, 19))
            draw_text("press  E  to return", text_font, (255,255,255), 92, 42)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(90, 60, 600, 700), 10)
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(100, 70, 580, 680))
            if one:
                draw_text("Welcome to Three Card Poker!", bet_font, (0,0,0), 105, 75)
                draw_text("The objective is to make the best three card", rule_text, (0,0,0), 105, 125)
                draw_text("hand possible and beat the dealer.", rule_text, (0,0,0), 105, 155)
                draw_text("If you run out of chips (displayed on the top right in game)", rule_text, (0,0,0), 105, 190)
                draw_text("you lose!", rule_text, (255,0,0), 105, 220)
                draw_text("Try to beat the", rule_text, (0,0,0), 105, 260)
                draw_text("HIGH SCORE", rule_text, (0,255,0), 250, 260)
                draw_text("Hand Rankings from Best to Worst:", rule_text, (0,0,0), 105, 300 + 40)
                draw_text("Straight Flush: Three consecutive cards of the same suit", rule_text, (0,0,0), 105, 330 + 50)
                draw_text("Three of a kind: Three cards of the same rank", rule_text, (0,0,0), 105, 360 + 50)
                draw_text("Straight: Three consecutive cards of different suits", rule_text, (0,0,0), 105, 390 + 50)
                draw_text("Flush: Three cards of the same suit", rule_text, (0,0,0), 105, 420 + 50)
                draw_text("Pair: Two cards of the same rank", rule_text, (0,0,0), 105, 450 + 50)
                draw_text("High Card: Highest ranked card in hand", rule_text, (0,0,0), 105, 480 + 50)
                draw_text("Press d", rule_text, (0,0,0), 600, 730)
                if select[pygame.K_d] == True:
                    option_counter += 1
                    if option_counter > 30:
                        one = False
                        two = True
                        option_counter = 0
            if two:
                draw_text("Stage 1: Betting", bet_font, (0,0,0), 105, 75)
                draw_text("The first step of Three Card Poker is betting.", rule_text, (0,0,0), 105, 125)
                draw_text("The Ante & Play bets compete against the dealer.", rule_text, (0,0,0), 105, 155)
                draw_text("The pair plus is a side bet that pays based", rule_text, (0,0,0), 105, 195)
                draw_text("on your hand, regardless of the dealer's hand.", rule_text, (0,0,0), 105, 225)
                draw_text("In this stage, place an Ante bet or Pair Plus.", rule_text, (0,0,0), 105, 265)
                draw_text("You can choose between either bet, or use both!", rule_text, (0,0,0), 105, 295)
                draw_text("Press d", rule_text, (0,0,0), 600, 730)
                draw_text("Press a", rule_text, (0,0,0), 105, 730)
                draw_text("Stage 2: Dealing", bet_font, (0,0,0), 105, 330)
                draw_text("After betting, you and the dealer will receive three cards.", rule_text, (0,0,0), 105, 380)
                draw_text("You review your hand and decide one of two moves:", rule_text, (0,0,0), 105, 410)
                draw_text("Play - Place an additional Play bet equal to the Ante bet.", rule_text, (0,0,0), 105, 460)
                draw_text("Fold - If you don't like your hand, forfeit the Ante bet.", rule_text, (0,0,0), 105, 490)
                draw_text("These moves only apply if you placed an Ante bet.", rule_text, (0,0,0), 105, 540)
                if select[pygame.K_d] == True:
                    option_counter += 1
                    if option_counter > 30:
                        three = True
                        two = False
                        option_counter = 0
                if select[pygame.K_a] == True:
                    option_counter += 1
                    if option_counter > 30:
                        one = True
                        two = False
                        option_counter = 0
            if three:
                draw_text("Stage 3: Showdown", bet_font, (0,0,0), 105, 75)
                draw_text("The showdown only occurs if you placed an Ante bet.", rule_text, (0,0,0), 105, 125)
                draw_text("The dealer must have at least a Queen high to play.", rule_text, (0,0,0), 105, 155)
                draw_text("If not, the Ante bet automatically wins even money", rule_text, (0,0,0), 105, 185)
                draw_text("and the your Play bet is returned.", rule_text, (0,0,0), 105, 215)
                draw_text("If so and you win, both Ante and Play bets win even money.", rule_text, (0,0,0), 105, 245)
                draw_text("If your hand ties with the dealer, both Ante and Play", rule_text, (0,0,0), 105, 275)
                draw_text("bets are returned", rule_text, (0,0,0), 105, 305)
                draw_text("The game then continues with a new round of betting.", rule_text, (0,0,0), 105, 335)
                draw_text("Bonus Payouts:", rule_text, (0,0,0), 105, 390 - 30)
                draw_text("These hands pay a bonus regardless of the dealer's hand.", rule_text, (0,0,0), 105, 420 - 30)
                draw_text("Ante Bonus:", rule_text, (0,0,0), 105, 460 - 40)
                draw_text("Straight Flush .................................... 5:1", rule_text, (0,0,0), 105, 490 - 40)
                draw_text("Three of a Kind .................................. 4:1", rule_text, (0,0,0), 105, 520 - 40)
                draw_text("Straight .............................................. 1:1", rule_text, (0,0,0), 105, 550 - 40)
                draw_text("Pair Plus Bonus:", rule_text, (0,0,0), 105, 550)
                draw_text("Straight Flush .................................... 40:1", rule_text, (0,0,0), 105, 580)
                draw_text("Three of a Kind .................................. 30:1", rule_text, (0,0,0), 105, 610)
                draw_text("Straight .............................................. 6:1", rule_text, (0,0,0), 105, 640)
                draw_text("Flush .................................................. 4:1", rule_text, (0,0,0), 105, 670)
                draw_text("Pair ..................................................... 1:1", rule_text, (0,0,0), 105, 700)
                draw_text("Press a", rule_text, (0,0,0), 105, 730)
                if select[pygame.K_a] == True:
                    option_counter += 1
                    if option_counter > 30:
                        three = False
                        two = True
                        option_counter = 0
            if select[pygame.K_e] == True:
                option_counter += 1
                if option_counter > 50:
                    rules = False
                    option_counter = 0
    
        

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    
pygame.quit()


        
    
         
        