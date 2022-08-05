from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list) # prereq: courses it is a prereq for
        indegree = defaultdict(int) # course: num of prereqs required
        completed = []
        
        for course, prereq in prerequisites:
            prereq_map[prereq].append(course)
            indegree[course] = indegree.get(course, 0) + 1
            
        queue = deque() # queue contains only courses with fully completed prereqs
        for course in range(numCourses):
            if course not in indegree:
                queue.append(course)

        while queue:
            curr_prereq = queue.popleft()
            completed.append(curr_prereq)
            
            for neighbour in prereq_map[curr_prereq]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
            
        if len(completed) == numCourses:
            return True
        else:
            return False
