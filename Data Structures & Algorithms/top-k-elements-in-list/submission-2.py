class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        kmap = defaultdict(list)
        retresu = []
        
        check = True
        i = 0

        while i < len(nums):
            count = 1
            curv = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] == curv:
                count += 1
                j += 1
            i = j         

            kmap[count].append(curv)

        sorted_data = dict(sorted(kmap.items(), reverse=True))
        rept = 1
        for key in sorted_data:
            if rept > k:
                break
            for l in sorted_data[key]:
                retresu.append(l)
            rept += 1


        return retresu[0:k]
