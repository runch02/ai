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
    'A': ['a', 'b', 'c'],
    'a': [], 'b': [], 'c': [],
    'D': ['e', 'f', 'g'],
    'e': [], 'f': [], 'g': [],
    'H': ['i', 'j', 'k'],
    'i': [], 'j': [], 'k': [],
    'L': ['m', 'n', 'o'],
    'm': [], 'n': [], 'o': [],
    'P': ['q', 'r', 's'],
    'q': [], 'r': [], 's': [],
    'T': ['u', 'v', 'w'],
    'u': [], 'v': [], 'w': [],
    'X': ['y', 'z'],
    'y': [], 'z': []
}

f = First(graph, 'A', 'y')
print(f.bfs_shortest_path())


prac_1_1
