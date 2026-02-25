from ex0.Card import Card
import random

class Deck():
    cards = []
    cards_types = {'spell': 0, 'creature': 0, 'artifact': 0}
    def add_card(self, card: Card) -> None:
        self.cards_types[card.card_type] += 1
        self.cards.append(card)
    def remove_card(self, card_name: str) -> bool:
        cards.remove(card_name)
        return True
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    def draw_card(self) -> Card:
        return self.cards.pop(0)
    def get_deck_stats(self) -> dict:
        costs_total = 0
        avg_costs = 0
        for card in self.cards:
            costs_total += card.cost
        avg_costs = costs_total / len(self.cards)
        return {'total_cards': sum(self.cards_types.values()), 'creatures': self.cards_types['creature'], 'spells': self.cards_types['spell'], 'artifacts': self.cards_types['artifact'], 'avg_cost': avg_costs}
