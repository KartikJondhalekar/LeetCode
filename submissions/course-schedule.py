# Problem #207: Course Schedule
# Difficulty : Medium
# Language   : python3
# Runtime    : 3 ms
# Memory     : 21.3 MB
# URL        : https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = { i : [] for i in range(numCourses)}
        visited = set()

        for course, preReq in prerequisites:
            preReqMap[course].append(preReq)

        def dfs(course):
            if course in visited:
                return False

            if preReqMap[course] == []:
                return True

            visited.add(course)

            for preReq in preReqMap[course]:
                if not dfs(preReq):
                    return False

            visited.remove(course)
            preReqMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True