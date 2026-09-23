class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def dfs(i, currentSum):
            if currentSum == target:
                res.append(sol[:])
                return 
            
            if i == len(nums) or currentSum > target:
                return
            
            dfs(i+1, currentSum)

            sol.append(nums[i])
            dfs(i, currentSum + nums[i])
            sol.pop()
        
        dfs(0,0)
        return res

            