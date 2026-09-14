class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # have a heap going up to k length
        heap = nums[:k]
        heapq.heapify(heap)
        # looking at remaining elements
        for n in nums[k:]:
            # if n > heap[0] means in kth spot
            if n > heap[0]:
                # replace and push
                heapq.heappop(heap)
                heapq.heappush(heap, n)
            
        return heap[0]