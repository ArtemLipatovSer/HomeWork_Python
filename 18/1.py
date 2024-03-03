from cards.funcCards import *

print(createDesk())

shuffle(createDesk())

deal(3, 5, mixDeck)

print(f'Карты игроков - {arrPlayers},\n'
      f'Оставшаяся колода - {mixDeck}')
