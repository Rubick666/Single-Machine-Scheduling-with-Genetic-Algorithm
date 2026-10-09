import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Problem Data
# -----------------------------
processing_times = [12, 7, 15, 5, 9, 11, 8]
weights = [4, 9, 3, 7, 5, 6, 8]

setup_times = [
    [0, 4, 6, 5, 7, 3, 4],
    [4, 0, 5, 6, 4, 5, 6],
    [6, 5, 0, 4, 5, 7, 6],
    [5, 6, 4, 0, 3, 4, 5],
    [7, 4, 5, 3, 0, 6, 4],
    [3, 5, 7, 4, 6, 0, 5],
    [4, 6, 6, 5, 4, 5, 0]
]

n_jobs = len(processing_times)

# -----------------------------
# GA Hyperparameters
# -----------------------------
POP_SIZE = int(os.getenv("POP_SIZE", 50))
MAX_GEN = int(os.getenv("MAX_GEN", 100))
ELITISM = int(os.getenv("ELITISM", 2))
TOURNAMENT_K = int(os.getenv("TOURNAMENT_K", 3))