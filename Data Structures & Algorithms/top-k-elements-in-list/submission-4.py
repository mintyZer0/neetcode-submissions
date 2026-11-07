class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}

        for n in nums:
            if n not in num_map:
                num_map.setdefault(n, 1)
            elif n in num_map:
                num_map[n] += 1
        sorted_dict = dict(sorted(num_map.items(), key=lambda item:item[1], reverse=True ))
        sorted_keys = list(sorted_dict.keys())
        return sorted_keys[:k]