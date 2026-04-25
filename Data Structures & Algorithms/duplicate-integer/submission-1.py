class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for index, num in enumerate(nums):
            for num1 in nums[index + 1:]:
                if num1 == num:
                    return True

        return False
