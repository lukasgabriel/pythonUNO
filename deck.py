# deck.py

from math import floor
from time import time_ns
from random import seed, random
import toml


class Card():
    def __init__(self, c_type: str, c_color: int, c_value: int, c_itera: int, ruleset: dict = toml.load("rules_official.toml")):

        self.deck_ref = ruleset["deck"]
        self.game_ref = ruleset["game"]
        self.points_ref = ruleset["points"]

        self.c_type = c_type
        self.c_color = c_color
        self.c_value = c_value
        self.c_itera = c_itera

        self.assert_ruleset()

        self.desc = self.make_desc()


    def assert_ruleset(self):
        try:
            if self.c_type not in ["wild", "wild4"]:
                assert self.c_color in range(0, self.deck_ref["n_colors"])  # 4 Colors: 0, 1, 2, 3
            else:
                assert self.c_color == 4 # 4 = No Color (For Wildcards and Wildfours)
            assert self.c_type in self.deck_ref["types"]
            assert self.c_value in range(0, 9) or self.c_value in self.points_ref.values()
        except AssertionError:
            print("Invalid ruleset or card.")

    def __str__(self):
        if self.c_type in ["1to9", "zero"]:
            name = self.c_value
        else: 
            name = {"wild": "W", "wild4": "F", "draw2": "D", "reverse": "R", "skip": "S"}[self.c_type]
        color = ["R", "Y", "G", "B", "N"][self.c_color]
        return f"{color}{name}{self.c_itera}"

    def make_desc(self):
        if self.c_type in ["1to9", "zero"]:
            name = ["Zero ", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "][self.c_value]
        else: 
            name = {"wild": "Wild-Card ", "wild4": "Draw-Four Wild-Card ", "draw2": "Draw-Two Card ", "reverse": "Reverse Card ", "skip": "Skip Card "}[self.c_type]
        color = ["Red ", "Yellow ", "Green ", "Blue ", ""][self.c_color]
        return f"{color}{name}{self.c_itera + 1}"

    def __repr__(self):
        return f"Card('{self.c_type}', {self.c_color}, {self.c_value}, {self.c_itera})"


class Deck():
    def __init__(self, d_seed = None, ruleset: dict = toml.load("rules_official.toml")):

        if not d_seed:
            d_seed = time_ns()
        self.d_seed = d_seed
        seed(a=d_seed)

        self.deck_ref = ruleset["deck"]
        self.game_ref = ruleset["game"]
        self.points_ref = ruleset["points"]

        self.deck = []  # Working deck
        self.pile = []  # Discard pile

        self.assert_ruleset()
        self.build()

    def build(self):
        for color in range(self.deck_ref['n_colors']):

            for itera in range(self.deck_ref['n_zeros_per_c']):
                self.deck.append(Card(c_type = "zero", c_color = color, c_value = 0, c_itera = itera))

            for itera in range(self.deck_ref['n_1to9_per_c']):
                for i in range(1, 9):
                    self.deck.append(Card(c_type = "1to9", c_color = color, c_value = i, c_itera = itera))

            for itera in range(self.deck_ref['n_skip_per_c']):
                self.deck.append(Card(c_type = "skip", c_color = color, c_value = self.points_ref["action_card_points"], c_itera = itera))

            for itera in range(self.deck_ref['n_draw2_per_c']):
                self.deck.append(Card(c_type = "draw2", c_color = color, c_value = self.points_ref["action_card_points"], c_itera = itera))

            for itera in range(self.deck_ref['n_reverse_per_c']):
                self.deck.append(Card(c_type = "reverse", c_color = color, c_value = self.points_ref["action_card_points"], c_itera = itera))

        for itera in range(self.deck_ref['n_wild']):
            self.deck.append(Card(c_type = "wild", c_color = 4, c_value = self.points_ref["wild_card_points"], c_itera = itera))

        for itera in range(self.deck_ref['n_wild4']):
            self.deck.append(Card(c_type = "wild4", c_color = 4, c_value = self.points_ref["wild_card_points"], c_itera = itera))

        pass

    def shuffle(self):
        l = len(self.deck)
        while l > 1:
            i = int(floor(random() * l))
            l -= 1
            self.deck[i], self.deck[l] = self.deck[l], self.deck[i]
        return self.deck

    def draw(self):
        pass

    def discard(self):
        pass

    def assert_ruleset(self):
        try:
            assert (
                self.deck_ref["n_cards"]
                == (self.deck_ref["n_colors"] * self.deck_ref["n_cards_per_c"])
                + self.deck_ref["n_wild"]
                + self.deck_ref["n_wild4"]
            )
            assert (
                self.deck_ref["n_cards_per_c"]
                == self.deck_ref["n_zeros_per_c"]
                + (self.deck_ref["n_1to9_per_c"] * 9)
                + self.deck_ref["n_skip_per_c"]
                + self.deck_ref["n_draw2_per_c"]
                + self.deck_ref["n_reverse_per_c"]
            )

            assert self.deck_ref['n_cards'] <= 256

        except AssertionError:
            print("Invalid ruleset.")

    def __str__(self):
        return str([card.__str__() for card in self.deck])

    def __repr__(self):
        return f"Deck(seed='{self.d_seed}')"


""" my_deck = Deck()



#while counter := 0 < deck['n_cards']:
counter = 0
deck = []

for _ in (range(self.deck_ref['n_zeros_per_c'] * self.deck_ref['n_colors'])):
    deck.append({"0":format(counter, '02x')})
    counter += 1


for i in range(0, 9):
    for _ in range(self.deck_ref["n_1to9_per_c"]):
        for c in self.deck_ref["n_colors"]: """
            

deck = Deck("test2")
deck.shuffle()
print(deck)
print(deck.__repr__())

for card in deck.deck:
    print(card.make_desc())
#print(deck.deck_ref)
