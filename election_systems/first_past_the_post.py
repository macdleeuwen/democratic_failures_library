# This function, given a list of lists where each list represents a voter's preferences and the
# placement on the list reflects the ordering of candidates (i.e., [B, A, C] suggests that the
# voter prefers B to A and A to C), returns an ordered list of the candidates, reflecting their
# relative rank. [B, A, C] would mean B had more votes than A who had more than C.
# This election system is called First Past the Post.
# FPTP only allows someone to register their first choice, but since this library needs to be
# able to take in whole sets of preferences, for this system I'm just cutting out the rest
# of the list of preferences (voter is the preference list for a voter, voter[0] is only
# their first preference).

def first_past_the_post(prefs):
    # Instantiating dictionary.
    results = {}
    for voter in prefs:
        if voter[0] not in results.keys():
            results[voter[0]] = 1
        else:
            results[voter[0]] = results[voter[0]] + 1
    # Flip the results
    sorted_result = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # turn the result into a sorted list
    results_list = []
    for each in sorted_result:
        results_list.append(each[0])

    return results_list





