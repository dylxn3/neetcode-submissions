class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
        for character in charSet:
            left = 0
            count = 0
            for r in range(len(s)):
                if s[r] == character:
                    count+=1
                
                while(r-left+1) - count > k:
                    if s[left] == character:
                        count-=1
                    left+=1
                
                res = max(res, r-left + 1)
        
        return res