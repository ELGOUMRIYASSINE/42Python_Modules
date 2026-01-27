data = {
    'alice': [
        'first_blood',
        'speed_runner',
        'pixel_perfect',
        'first_blood',
        'pixel_perfect',
        'first_blood',
    ],
    'bob': [
        'first_blood',
        'level_master',
        'boss_hunter',
        'treasure_seeker',
        'level_master',
        'level_master',
    ],
    'charlie': [
        'treasure_seeker',
        'boss_hunter',
        'combo_king',
        'first_blood',
        'boss_hunter',
        'first_blood',
        'boss_hunter',
        'first_blood',
    ],
    'diana': [
        'first_blood',
        'combo_king',
        'level_master',
        'treasure_seeker',
        'speed_runner',
        'combo_king',
        'combo_king',
        'level_master',
    ],
    'eve': [
        'level_master',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
    ],
    'frank': [
        'explorer',
        'boss_hunter',
        'first_blood',
        'explorer',
        'first_blood',
        'boss_hunter',
    ],
}


def Tracker(data):
    print("=== Achievement Tracker System ===\n")
    unique_achievements = set()
    all_common = None
    unique = set()
    # all_unique = None
    for player, achivement in data.items():

        # for player, achivement in data.items():
        print(f"Player {player} achievements: {set(achivement)}")

        # for ach in achivement:
        unique_achievements = unique_achievements.union(achivement)

        # for common achievements:
        if (all_common is None):
            all_common = set(achivement)
        else:
            all_common = all_common.intersection(set(achivement))
            unique = unique.union(set(achivement))

    rare = set()
    for achievement in unique_achievements:
        count = 0
        for player in data.values():
            if achievement in player:
                count += 1
        if count == 1:
            rare = rare.union({achievement})

    print()
    print("=== Achievement Analytics ===")

    print(f"All unique achievements unlocked: {unique_achievements}")
    print(f"Total unique achievements unlocked: {len(unique_achievements)}\n")

    print(f"Common to all players: {all_common}")
    print(f"Rare achievements (1 player):  {rare}\n")

    print(f"Alice vs Bob common: "
          f"{set(data['alice']).intersection(set(data['bob']))}")
    print(f"Alice unique: {set(data['alice']).difference(set(data['bob']))}")
    print(f"Bob unique: {set(data['bob']).difference(set(data['alice']))}")


Tracker(data)
