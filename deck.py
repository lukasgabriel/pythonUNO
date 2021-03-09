# deck.py

import toml


deck_ref = toml.load("rules_official.toml")["deck"]

assert (
    deck_ref["n_cards"]
    == (deck_ref["n_colors"] * deck_ref["n_cards_per_c"])
    + deck_ref["n_wilds"]
    + deck_ref["n_wildfours"]
)
assert (
    deck_ref["n_cards_per_c"]
    == deck_ref["n_zeros_per_c"]
    + (deck_ref["n_1to9_per_c"] * 9)
    + deck_ref["n_skip_per_c"]
    + deck_ref["n_draw2_per_c"]
    + deck_ref["n_reverse_per_c"]
)

assert deck_ref['n_cards'] <= 256

#while counter := 0 < deck['n_cards']:
counter = 0
deck = []

for _ in (range(deck_ref['n_zeros_per_c'] * deck_ref['n_colors'])):
    deck.append({"0":format(counter, '02x')})
    counter += 1
for i in range(0, 9):
    for _ in range(deck_ref["n_1to9_per_c"]):
        for c in deck_ref["n_colors"]:
            

print(deck)
