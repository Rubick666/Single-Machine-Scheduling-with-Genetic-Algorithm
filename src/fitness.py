from config import n_jobs, processing_times, setup_times, weights

def evaluate(sequence):
    """Calculate total weighted completion time for a job sequence"""
    completion_times = []
    completion_times.append(processing_times[sequence[0]])
    for k in range(1, n_jobs):
        prev = sequence[k-1]
        curr = sequence[k]
        completion_times.append(completion_times[-1] + setup_times[prev][curr] + processing_times[curr])
    total = sum(weights[sequence[k]] * completion_times[k] for k in range(n_jobs))
    return 1 / total  # fitness is inverse