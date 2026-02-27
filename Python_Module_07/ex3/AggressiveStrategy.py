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
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        remaining_mana = 5

        sorted_hand = []
        for card in hand:
            inserted = False
            for i in range(len(sorted_hand)):
                if card.cost < sorted_hand[i].cost:
                    sorted_hand.insert(i, card)
                    inserted = True
                    break
            if not inserted:
                sorted_hand.append(card)

        for card in sorted_hand:
            if card.cost <= remaining_mana:

                cards_played.append(card.name)
                mana_used += card.cost
                remaining_mana -= card.cost

                if hasattr(card, "attack"):
                    damage_dealt += card.attack
                elif hasattr(card, "damage"):
                    damage_dealt += card.damage

        targets = self.prioritize_targets(battlefield)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [t.name for t in targets],
            "damage_dealt": damage_dealt
        }
