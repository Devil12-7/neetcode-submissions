class Solution:
    def encode(self, strs: List[str]) -> str:
        nstr = ""
        for s in strs:
            nstr += str(len(s)) + "#" + s
        return nstr

    def decode(self, s: str) -> List[str]:
        slist, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            strlen = int(s[i:j])
            
            word = s[j+1 : j + 1 + strlen]
            slist.append(word)
            i = j + 1 + strlen

        return slist
        
        
        

      
