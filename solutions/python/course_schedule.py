class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # key is course, values is list of prereqs
        prereq_map = collections.defaultdict(list)
        
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if not prereq_map[course]:
                return True
            
            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
                
            visited.remove(course)
            prereq_map[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
