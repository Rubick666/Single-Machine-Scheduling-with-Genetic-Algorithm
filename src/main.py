import matplotlib.pyplot as plt
from config import POP_SIZE, MAX_GEN, ELITISM, TOURNAMENT_K, n_jobs
from fitness import evaluate
from operators import order_crossover, swap_mutation
from selection import tournament_selection

# -----------------------------
# Genetic Algorithm
# -----------------------------
def genetic_algorithm(crossover_func=order_crossover, mutation_func=swap_mutation, 
                      pop_size=POP_SIZE, max_gen=MAX_GEN, elitism=ELITISM):
    # initialize population
    population = []
    for _ in range(pop_size):
        seq = list(range(n_jobs))
        random.shuffle(seq)
        fitness = evaluate(seq)
        population.append((seq, fitness))

    best_fitnesses = []
    avg_fitnesses = []

    for gen in range(max_gen):
        # sort population
        population.sort(key=lambda ind: ind[1], reverse=True)
        new_pop = population[:elitism]  # elitism

        # record stats
        best_fitnesses.append(population[0][1])
        avg_fitnesses.append(sum(ind[1] for ind in population)/pop_size)

        # generate new individuals
        while len(new_pop) < pop_size:
            p1 = tournament_selection(population, k=TOURNAMENT_K)
            p2 = tournament_selection(population, k=TOURNAMENT_K)
            child = crossover_func(p1, p2)
            child = mutation_func(child)
            new_pop.append((child, evaluate(child)))

        population = new_pop

    # final result
    population.sort(key=lambda ind: ind[1], reverse=True)
    best_seq, best_fit = population[0]
    return best_seq, 1/best_fit, max_gen, best_fitnesses, avg_fitnesses

# -----------------------------
# Run Example
# -----------------------------
if __name__ == "__main__":
    import random # Needed for initial shuffle inside genetic_algorithm

    # Example: Order crossover + Swap mutation
    best_seq, best_cost, gens, best_f, avg_f = genetic_algorithm(order_crossover, swap_mutation)

    print("Best sequence:", best_seq)
    print("Minimum total weighted completion time:", best_cost)
    print("Generations executed:", gens)

    # Plot fitness
    plt.plot(best_f, label="Max fitness")
    plt.plot(avg_f, label="Average fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.show()