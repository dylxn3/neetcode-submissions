class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicto = defaultdict(int)
        i = 0 
        result = 0 

        for j in range(len(s)):
            dicto[s[j]]+=1
            currlen = j - i + 1
            maxFreq = max(dicto.values())

            if currlen - maxFreq > k:
                dicto[s[i]]-=1
                i+=1
            
            result = max(result, j - i+1)
        
        return result