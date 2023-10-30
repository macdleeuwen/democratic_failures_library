# Monotonicity refers to an election system guaranteeing that being ranked higher does not reduce
# your chance of winning, and being ranked lower does not increase your chance of winning.
# Much of this code is very specific to monotonicity or non-monotonicity in the context of
# IRV, or instant runoff voting. That is because the only election system in this library which
# results in non-monotonicity is IRV. Runoff voting (not to be confused with instant runoff!)
# is the only other system of which I am aware that also theoretically violates this criterion.
# Perhaps in the future I'll add that!!

# HUGE thank you to this: http://www.mcdougall.org.uk/VM/ISSUE5/P1.HTM
# Which saved my life when writing this code :)
# This has the limitation of only working when there are 3 candidates. I am hoping to,
# in the future, be able to come up with a more general criteria for when monotonicity
# is violated. For the time being, this code uses a brute force approach if there are
# more than 3 candidates. Very computationally demanding if there are tons of preferences,
# as there are likely to be in real life, so it is not ideal, nor permanent.

# Dr. C Allard gives us the following:

# Where a is the proportion of votes credited to A (in the first round)
# b is the proportion of votes credited to B (in the first round)
# c is the proportion of votes credited to C (in the first round)
# Tij = the proportion of i's votes which transfer to j if i is eliminated
# alpha = TCB - TCA
# beta = TBC - TBA

# An election is non-monotonic iff :
# - b > c
# - a < b + alpha*c
# - a > max{(2b - c) and ((2 + beta)b - c)

# Thanks also to https://rangevoting.org/Monotone.html who gave me some great examples of
# non-monotonic elections, which are included liberally in the tests for this function!

from election_systems.first_past_the_post import first_past_the_post
from election_systems.ranked_choice import ranked_choice
from collections import defaultdict
import copy


# True means monotonic; false means non-monotonic.
def monotonicity(prefs):
    num_of_candidates = len({rank for voter in prefs for rank in voter})
    preferences = copy.deepcopy(prefs)
    # this is helpful to know which helper function to send preferences to
    check_ties_result = check_ties(prefs)
    candidates_ranked = check_ties_result[0]
    result = None
    if num_of_candidates <= 2:
        # This would not be mathematically possible.
        return True
    elif num_of_candidates == 3 and candidates_ranked is False:
        result = monotonicity_three_candidates(prefs, check_ties_result[1])
    elif candidates_ranked > 3 or candidates_ranked is True:
        ranking = ranked_choice(preferences)
        new_prefs = []
        for voter in prefs:
            new_prefs.append([value for value in voter if value in ranking])
        result = monotonicity_three_candidates(new_prefs, check_ties_result[1])
    return result


def check_ties(preferences):
    candidate_counts = defaultdict(int)

    # Count the first preference votes for each candidate
    for voter_pref in preferences:
        if voter_pref:
            candidate = voter_pref[0]
            candidate_counts[candidate] += 1

    # Find candidates with the maximum number of first preference votes
    max_votes = max(candidate_counts.values())
    tied_candidates = [candidate for candidate, count in candidate_counts.items() if count == max_votes]

    if len(tied_candidates) > 1:
        return True, candidate_counts

    return False, candidate_counts


def monotonicity_three_candidates(prefs, totals):
    list_of_candidates = first_past_the_post(prefs)
    num_of_votes = len(prefs)
    a = totals[list_of_candidates[0]] / num_of_votes
    b = totals[list_of_candidates[1]]/ num_of_votes
    c = totals[list_of_candidates[2]] / num_of_votes
    alpha = transfer_ij(prefs, list_of_candidates[2], list_of_candidates[1]) - \
            transfer_ij(prefs, list_of_candidates[2], list_of_candidates[0])
    beta = transfer_ij(prefs, list_of_candidates[1], list_of_candidates[2]) - \
           transfer_ij(prefs, list_of_candidates[1], list_of_candidates[0])
    one = condition_one(b, c)
    two = condition_two(a, b, c, alpha)
    three = condition_three(a, b, c, beta)
    if one and two and three:
        return False
    else:
        return True


def transfer_ij(prefs, i, j):
    new_prefs = []
    for voter in prefs:
        if voter[0] == i:
            new_prefs.append(voter)
    num_of_js = 0
    for voter in new_prefs:
        if voter[1] is j:
            num_of_js = num_of_js + 1
    if num_of_js != 0:
        return num_of_js / len(new_prefs)
    else:
        return 0


def condition_one(b, c):
    if b > c:
        return True


def condition_two(a, b, c, alpha):
    if a < (b + (alpha * c)):
        return True


def condition_three(a, b, c, beta):
    if a > max(((2 * b) - c), (((2 + beta) * b) - c)):
        return True
