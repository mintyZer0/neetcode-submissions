class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = self.map_chars(s)
        t_map = self.map_chars(t)
        if s_map == t_map:
            return True
        else:
            return False
        
    
    def map_chars(self, s: str) -> dict:
        char_map = {}
        for char in s:
            if char not in char_map:
                char_map[char] = 1
            else:
                char_map[char] += 1

        return char_map
