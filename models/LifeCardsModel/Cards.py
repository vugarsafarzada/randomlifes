from assets.helper_methods import shuffle_array, select_random_items, randomItemFromList


class Cards:
    def __init__(self):
        self._ranks_chars = ['A', 'K', 'Q', 'J']

        self.suits_dict = {
            'spades': '♠️',
            'diamonds': '♦️',
            'clubs': '♣️',
            'hearts': '♥️',
        }

        self._suits = [
            self.suits_dict['clubs'],
            self.suits_dict['diamonds'],
            self.suits_dict['hearts'],
            self.suits_dict['spades']
        ]

    @property
    def order_for_36(self):
        ranks_for_36 = []
        order_for_36 = []

        for c in range(6, 11):
            ranks_for_36.append(c)
            ranks_for_36 = list(set(ranks_for_36).union(self._ranks_chars))

        for suit_value in self._suits:
            for order_value in ranks_for_36:
                order_for_36.append([order_value, suit_value])

        return order_for_36

    @property
    def order_for_52(self):
        ranks_for_52 = []
        order_for_52 = []

        for c in range(2, 11):
            ranks_for_52.append(c)
            ranks_for_52 = list(set(ranks_for_52).union(self._ranks_chars))

        for suit_value in self._suits:
            for order_value in ranks_for_52:
                order_for_52.append([order_value, suit_value])

        return order_for_52

    @staticmethod
    def cards_by_suit(suit, target_order=[]):
        result = []
        for card in target_order:
            if suit == card[1]:
                result.append(card)

        return result

    @staticmethod
    def cards_by_rank(rank, target_order=[]):
        result = []
        for card in target_order:
            if rank == card[0]:
                result.append(card)

        return result

    @staticmethod
    def shuffle_cards(array):
        return shuffle_array(array)

cards = Cards()

#print(cards.order_for_36)
#print(cards.cards_by_suit(cards.suits['clubs'], target_order=cards.order_for_36))
#print(cards.cards_by_rank('K', target_order=cards.order_for_36))
#print(cards.shuffle_cards(cards.order_for_36))

order = cards.order_for_36
shuffled_cards = cards.shuffle_cards(order)

hand = select_random_items(shuffled_cards, 7)
opened = shuffled_cards[-1]

print('Opened card:', opened)
print()
print('Your hand:')
for i in order:
    print(i)

