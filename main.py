#!/usr/bin/python3
from Deck import *
from functools import reduce

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.positions = [False for _ in range(len(cards))]

    def show_cards(self):
        return [c.show_card() for c in self.cards]

    def pick_card(self, deck):
        return deck.get_card()

    def check_end(self):
        return all(self.positions)

class Game:
    def __init__(self):
        self.players = {}
        self.deck = Deck()
        self.rules = self.get_rules()
        self.pass_cards = ['J', 'Q', 'K']

    def add_player(self, name, num_cards):
        self.players[name] = Player(name, self.deck.get_cards(num_cards))

    def show_player_by_name(self, name):
        return '{}: {}'.format(self.players[name].name, self.players[name].show_cards())

    def get_rules(self):
        return { 'A' : 0, 2 : 1, 3 : 2, 4 : 3, 5 : 4, 6 : 5, 7 : 6, 8 : 7, 9 : 8, 10 : 9 }

    def evaluate(self, picked_card, player):
        if picked_card.number in self.pass_cards:
            print(player.show_cards())
            print(player.positions)
            return
        index = self.rules[picked_card.number]
        if not player.positions[index]:
            player.positions[index] = True
            new_card = player.cards[index]
            player.cards[index] = picked_card
            print(new_card.show_card())
            self.evaluate(new_card, player)
        else:
            print(player.show_cards())
            print(player.positions)
            return

    def run_turn(self, player_name):
        current_player = self.players[player_name]
        print(current_player.show_cards())
        pick = current_player.pick_card(self.deck)
        print(pick.show_card())
        self.evaluate(pick, current_player)
        
        

def main():
    Soap = Game()
    Soap.add_player('Arthur', 10)
    Soap.add_player('Gabi', 10)
    Soap.run_turn('Arthur')
    print(Soap.players['Arthur'].check_end())
    # print(Soap.show_player_by_name('Arthur'))
    # print(Soap.show_player_by_name('Gabi'))
    # D = Deck()
    # A = Player('Arthur', D.get_cards(10))
    # G = Player('Gabi', D.get_cards(10))
    # print('{}: {}'.format(A.name, A.show_cards()))
    # print('{}: {}'.format(G.name, G.show_cards()))

if __name__ == "__main__":
    main()