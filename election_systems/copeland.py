# Given a list of lists, where each list represents a voter's preference ordering over
# a set of candidates, i.e., ['B', 'A', 'C'] means B is preferred to A, and A is preferred
# to C, runs the voter preferences on Copeland method.

def copeland(prefs):
    candidate_scores = {}

    for voter_pref in prefs:
        for i, candidate in enumerate(voter_pref):
            if candidate not in candidate_scores:
                candidate_scores[candidate] = 0

            for other_candidate in voter_pref[i + 1:]:
                candidate_scores[candidate] += compare_candidates(candidate, other_candidate, prefs)

    sorted_result = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)
    results_list = []
    for each in sorted_result:
        results_list.append(each[0])

    return results_list


def compare_candidates(candidate1, candidate2, prefs):
    candidate1_wins = 0
    candidate2_wins = 0

    for voter_pref in prefs:
        if candidate1 in voter_pref and candidate2 in voter_pref:
            if voter_pref.index(candidate1) < voter_pref.index(candidate2):
                candidate1_wins += 1
            else:
                candidate2_wins += 1

    if candidate1_wins > candidate2_wins:
        return 1
    elif candidate2_wins > candidate1_wins:
        return -1
    else:
        return 0


