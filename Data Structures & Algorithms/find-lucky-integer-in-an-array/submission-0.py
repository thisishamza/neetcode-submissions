class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = Counter(arr)
        num = -1
        for k,v in lucky.items():
            if k == v:
                if k>num:
                    num = k
        return num
