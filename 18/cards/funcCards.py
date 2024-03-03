import random


def createDesk():
    denomination = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    suit = ('s', 'h', 'd', 'c')
    deck = list()
    for i in denomination:
        for j in suit:
            deck.append(i + j)
    return deck


mixDeck = list()


def shuffle(arr):
    count = 0
    while True:
        elem = arr[random.randint(0, (len(arr) - 1))]
        if elem not in mixDeck:
            mixDeck.append(elem)
            count += 1
            if count == 52:
                break
    print(mixDeck)


arrPlayers = []


def deal(players, cards, deck):
    for i in range(players):
        arrPlayers.append([])
    for i in range(cards):
        for j in range(players):
            arrPlayers[j].append(mixDeck[0])
            mixDeck.remove(mixDeck[0])
    return arrPlayers, mixDeck
