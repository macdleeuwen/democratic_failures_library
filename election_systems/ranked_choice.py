# This function, given a list of lists where each list represents a voter's preferences and the
# placement on the list reflects the ordering of candidates (i.e., [B, A, C] suggests that the
# voter prefers B to A and A to C), returns an ordered list of the candidates.
# If any candidate receives more than 50% first-choice placements, they win. If no candidate does,
# the candidate with the least first-choice placements is eliminated, and the process continues.
# This election system is called Ranked Choice.
from collections import defaultdict


def ranked_choice(prefs):
    candidates = set(candidate for voter_pref in prefs for candidate in voter_pref)
    eliminated_candidates = set()


    while True:
        candidate_counts = defaultdict(int)

        # Count the first preference votes for each candidate
        for voter_pref in prefs:
            for candidate in voter_pref:
                if candidate not in eliminated_candidates:
                    candidate_counts[candidate] += 1
                    break  # Move to the next voter

        # Find all candidates with no votes in this round
        candidates_with_no_votes = {c for c in candidates if c not in candidate_counts}
        candidate_counts.update({c: 0 for c in candidates_with_no_votes})

        # Sort candidates by vote count
        sorted_candidates = sorted(candidate_counts.keys(), key=lambda x: (-candidate_counts[x], x))

        # Check if any candidate has more than 50% of the first preference votes
        for candidate in sorted_candidates:
            if candidate_counts[candidate] > len(prefs) / 2:
                return sorted_candidates

        # Find the candidate with the fewest first preference votes
        eliminated_candidate = sorted_candidates[-1]

        # Eliminate the candidate with the fewest votes
        eliminated_candidates.add(eliminated_candidate)

        # Update the preferences by removing eliminated candidate from voters' lists
        for i in range(len(prefs)):
            while eliminated_candidate in prefs[i]:
                prefs[i].remove(eliminated_candidate)
