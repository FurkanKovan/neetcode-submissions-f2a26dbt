class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for _ in range(len(nums) + 1)]
        freq_count = {}

        for n in nums:
            freq_count[n] = freq_count.get(n, 0) + 1

        for n, freq in freq_count.items():
            freq_list[freq].append(n)

        result = []
        for i in range(len(freq_list) - 1, 0, -1):
            for n in freq_list[i]:
                result.append(n)
                if len(result) == k:
                    return result


