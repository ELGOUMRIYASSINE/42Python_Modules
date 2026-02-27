import random
from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    BASE_RATING = 1000

    def __init__(self, name, cost, rarity, attack, health):
            super().__init__(name, cost, rarity)
            self.attack_power = attack
            self.health = health
            self.wins = 0
            self.losses = 0
            self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name}

    def attack(self, target) -> dict:
        if self.attack_power > target.attack_power:
            return {"winner": self.name}
        elif self.attack_power < target.attack_power:
            return {"winner": target.name}
        else:
            return {"winner": "draw"}
    
    def defend(self, incoming_attack: int) -> bool:
        damage_taken = max(0, incoming_attack - self.health)
        self.health -= damage_taken
        return self.health > 0
    
    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        return 1200 + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating = self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating = self.calculate_rating()

    def get_rank_info(self) -> dict:
        print(f"{self.name} (ID: {self.name.lower().replace(' ', '_')})\n")
        print("- Interfaces: Card, Combatable, Rankable")
        print("- Rating: " + str(self.rating))
        print("- Record: " + str(self.wins) + "-" + str(self.losses))
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
