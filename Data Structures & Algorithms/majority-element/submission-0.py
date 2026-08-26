class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority_element = None

        for num in nums:
            if count==0:
                majority_element=num
                count +=1
            elif majority_element==num:
                count +=1
            else:
                count -=1
        if nums.count(majority_element) > len(nums)/2:
            return majority_element
        return -1
