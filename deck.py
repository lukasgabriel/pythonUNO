# deck.py

import toml


deck = toml.load("rules_official.toml")["deck"]

assert (
    deck["n_cards"]
    == (deck["n_colors"] * deck["n_cards_per_c"])
    + deck["n_wilds"]
    + deck["n_wildfours"]
)
assert (
    deck["n_cards_per_c"]
    == deck["n_zeros_per_c"]
    + (deck["n_1to9_per_c"] * 9)
    + deck["n_skip_per_c"]
    + deck["n_draw2_per_c"]
    + deck["n_reverse_per_c"]
)

