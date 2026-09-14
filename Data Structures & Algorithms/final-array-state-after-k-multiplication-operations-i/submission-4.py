class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        while k > 0: 
            i = 0
            minimum = min(nums)
            while nums[i] != minimum: 
                i+=1
            nums[i] *= multiplier
            k-=1
        
        return nums
            