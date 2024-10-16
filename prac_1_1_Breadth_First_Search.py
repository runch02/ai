class First:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def bfs_shortest_path(self):
        explored = []
        queue = [[self.start]]

        if self.start == self.goal:
            return "That was easy! Start = Goal"
        
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in self.graph:
                continue

            neighbours = self.graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == self.goal:
                    return new_path
                
            explored.append(node)

        return "Path doesn't exist"

graph = {
    "": [],
}

start = input("Enter the Start Node: ")
goal = input("Enter the Goal Node: ")

f = First(graph, start, goal)
print(f.bfs_shortest_path())
