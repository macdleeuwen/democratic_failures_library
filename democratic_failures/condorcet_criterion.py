# Condorcet criterion is the idea that if someone gets over 50% of the vote in every
# head to head election between other candidates, they win the overall election.
import itertools
from election_systems.first_past_the_post import first_past_the_post


def condorcet(prefs, winner):
    list_of_candidates = sorted({rank for voter in prefs for rank in voter})
    possible_pairs = itertools.combinations(list_of_candidates, 2)
    winner_dict = {}
    for pair in possible_pairs:
        pair_winner = pairwise_winner(prefs, pair[0], pair[1])
        if pair_winner not in winner_dict:
            winner_dict[pair_winner] = 1
        else:
            winner_dict[pair_winner] = winner_dict[pair_winner] + 1
    if winner not in winner_dict:
        return False
    elif winner_dict[winner] == (len(list_of_candidates) - 1):
        return True
    else:
        return False


def pairwise_winner(prefs, winner, candidate):
    loc = [winner, candidate]
    new_prefs = []
    for voter in prefs:
        new_prefs.append([value for value in voter if value in loc])

    pairwise_results = first_past_the_post(new_prefs)[0]
    return pairwise_results[0]
