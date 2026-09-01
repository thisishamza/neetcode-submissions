class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = sorted(zip(heights, names), reverse=True)
        return [height[1] for height in mapping]