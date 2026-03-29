class Solution:

    def dfs(self, node, visit):
        if node in visit:
            return True
        visit.add(node)

        if node not in self.graph:
            return False

        for neighbor in self.graph[node]:
            if self.dfs(neighbor, visit):
                return True
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        degree_in = [0] * numCourses
        visit = set()

        for pair in prerequisites:
            a = pair[0]
            b = pair[1]

            if a not in self.graph:
                self.graph[a] = set()
            if b not in self.graph:
                self.graph[b] = set()
            self.graph[b].add(a)
            degree_in[a] += 1
        
        for node in range(numCourses):
            if not degree_in[node]:
                if self.dfs(node, visit):
                    return False
        return len(visit) == numCourses