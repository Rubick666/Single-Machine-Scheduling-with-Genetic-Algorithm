# Benchmarks & Experimental Results

This document outlines the quantitative results of the Single-Machine Scheduling Genetic Algorithm under various configurations.

## Problem Overview
- **Objective:** Minimize total weighted completion time.
- **Fitness Function:** \(fitness(X) = 1 / T(X)\)
- **Dataset:** \(n=7\) jobs, with sequence-dependent setup times.
- **GA Parameters:** Population = 50, Max Generations = 100, Elitism = 2, Tournament Selection (k=3).

## 1. Crossover & Mutation Combinations (9 Tests)

The assignment required testing all 9 possible combinations of Crossover (OX, PMX, CX) and Mutation (Swap, Inversion, Scramble). 

| Crossover | Mutation | Best Sequence Found | Min Total Weighted Completion Time | Convergence Generation (Approx) |
| :--- | :--- | :--- | :--- | :--- |
| **OX** | Swap | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~15 |
| **OX** | Inversion | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~10 |
| **OX** | Scramble | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~8 |
| **PMX** | Swap | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~12 |
| **PMX** | Inversion | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~5 |
| **PMX** | Scramble | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~10 |
| **CX** | Swap | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~20 |
| **CX** | Inversion | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~5 |
| **CX** | Scramble | `[1, 4, 3, 6, 5, 0, 2]` | 1596.0 | ~8 |

*Note: The Max Fitness plateau for all runs is approximately `0.0006265`, which confirms that all 9 combinations successfully found the optimal sequence yielding a total weighted completion time of 1596.0.*

## 2. Observations & Discussion

- **Encoding:** Permutation representation successfully guarantees no repeating or missing jobs.
- **Elitism:** The top 2 individuals were preserved in every generation, ensuring the best solution never degraded.
- **Performance:** The plot for OX + Swap shows rapid initial improvement in Max Fitness, plateauing around generation 15, while Average Fitness fluctuates due to the random nature of tournament selection and mutation.
- **Convergence Speed:** While all combinations found the optimal solution, the PMX + Inversion and CX + Inversion combinations showed the fastest convergence (plateauing around generation 5). The CX + Swap combination was the slowest, taking roughly 20 generations to stabilize.
- **Conclusion:** The algorithm successfully minimized the total weighted completion time. The choice of crossover and mutation operators influenced the convergence speed but did not affect the final solution quality in this specific dataset.