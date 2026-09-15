class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        temp_check = 0
        for word in words:
            for ch in word:
                if ch in allowed:
                    temp_check += 1
            if temp_check == len(word):
                consistent +=1
            temp_check = 0
        return consistent
