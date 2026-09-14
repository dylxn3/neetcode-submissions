class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for number in nums[k:]:
            if number > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
            
        
        return heap[0]