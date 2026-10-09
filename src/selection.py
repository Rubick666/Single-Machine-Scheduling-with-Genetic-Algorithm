import random

def tournament_selection(pop, k=3):
    """Pick best out of k random individuals"""
    selected = random.sample(pop, k)
    selected.sort(key=lambda ind: ind[1], reverse=True)
    return selected[0][0]