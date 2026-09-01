class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = sorted(zip(heights, names), reverse=True)
        return [name for height,name in mapping]