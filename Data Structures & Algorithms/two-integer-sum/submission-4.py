class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, value in enumerate(nums):
            current = target - value
            if current in hash:
                return [hash[current], index]
            else:
                hash[value] = index
        
        
