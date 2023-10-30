# Contains utility functions which are used throughout the code base.


from collections import defaultdict
from itertools import permutations


def convert_pairwise_to_ranking(pairwise_preferences):
    # Format of pairwise will be a list of lists of lists (oof)
    # ["A", "B"] means A is preferred to B
    # for a single voter, this might look like:
    # [["A", "B"], ["B", "C"]]
    new_ranking = []
    for each in pairwise_preferences:
        ranking = single_ranking(each)
        new_ranking.append(ranking)

    return new_ranking


def single_ranking(pairwise_preferences):
    pairwise_win_counts = defaultdict(int)

    # Iterate through the pairwise preferences and count wins
    for pref in pairwise_preferences:
        for i, candidate1 in enumerate(pref):
            for j, candidate2 in enumerate(pref):
                if i < j:
                    pairwise_win_counts[(candidate1, candidate2)] += 1

    candidates = set(candidate for pref in pairwise_preferences for candidate in pref)
    all_rankings = list(permutations(candidates))

    # Calculate the strength of each ranking
    ranking_strengths = {}
    for ranking in all_rankings:
        strength = 0
        for i, candidate1 in enumerate(ranking):
            for j, candidate2 in enumerate(ranking):
                if i < j:
                    strength += pairwise_win_counts.get((candidate1, candidate2), 0)
        ranking_strengths[ranking] = strength

    # Find the ranking with the highest strength
    best_ranking = max(all_rankings, key=lambda r: ranking_strengths[r])

    return list(best_ranking)


def ranking_to_pairwise(ranking_preferences):
    pairwise_list = []

    for ranking in ranking_preferences:
        pairwise_ranking = []
        for i in range(len(ranking)):
            for j in range(i + 1, len(ranking)):
                pairwise_ranking.append([ranking[i], ranking[j]])
        pairwise_list.append(pairwise_ranking)

    return pairwise_list
