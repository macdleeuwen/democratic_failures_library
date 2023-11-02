# The majority criterion states that if a candidate is preferred (ranked first)
# by more than half of voters, they must win.

def majority(prefs, winner):
    num_voters = len(prefs)

    results = {}
    for voter in prefs:
        if voter[0] not in results.keys():
            results[voter[0]] = 1
        else:
            results[voter[0]] = results[voter[0]] + 1

    plurality = max(results, key=results.get)

    if results[plurality] / num_voters > 0.5:
        if plurality == winner:
            return True
        else:
            return False
    else:
        return True
