def sum_series(nth=1, sequence=[0, 1]):
    """
    Generate a list of sums given a seed and return the Nth number.
    """
    for i in range(2, nth):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    # print(sequence)
    return sequence[nth - 1]


