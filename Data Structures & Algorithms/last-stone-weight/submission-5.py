class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index, stone in enumerate(stones):
            stones[index] = -stone
        
        heapq.heapify(stones)

        while stones:
            stone1 = -heapq.heappop(stones)
            if not stones:
                return stone1
            else:
                stone2 = -heapq.heappop(stones)
                if stone1 > stone2:
                    heapq.heappush(stones, stone2 - stone1)
        return 0