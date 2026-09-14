class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hash = new Map()
        for (let i =0; i< nums.length; i++){
            let difference = target - nums[i]
            const sumIndex = hash.get(difference);
            if (hash.has(difference)){
                return[i, hash.get(difference)]
            }
            hash.set(nums[i],i)
        }
        return[0,0]
    
    
    }

  

}
