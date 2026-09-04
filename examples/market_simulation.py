import sys
import os

# Add the root directory to the Python path to import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.matching import stable_matching

def main() -> None:
    """Runs a market simulation using the Gale-Shapley Stable Marriage Algorithm.

    This simulation matches a group of 4 Workers with a group of 4 Firms
    based on their ranked preferences for each other.
    """
    # 4 Workers ranking 4 Firms
    workers_prefs = {
        'Worker 1': ['Firm A', 'Firm B', 'Firm C', 'Firm D'],
        'Worker 2': ['Firm B', 'Firm A', 'Firm D', 'Firm C'],
        'Worker 3': ['Firm A', 'Firm C', 'Firm B', 'Firm D'],
        'Worker 4': ['Firm C', 'Firm D', 'Firm A', 'Firm B']
    }

    # 4 Firms ranking 4 Workers
    firms_prefs = {
        'Firm A': ['Worker 3', 'Worker 1', 'Worker 2', 'Worker 4'],
        'Firm B': ['Worker 2', 'Worker 1', 'Worker 4', 'Worker 3'],
        'Firm C': ['Worker 1', 'Worker 3', 'Worker 4', 'Worker 2'],
        'Firm D': ['Worker 4', 'Worker 2', 'Worker 1', 'Worker 3']
    }

    print("Market Simulation: Stable Matching")
    print("-" * 35)
    print("Computing stable matches between Workers and Firms...")

    matches = stable_matching(workers_prefs, firms_prefs)

    print("\nFinal Stable Pairings:")
    print("-" * 22)
    for worker, firm in sorted(matches.items()):
        print(f"{worker} -> {firm}")

if __name__ == "__main__":
    main()
