# Independence of irrelevant alternatives refers to the ability of a voting method to return
# the same ordering between two candidates irrespective of the inclusion of an additional candidate.

# For instance, if A is preferred to B without the inclusion of C, including C in the election
# should not change the relative ranking of A and B.

# Called IIA as a function bc independence of irrelevant alternatives is a long name!

from election_systems.borda_count import borda_count
from election_systems.first_past_the_post import first_past_the_post
from election_systems.ranked_choice import ranked_choice

method_dict = {"IRV": ranked_choice, "FPTP": first_past_the_post,
               "Borda": borda_count}


def iia(prefs, ranking, method):
    list_of_candidates = sorted({rank for voter in prefs for rank in voter})
    # this would be impossible
    if len(list_of_candidates) <= 2:
        return True

    # True for satisfies IIA; false for does not
    result = True

    for candidate in list_of_candidates:
        temp_list = list(list_of_candidates)
        temp_list.remove(candidate)

        temp_ranking = list(ranking)
        for rank in ranking:
            if rank == candidate:
                temp_ranking.remove(rank)

        new_prefs = []
        for voter in prefs:
            new_prefs.append([value for value in voter if value in temp_list])

        new_ranking = method_dict[method](new_prefs)

        final_new_ranking = []
        for each in new_ranking:
            final_new_ranking.append(each)
        final_original_ranking = []
        for each in temp_ranking:
            final_original_ranking.append(each)

        if final_original_ranking != final_new_ranking:
            result = False

    return result
