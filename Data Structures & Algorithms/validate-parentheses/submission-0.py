class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s) % 2 != 0:
            return False
        
        chars = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

        for c in s:
            if c in chars:
                stack.append(c)
                continue
            if not stack:
                return False
            if chars[stack.pop()] == c:
                continue
            return False

        return len(stack) == 0