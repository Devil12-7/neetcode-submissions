class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        twosMap = {}
        twolList = []

        for i, j in enumerate(nums):
            rem = target - j
            if twosMap.get(rem) == None :
                twosMap[j] = i
            else:
                twolList.append(i)
                twolList.append(twosMap.get(rem))
        
        return sorted(twolList)



        


        



        
        



        