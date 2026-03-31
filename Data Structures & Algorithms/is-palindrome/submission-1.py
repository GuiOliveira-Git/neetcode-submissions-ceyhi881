class Solution:

    def isPalindrome(self, s: str) -> bool:
        def remove_non_alphanumeric(input_string):
            cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
            return cleaned_string

        rev = s[::-1]

        return remove_non_alphanumeric(s.lower()) == remove_non_alphanumeric(rev.lower())