import typing
from Card import Card

class CreatureCard(Card):
    card_type = "creature"
    def __init__(self, name, cost, rarity, attack, health):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict):
        result = {'card_played': self.name, 'mana_used': self.cost, 'effect': game_state['effect']}
        return result

    def get_card_info(self):
        base_info = super().get_card_info()
        base_info['Attack'] = self.attack
        base_info['Health'] = self.health
        return base_info
    
    def attack_target(self, target):
        result = {'attacker': self.name, 'target': target.name, 'damage_dealt': self.attack, 'combat_resolved': True}
        return result