class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        first_ch = ''
        for k,v in freq.items():
            if v == 1:
                first_ch = k
                break
        if first_ch:
            return s.index(first_ch)
        else:
            return -1
                
