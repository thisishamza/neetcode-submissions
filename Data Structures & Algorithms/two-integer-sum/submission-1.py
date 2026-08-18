class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted((num,i) for i, num in enumerate(nums))
        left = 0
        right = len(nums) - 1
        while left < right:
            if indexed[left][0] + indexed[right][0] == target:
                return sorted([indexed[left][1] , indexed[right][1]])
            if indexed[left][0] + indexed[right][0] < target:
                left +=1
            else:
                right -=1


