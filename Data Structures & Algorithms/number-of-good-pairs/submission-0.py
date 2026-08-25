class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pair = 0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i<j and nums[i] == nums[j]:
                    pair +=1
        return pair
        