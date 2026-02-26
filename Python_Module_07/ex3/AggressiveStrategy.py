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

        for card in hand:
            if card.card_type == "Creature":
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.attack  # creature attack damage

            elif card.card_type == "Spell":
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += 3  # simple fixed spell damage

            # Ignore artifacts in aggressive strategy
            elif card.card_type == "Artifact":
                continue

        targets = self.prioritize_targets(battlefield)

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [target.name for target in targets],
            "damage_dealt": damage_dealt
        }
