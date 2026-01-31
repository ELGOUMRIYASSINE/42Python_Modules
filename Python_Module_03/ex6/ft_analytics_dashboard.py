"""Game Analytics Dashboard.

Demonstrates list, dict, and set comprehensions for data analysis.
"""

game_data = {
    'players': {
        'alice': {
            'level': 41,
            'total_score': 2824,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements_count': 5,
            'region': 'north',
            'category': 'medium'
        },
        'bob': {
            'level': 16,
            'total_score': 4657,
            'sessions_played': 27,
            'favorite_mode': 'ranked',
            'achievements_count': 2,
            'region': 'east',
            'category': 'medium'
        },
        'charlie': {
            'level': 44,
            'total_score': 9935,
            'sessions_played': 21,
            'favorite_mode': 'ranked',
            'achievements_count': 7,
            'region': 'central',
            'category': 'high'
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4,
            'region': 'north',
            'category': 'low'
        },
        'eve': {
            'level': 33,
            'total_score': 1434,
            'sessions_played': 81,
            'favorite_mode': 'casual',
            'achievements_count': 7,
            'region': 'east',
            'category': 'low'
        },
        'frank': {
            'level': 15,
            'total_score': 8359,
            'sessions_played': 85,
            'favorite_mode': 'competitive',
            'achievements_count': 1,
            'region': 'central',
            'category': 'high'
        }
    },
    'sessions': [
        {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
         'mode': 'competitive', 'completed': False},
        {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
         'mode': 'casual', 'completed': True},
        {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
         'mode': 'competitive', 'completed': False},
        {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
         'mode': 'ranked', 'completed': True},
        {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
         'mode': 'competitive', 'completed': False},
        {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
         'mode': 'casual', 'completed': True},
        {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
         'mode': 'casual', 'completed': True},
        {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
         'mode': 'competitive', 'completed': False},
        {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
         'mode': 'casual', 'completed': False},
        {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
         'mode': 'casual', 'completed': True}
    ],
    'game_modes': ['casual', 'competitive', 'ranked'],
    'achievements': [
        'first_blood', 'level_master', 'speed_runner',
        'treasure_seeker', 'boss_hunter', 'pixel_perfect',
        'combo_king', 'explorer'
    ]
}

print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")

players = game_data['sessions']
high_scores = [
    player['player'] for player in players if player['score'] > 2000
]
scores_doubled = [player['score'] * 2 for player in players]
active_players = set([player['player'] for player in players])
print(f"High scorers (>2000): {high_scores}")
print(f"Scores doubled: {scores_doubled}")
print(f"Active players: {list(active_players)}")

print("\n=== Dict Comprehension Examples ===")

players = game_data['players']
player_scores = {
    player: data['total_score'] for player, data in players.items()
}

categories = {'low': 0, 'high': 0, 'medium': 0}
for data in players.values():
    categories[data['category']] += 1
achievement_counts = {
    player: data['achievements_count'] for player, data in players.items()
}
print(f"Player scores: {player_scores}")
print(f"Score categories: {categories}")
print(f"Achievement counts: {achievement_counts}")

print("\n=== Set Comprehension Examples ===")

unique_players = {player for player in players}
unique_achievements = {achiev for achiev in game_data['achievements']}
active_regions = {region['region'] for player, region in players.items()}
print(f"Unique players: {unique_players}")
print(f"Unique achievements:  {unique_achievements}")
print(f"Active regions:  {active_regions}")

print("\n=== Combined Analysis ===")

scores = [data['total_score'] for player, data in players.items()]
average = sum(scores) / len(unique_players)
max_score = max(scores)
top = {
    player: players[player] for player, data in players.items()
    if data['total_score'] == max_score
}
print(f"Total players: {len(unique_players)}")
print(f"Total unique achievements: {len(unique_achievements)}")
print(f"Average score: {average:.1f}")
for player, data in top.items():
    print(f"Top performer:  {player} ({data['total_score']} points, "
          f"{data['achievements_count']} achievements)")
