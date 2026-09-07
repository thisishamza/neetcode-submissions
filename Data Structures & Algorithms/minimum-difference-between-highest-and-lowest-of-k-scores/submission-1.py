class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        min_diff = float('inf')
        for i in range(0,n-k+1):
            window_diff = nums[i+k-1] - nums[i]
            min_diff = min(min_diff, window_diff)
        return min_diff
        
            


