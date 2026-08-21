class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        match_val = list(matching_brackets.values())
        stack = []
        for bracket in s:
            if bracket in match_val:
                stack.append(bracket)
            else:
                if not stack or stack[-1] !=matching_brackets.get(bracket):
                    return False
                stack.pop()
        return len(stack) == 0
