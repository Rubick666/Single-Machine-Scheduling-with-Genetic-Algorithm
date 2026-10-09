import random

# -----------------------------
# Crossover Operators
# -----------------------------
def order_crossover(p1, p2):
    """Order Crossover (OX)"""
    size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[a:b] = p1[a:b]
    pos = b
    for x in p2:
        if x not in child:
            if pos == size: pos = 0
            child[pos] = x
            pos += 1
    return child

def pmx_crossover(p1, p2):
    """Partially Mapped Crossover (PMX)"""
    size = len(p1)
    a, b = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[a:b] = p1[a:b]
    for i in range(a, b):
        if p2[i] not in child:
            pos = i
            while child[pos] is not None:
                pos = p2.index(p1[pos])
            child[pos] = p2[i]
    for i in range(size):
        if child[i] is None:
            child[i] = p2[i]
    return child

def cycle_crossover(p1, p2):
    """Cycle Crossover (CX)"""
    size = len(p1)
    child = [None]*size
    index = 0
    while None in child:
        if child[index] is None:
            start = index
            while True:
                child[index] = p1[index]
                index = p1.index(p2[index])
                if index == start:
                    break
        index = child.index(None) if None in child else size
    return child

# -----------------------------
# Mutation Operators
# -----------------------------
def swap_mutation(seq):
    a, b = random.sample(range(len(seq)), 2)
    seq[a], seq[b] = seq[b], seq[a]
    return seq

def inversion_mutation(seq):
    a, b = sorted(random.sample(range(len(seq)), 2))
    seq[a:b] = reversed(seq[a:b])
    return seq

def scramble_mutation(seq):
    a, b = sorted(random.sample(range(len(seq)), 2))
    subset = seq[a:b]
    random.shuffle(subset)
    seq[a:b] = subset
    return seq