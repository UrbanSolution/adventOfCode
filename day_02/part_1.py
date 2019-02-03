import numpy as np

with open('input.txt', 'r') as f:
    ids = [list(l.replace('\n', '')) for l in f.readlines()]


def count_duplets_and_triplets(_id):
    counts = np.unique(_id, return_counts=True)[1]
    if 2 in counts:
        if 3 in counts:
            return 1, 1
        return 1, 0
    if 3 in counts:
        return 0, 1
    return 0, 0


def checksum(ids):
    n_duplets = 0
    n_triplets = 0
    for _id in ids:
        counts = count_duplets_and_triplets(_id)
        n_duplets += counts[0]
        n_triplets += counts[1]
    return n_duplets * n_triplets


print(f'Checksum is : {checksum(ids)}')
