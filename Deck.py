#!/usr/bin/python3
from random import randint, shuffle

class Deck:
    def __init__(self):
        self.suits = ['clubs', 'hearts', 'spades', 'diamonds']
        self.numbers =  ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.cards = self.populate()
        self.play_cards = self.shuffle_cards()
    
    def populate(self):
        return [Card(number, suit) for number in self.numbers for suit in self.suits]

    def shuffle_cards(self):
        ids = self.cards
        shuffle(ids)
        return ids

    def get_card(self):
        return self.play_cards.pop()

    def get_cards(self, quantity):
        return [self.get_card() for i in range(quantity)]

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    
    def show_card(self):
        return '{} of {}'.format(self.number, self.suit)
    

