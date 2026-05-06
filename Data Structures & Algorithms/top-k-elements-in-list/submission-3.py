class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # creates a map
        
        # store the num as a key and corresponding count as a value
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        arr = []
        # store count and number as list under list
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort() # sort based on count

        res = [] # create return list
        
        # take the second value i.e 1 and start from last since we are
        # doing most occured value
        while len(res) < k :
            res.append(arr.pop()[1])
        
        return res


