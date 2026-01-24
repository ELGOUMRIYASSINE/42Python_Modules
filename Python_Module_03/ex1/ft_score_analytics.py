"""
Player Score Analytics Script.

This script processes a list of scores passed via command-line arguments and
calculates player statistics.
It displays the total players, total score, average score, high score,
low score, and score range.

Usage:
    python3 ft_score_analytics.py <score1> <score2> ...

- If no scores are provided, it shows a usage message.
- Invalid scores (non-integer values) will produce an error message.

Example:
    python3 ft_score_analytics.py 85 90 78
    Output:
        Total players: 3
        Total score: 253
        Average score: 84.33
"""

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    list_len = len(sys.argv)
    if (list_len < 2):
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        scores = []
        i = 0
        try:
            while i < list_len - 1:
                scores.append(int(sys.argv[i + 1]))
                i += 1
            print(f"Scores processed: {scores}")
            print(f"Total players: {list_len - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / (list_len - 1):.2f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError:
            print(f"Score Error: {sys.argv[i + 1]} Invalid Value!")
