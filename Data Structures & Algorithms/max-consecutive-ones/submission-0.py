class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        ones = 0
        for num in nums:
            if num == 1:
                ones +=1
            else:
                ones = 0
            if ones> max_one:
                max_one = ones

        return max_one


                
            
