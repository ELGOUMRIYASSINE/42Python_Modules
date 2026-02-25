from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets = []
        for target in available_targets:
            if target.get_combat_stats().get("defense", 0) <= 2:
                targets.append(target)
        if not targets:
            return available_targets
        return targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return {
            "actions": ["play_creature", "attack"],
            "cards_played": [card.name for card in hand if card.card_type == "creature"],
            "targets_prioritized": self.prioritize_targets(battlefield)
        }
