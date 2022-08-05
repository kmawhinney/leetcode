from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)
        indegree = defaultdict(int)
        result = []
        
        for course, prereq in prerequisites:
            prereq_map[prereq].append(course)
            indegree[course] = indegree.get(course, 0) + 1
        
        queue = deque()

        for course in range(numCourses):
            if course not in indegree:
                queue.append(course)
        
        while queue:
            curr_prereq = queue.popleft()
            result.append(curr_prereq)
            
            for neighbour in prereq_map[curr_prereq]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(result) == numCourses:
            return result
        else:
            return []
