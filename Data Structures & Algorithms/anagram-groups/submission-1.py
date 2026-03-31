class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        abcdefghijklmnopqrstuvwxyz
        act ---> [act, cat]
        opst --> [pots, tops, stop]
        aht ---> [hat]
        """
        sorted_chars_to_string = {}
        for s in strs:
            char_list = list(s)
            char_list.sort()
            sorted_string = ''.join(char_list)

            if sorted_string not in sorted_chars_to_string:
                sorted_chars_to_string[sorted_string] = [s]
            else:
                sorted_chars_to_string[sorted_string].append(s)

        res = []
        for k, v in sorted_chars_to_string.items():
            res.append(v)
        return res

