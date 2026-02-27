from typing import Any
from ex4.TournamentCard import TournamentCard

class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches = []
        self.matches_played = 0
    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.lower().replace(" ", "_")
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        result = card1.attack(card2)

        if result["winner"] == card1.name:
            card1.update_wins(1)
            card2.update_losses(1)
            winner = card1_id
            loser = card2_id
        elif result["winner"] == card2.name:
            card2.update_wins(1)
            card1.update_losses(1)
            winner = card2_id
            loser = card1_id
        else:
            winner = "draw"
            loser = "draw"

        self.matches_played += 1

        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": self.cards[winner].rating if winner != "draw" else None,
            "loser_rating": self.cards[loser].rating if loser != "draw" else None,
        }

    def get_leaderboard(self) -> list:
        cards_ratings = [(card_id, card.rating) for card_id, card in self.cards.items()]
        sorted_cards = sorted(cards_ratings, key=lambda x: x[1], reverse=True)
        print(f"1. {sorted_cards[0][0]} - Rating: {sorted_cards[0][1]} (1-0)")
        if len(sorted_cards) > 1:
            print(f"2. {sorted_cards[1][0]} - Rating: {sorted_cards[1][1]} (0-1)")
        return sorted_cards

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": sum(card.rating for card in self.cards.values()) / len(self.cards) if self.cards else 0,
            "platform_status": "active" if self.matches_played > 0 else "inactive"
        }