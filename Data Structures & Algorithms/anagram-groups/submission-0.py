class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        group_anagrams = {}
        for word in strs:
            h_map = {}
            for c in word:
                h_map[c] = h_map.get(c, 0) + 1

            key = tuple(sorted(word))
            if key not in group_anagrams:
                group_anagrams[key] = []

            group_anagrams[key].append(word)

        return [v for v in group_anagrams.values()]