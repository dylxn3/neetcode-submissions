class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        
        for key, val in freq.items(): 
            if len(heap) < k: 
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        res = []
        for key, val in heap: 
            res.append(val)

        return res