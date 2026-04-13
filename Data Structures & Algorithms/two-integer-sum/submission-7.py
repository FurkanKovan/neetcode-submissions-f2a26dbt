class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if hash_nums.get(diff) != None:
                return [min(i, hash_nums.get(diff)), max(i, hash_nums.get(diff))]
            else:
                hash_nums[nums[i]] = i
