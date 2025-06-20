'''
Write a function named missing_card that given a card game returns the (single) missing card name.

The card game will be given as a single string of space-separated cards names.

A card is represented by its color and value, the color being in {"S", "H", "D", "C"} and the value being in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}, for a total of 52 possibilities.

You'll always be given 51 cards, and you have to return the missing one.

https://genepy.org/exercises/the-missing-card
'''


def missing_card(cards):
    color = {"S", "H", "D", "C"}
    numbers = range(2, 11)
    figures = {"J", "Q", "K", "A"}
    mix = []
    for c in color:
        for n in numbers:
            mix.append(c + str(n))
        for f in figures:
            mix.append(c + f)

    for card in mix:
        if card not in cards:
            return card
    return None
