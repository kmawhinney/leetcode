from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereq = defaultdict(list) # course:prereqs

        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)

        visited = set()

        def dfs(course):
            # Base cases
            if course in visited:
                return False
            if not course_to_prereq[course]:
                return True

            # Recursive case
            visited.add(course)
            for prereq in course_to_prereq[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            course_to_prereq[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
