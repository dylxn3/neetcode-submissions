
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = Counter(tasks)
        heap = [-x for x in frequency.values()]
        heapq.heapify(heap)
        q = deque()

        mins = 0
        while heap or q: 
            mins+=1
            if heap: 
                task = heapq.heappop(heap)
                task+=1
                if task < 0: 
                    q.append([task, mins+n])
            
            if q and q[0][1] == mins: 
                task = q.popleft()
                heapq.heappush(heap, task[0])

        return mins

