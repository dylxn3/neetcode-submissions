class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        visited = set()
        completed = set()

        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        
        def backtrack(course):
            if course in visited:
                return False
            
            if course in completed:
                return True
            
            visited.add(course)
            for prereqs in hashmap[course]:
                if not backtrack(prereqs):
                    return False 
                
            visited.remove(course)
            completed.add(course)
            return True
        
        for course in range(numCourses):
            if not backtrack(course):
                return False
            
        
        return True 
