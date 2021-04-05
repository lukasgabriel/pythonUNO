# deck.py


import toml

class Card:
    def __init__(self, c_type: str, c_color: int, ruleset: dict = toml.load("rules_official.toml")):
        self.deck_ref = ruleset["deck"]
        self.points_ref = ruleset["points"]

        self.c_type = c_type
        self.c_color = c_color

        try:
            assert self.c_color in range(self.deck_ref["n_colors"]) # 4 Colors: 0, 1, 2, 3.
        except AssertionError:
            print("Invalid ruleset or card.")



class Deck:
    def __init__(self, ruleset: dict = toml.load("rules_official.toml")):
        self.deck_ref = ruleset["deck"]
        self.game_ref = ruleset["game"]

        self.deck = []  # Working deck
        self.pile = []  # Discard pile

        try: 
            self.assert_ruleset()
        except AssertionError:
            print("Invalid ruleset.")

        for i in (range(self.deck_ref['n_zeros_per_c'] * self.deck_ref['n_colors'])):
            deck.append(Card(c_type, c_color, self.ruleset))

        
        pass
    def shuffle(self):
        pass
    def draw(self):
        pass
    def discard(self):
        pass
    def assert_ruleset(self):
        assert (
            self.deck_ref["n_cards"]
            == (self.deck_ref["n_colors"] * self.deck_ref["n_cards_per_c"])
            + self.deck_ref["n_wilds"]
            + self.deck_ref["n_wildfours"]
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
            


print(Deck().deck_ref)
