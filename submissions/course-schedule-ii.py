# Problem #210: Course Schedule II
# Difficulty : Medium
# Language   : python3
# Runtime    : 0 ms
# Memory     : 21.6 MB
# URL        : https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqMap = {i : [] for i in range(numCourses)}
        visited = set()
        completed = set()
        res = []

        for c, p in prerequisites:
            preReqMap[c].append(p)

        def dfs(c):
            if c in visited:
                return False

            if c in completed:
                return True

            visited.add(c)

            for pc in preReqMap[c]:
                if not dfs(pc):
                    return False

            visited.remove(c)
            completed.add(c)
            res.append(c)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res