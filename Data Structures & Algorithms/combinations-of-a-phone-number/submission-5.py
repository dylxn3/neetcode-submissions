class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits:
            return []
        res, sol = [],[]
        def backtrack(i):
            if i == len(digits):
                res.append(''.join(sol[:]))
                return 
            
            for j in phone[digits[i]]: 
                sol.append(j)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res
