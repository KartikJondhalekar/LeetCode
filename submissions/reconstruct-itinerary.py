# Problem #332: Reconstruct Itinerary
# Difficulty : Hard
# Language   : python3
# Runtime    : 0 ms
# Memory     : 20 MB
# URL        : https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = collections.defaultdict(list)

        for source, destination in tickets:
            flights[source].append(destination)

        for source in flights:
            flights[source].sort(reverse=True)

        res = []

        def dfs(source):
            while flights[source]:
                destination = flights[source].pop()
                dfs(destination)

            res.append(source)
        
        dfs('JFK')

        return res[::-1]