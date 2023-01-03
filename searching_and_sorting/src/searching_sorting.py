from typing import List

def sorted_merge(a: List[int], b: List[int]) -> List[int]:
    count_iter = 0
    max_index = 0
    for item_b in b:
        if max_index >= len(a) - 1:
            a.extend(b[b.index(item_b):])
            count_iter += 1
            return a
        for item_a in a[max_index:]:
            count_iter += 1
            if item_b <= item_a:
                a.insert(a.index(item_a), item_b)
                max_index = a.index(item_a)
                break
    print(count_iter)
    return a
