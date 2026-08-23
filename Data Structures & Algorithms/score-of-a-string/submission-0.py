class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        score = 0
        while i<len(s)-1:
            score += abs(ord(s[i]) - ord(s[i+1]))
            i +=1
        return score
        