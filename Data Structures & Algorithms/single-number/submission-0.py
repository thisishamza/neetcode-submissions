class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = Counter(nums)
        for k,v in arr.items():
            if v == 1:
                return k