class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = tuple(zip(heights, names))
        sort_by_heights = sorted(mapping,reverse=True)
        return [height[1] for height in sort_by_heights]