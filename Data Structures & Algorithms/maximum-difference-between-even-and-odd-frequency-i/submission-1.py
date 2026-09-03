class Solution:
    def maxDifference(self, s: str) -> int:
        max_diff = 0
        s = Counter(s)
        even = min(v for v in s.values() if v%2==0)
        odd = max(v for v in s.values() if v%2!=0)
        return odd - even
