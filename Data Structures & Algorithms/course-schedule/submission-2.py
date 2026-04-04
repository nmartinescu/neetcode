class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0] * numCourses
        visit = set()
        queue = deque()

        for pair in prerequisites:
            a = pair[0]
            b = pair[1]
            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()
            graph[b].add(a)
            indegree[a] += 1
        for node in range(numCourses):
            if not indegree[node]:
                queue.append(node)
        while queue:
            node = queue.popleft()
            visit.add(node)

            for neighbor in graph.get(node, []):
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    queue.append(neighbor) 
        
        return len(visit) == numCourses