class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_text = ''.join(c for c in s.lower() if c.isalnum())
        
        left = 0
        right = len(filtered_text)-1

        while left <= right:
            if filtered_text[left] != filtered_text[right]:
                return False
            left += 1
            right -= 1

        return True
