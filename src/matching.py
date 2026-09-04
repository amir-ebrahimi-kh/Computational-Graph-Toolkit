from typing import Dict, List, TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')

def stable_matching(
    group1_prefs: Dict[T1, List[T2]],
    group2_prefs: Dict[T2, List[T1]]
) -> Dict[T1, T2]:
    """Computes a stable matching between two groups using the Gale-Shapley algorithm.

    This implementation assumes that group1 proposes to group2.

    Args:
        group1_prefs: A dictionary mapping members of the proposing group to a list
                      of their preferences from the other group, in descending order.
        group2_prefs: A dictionary mapping members of the receiving group to a list
                      of their preferences from the proposing group, in descending order.

    Returns:
        A dictionary mapping members of the proposing group (group1) to their
        matched partners from the receiving group (group2).
    """
    # Track the current matches for group2 (receiving group).
    # Keys are group2 members, values are their matched group1 members.
    matches: Dict[T2, T1] = {}

    # Track free members of group1
    free_group1 = list(group1_prefs.keys())

    # Track the next proposal index for each member of group1
    proposals_count: Dict[T1, int] = {g1: 0 for g1 in group1_prefs}

    # Pre-compute rankings for group2 to allow O(1) comparison
    # Group 2 member -> {Group 1 member -> Rank (lower is better)}
    group2_rankings: Dict[T2, Dict[T1, int]] = {}
    for g2, prefs in group2_prefs.items():
        group2_rankings[g2] = {g1: rank for rank, g1 in enumerate(prefs)}

    while free_group1:
        suitor = free_group1.pop(0)

        # Ensure the suitor hasn't exhausted all their preferences
        if proposals_count[suitor] >= len(group1_prefs[suitor]):
            continue

        # The suitor proposes to their next preferred choice
        reviewer = group1_prefs[suitor][proposals_count[suitor]]
        proposals_count[suitor] += 1

        if reviewer not in matches:
            # Reviewer is free, so they match
            matches[reviewer] = suitor
        else:
            # Reviewer is currently matched
            current_partner = matches[reviewer]

            # Check if reviewer prefers the new suitor over the current partner
            # Using the pre-computed rankings
            if group2_rankings[reviewer][suitor] < group2_rankings[reviewer][current_partner]:
                # Reviewer prefers new suitor, break old match and create new one
                matches[reviewer] = suitor
                free_group1.append(current_partner)
            else:
                # Reviewer prefers current partner, suitor remains free
                free_group1.append(suitor)

    # Return the matches as a mapping from group1 to group2
    return {suitor: reviewer for reviewer, suitor in matches.items()}
