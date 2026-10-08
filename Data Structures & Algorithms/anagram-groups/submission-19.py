class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        anagram_list = []

        for string in strs:
            s_sorted = "".join(sorted(string))
            anagram_map.setdefault(s_sorted, []).append(string)
            
        return list(anagram_map.values())


    # def map_anagram(self, s: str) -> dict:
    #     anagram_map = {}

    #     for char in s:
    #         if char not in anagram_map:
    #             anagram_map[char] = 1
    #         else:
    #             anagram_map[char] += 1

    #     return anagram_map