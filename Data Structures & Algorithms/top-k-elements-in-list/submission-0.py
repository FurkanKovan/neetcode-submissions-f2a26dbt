class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        sorted_freq_map = dict(sorted(freq_map.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_freq_map)[:k]