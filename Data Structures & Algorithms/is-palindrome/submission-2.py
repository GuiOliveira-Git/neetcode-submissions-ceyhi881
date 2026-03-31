class Solution:

    def isPalindrome(self, s: str) -> bool:
        def formatString(input_string):
            # Use regular expression to replace non-alphanumeric characters with an empty string
            input_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
            input_string = input_string.lower()
            return input_string

        text = formatString(s)
        left = 0
        right = len(text)-1

        while left < right:
            if text[left] != text[right]: 
                return False
            left+=1
            right-=1

        return True