
game_data = {
    'players': {
        'alice': {'level': 41, 'total_score': 2824, 'achievements_count': 5},
        'bob': {'level': 16, 'total_score': 4657, 'achievements_count': 2},
        'charlie': {'level': 44, 'total_score': 9935, 'achievements_count': 7},
        'diana': {'level': 3, 'total_score': 1488, 'achievements_count': 4},
        'eve': {'level': 33, 'total_score': 1434, 'achievements_count': 7},
        'frank': {'level': 15, 'total_score': 8359, 'achievements_count': 1},
        'grace': {'level': 28, 'total_score': 5621, 'achievements_count': 6},
        'henry': {'level': 50, 'total_score': 11204, 'achievements_count': 9},
        'iris': {'level': 12, 'total_score': 2100, 'achievements_count': 3},
        'jack': {'level': 37, 'total_score': 7890, 'achievements_count': 8}
    },
    'sessions': [
        {'player': 'bob', 'score': 1831, 'mode': 'competitive'},
        {'player': 'alice', 'score': 1981, 'mode': 'ranked'},
        {'player': 'diana', 'score': 2361, 'mode': 'competitive'},
        {'player': 'charlie', 'score': 1196, 'mode': 'casual'},
        {'player': 'eve', 'score': 2985, 'mode': 'casual'},
        {'player': 'frank', 'score': 2754, 'mode': 'casual'},
        {'player': 'grace', 'score': 3120, 'mode': 'ranked'},
        {'player': 'henry', 'score': 4500, 'mode': 'competitive'},
        {'player': 'iris', 'score': 890, 'mode': 'casual'},
        {'player': 'jack', 'score': 3650, 'mode': 'ranked'}
    ],
    'achievements': [
        'first_blood', 'level_master', 'speed_runner',
        'treasure_seeker', 'boss_hunter', 'pixel_perfect',
        'combo_king', 'explorer', 'champion', 'legendary'
    ]
}

print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")

players = game_data['sessions']
high_scores = [
    player['player'] for player in players if player['score'] > 2000
]
scores_doubled = [player['score'] * 2 for player in players]
active_players = [player['player'] * 2 for player in players]
print(f"High scorers (>2000): {high_scores}")
print(f"Scores doubled: {scores_doubled}")
print(f"Active players: {active_players}")

print("=== Dict Comprehension Examples ===")

players = game_data['players']
player_scores = {player:data['total_score'] for player, data in players.items()}
Score categories = {}
print(f"Player scores: {player_scores}")
print(f"Score categories: {player_scores}")
	
