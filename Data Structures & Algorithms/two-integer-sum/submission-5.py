class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = len(nums)
        while i > 0:
            i -= 1
            for j in range(len(nums)):
                if nums[j] + nums[i] == target:
                    return [j,i]