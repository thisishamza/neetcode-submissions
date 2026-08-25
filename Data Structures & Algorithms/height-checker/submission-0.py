class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        order = 0
        for h1,h2 in zip(heights, sort_heights):
            if h1 != h2:
                order +=1
        return order
