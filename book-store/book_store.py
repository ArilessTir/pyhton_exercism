def total(basket):
    if len(basket) is 0:
        return 0

    if len(set(basket)) is 5:
        return 8 * len(basket) * 0.75
