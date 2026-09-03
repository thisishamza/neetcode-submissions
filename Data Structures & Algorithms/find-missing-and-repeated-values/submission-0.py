class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        griding = []
        missing = None
        repeated = None
        for g in grid:
            for i in g:
                griding.append(i)
        count_grid = Counter(griding)
        for i in range(1, len(griding)+1):
            if i not in griding:
                missing = i

        for k,v in count_grid.items():
            if v > 1:
                repeated = k
        return [repeated, missing]


