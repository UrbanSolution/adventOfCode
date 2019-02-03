from itertools import combinations

with open('input.txt', 'r') as f:
    ids = [l.replace('\n', '') for l in f.readlines()]

for id_1, id_2 in combinations(ids, 2):
    has_diff = False
    diff_index = None
    for i, (char_1, char_2) in enumerate(zip(id_1, id_2)):
        if char_1 != char_2:
            if has_diff:
                break
            has_diff = True
            diff_index = i
    else:
        break

print(f'Common substring : {id_1[:diff_index] + id_1[diff_index+1:]}')
