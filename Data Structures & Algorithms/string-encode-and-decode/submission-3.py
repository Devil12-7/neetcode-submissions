class Solution:
    def encode(self, strs: List[str]) -> str:
        nStr = ""

        for strr in strs:
            nStr += str(len(strr)) + "#" + strr
        
        return nStr

    def decode(self, s: str) -> List[str]:

        i, retList = 0, []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            lenS = int(s[i:j])
            i = j + 1
            j = i + lenS
            retList.append(s[i:j])
            i = j
        return retList
            

            

        
        
        
        

      
