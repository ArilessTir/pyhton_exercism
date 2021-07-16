def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(x for x in scores if x!=0)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]