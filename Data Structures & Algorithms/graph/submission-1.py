class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def dfs(self, node, target, visit):
        if node == target:
            return True
        visit.add(node)
        for neighbour in self.graph[node]:
            if neighbour not in visit:
                if self.dfs(neighbour, target, visit):
                    return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())
        