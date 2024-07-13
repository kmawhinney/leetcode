from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TOPOLOGICAL SORT SOLUTION
        
        graph = {} # Prereq: List of Courses
        inDegree = {} # Course: Number of Prereqs

        for course in range(numCourses):
            graph[course] = []
            inDegree[course] = 0

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1

        q = deque([course for course in inDegree if inDegree[course] == 0])
        completedCourses = 0

        while q:
            course = q.popleft()
            completedCourses += 1

            for neighbor in graph[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    q.append(neighbor)

        return completedCourses == numCourses
