class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        finalList = []
        i , j = 0, 0

        while i < len(nums):
            if j != len(nums) - 1: j = j + 1
            if nums[i] + nums[j] == target:
                finalList.append(i)
                finalList.append(j)
            if j == len(nums) - 1:
                i = i + 1
                j = i
        
        return list(set(sorted(finalList)))
        



        