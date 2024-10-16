graph = {
    "": [],
}

def IDFS(root, goal):
    depth = 0
    while True:
        print(f"Looping at depth {depth}")
        result = DLS(root, goal, depth)
        print(f"Result: {result}, Goal: {goal}")
        if result == goal:
            return result
        depth = depth + 1

def DLS(node, goal, depth):
    print(f"node: {node}, goal: {goal}, depth: {depth}")
    if depth == 0 and node == goal:
        print("Found goal")
        return node
    elif depth > 0:
        print(f"Looping through children: {graph.get(node, [])}")
        for child in graph.get(node, []):
            if goal == DLS(child, goal, depth - 1):
                return goal


root = input("Enter the root node: ")
goal = input("Enter the goal node: ")

IDFS(root, goal)
