class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for string in strs:
            # Prefix each string with its length and a special character '#'
            encoded_string += f"{len(string)}#{string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        decoded_strings = []
        i = 0
        
        while i < len(s):
            # Find the position of the next '#'
            j = s.find('#', i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string using the length and append to the result
            decoded_strings.append(s[j+1:j+1+length])
            # Move the index past the current string
            i = j + 1 + length
        
        return decoded_strings