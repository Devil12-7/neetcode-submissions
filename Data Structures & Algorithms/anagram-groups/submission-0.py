class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)

        for c in strs:
            cValue = Counter(c)
            key = tuple(sorted(cValue.items()))
            hashMap[key].append(c)
        
        return list(hashMap.values())





        