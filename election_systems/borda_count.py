# This function, given a list of lists where each list represents a voter's preferences and the
# placement on the list reflects the ordering of candidates (i.e., [B, A, C] suggests that the
# voter prefers B to A and A to C), assigns a value to being placed in a particular order on the
# list, and gives the candidate with the highest total "value" count. F

def borda_count(prefs):
    results = {}
    # The number of candidates determines the number of points allotted for a particular rank
    num_of_candidates = len({rank for voter in prefs for rank in voter})
    for voter in prefs:
        # enumerate provides a way to count position in the list
        for rank in enumerate(voter):
            if rank[1] not in results.keys():
                # if the candidate isn't already in the results dict, add them
                # their score is just the number of candidates - their rank
                results[rank[1]] = num_of_candidates - rank[0]
            else:
                # same thing except add that score to their existing score
                results[rank[1]] = results[rank[1]] + (num_of_candidates - rank[0])
    sorted_result = sorted(results.items(), key=lambda x: x[1], reverse=True)

    results_list = []
    for each in sorted_result:
        results_list.append(each[0])

    return results_list

