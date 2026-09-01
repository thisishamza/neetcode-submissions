class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_t = Counter(nums)
        sorted_nums = sorted(nums_t.items(), key=lambda x: (x[1], -x[0]))
        vals = []
        for num, freq in sorted_nums:
            vals.extend([num] * freq)
        return vals
            
