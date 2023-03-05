from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]

    Create all k-combinations of digits and keep those with sum n:
