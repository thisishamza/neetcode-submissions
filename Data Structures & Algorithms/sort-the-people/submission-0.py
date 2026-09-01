class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = tuple(zip(names,heights))
        sort_by_heights = sorted(mapping, key = lambda x:-x[1])
        return [heights[0] for heights in sort_by_heights]