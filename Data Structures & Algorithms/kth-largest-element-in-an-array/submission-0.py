import heapq as heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        largest = heapq.nsmallest(k,max_heap)
        return -largest[-1]
