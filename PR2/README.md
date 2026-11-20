# Practical No. 2: Uninformed Search Algorithms – BFS and DFS

## 1. Aim

To implement Breadth First Search (BFS) and Depth First Search (DFS) algorithms for solving route-finding problems and compare their performance based on path length, nodes explored, and execution time.

## 2. Description

Uninformed Search Algorithms search for a goal without using additional information or heuristics about the goal's location.

In this practical, we use a graph representing a route map. Each node represents a location, and each edge represents a connection between two locations.

We implement two search algorithms:

- **Breadth First Search (BFS):** Explores neighboring nodes level by level using a queue (FIFO).
- **Depth First Search (DFS):** Explores one branch as deeply as possible before backtracking, using a stack (LIFO).

## 3. Libraries Used

- `collections.deque`: Used to implement the queue in BFS.
- `time`: Used to measure the execution time of BFS and DFS.

Both are built-in Python modules. No external libraries are required.

## 4. Code Explanation

### A. Importing Libraries

```python
from collections import deque
import time
```

- `deque` provides an efficient queue for BFS.
- `time` measures how long each algorithm takes to execute.

### B. Creating the Route Graph

```python
route_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```

The graph is represented using an adjacency list.

- A, B, C, D, E and F represent locations.
- Each list contains the neighboring locations.
- For example, A is connected to B and C.

### C. Breadth First Search (BFS)

```python
def bfs_route(graph, start, goal):
```

This function finds a route from the starting node to the goal node using BFS.

1. `start_time = time.time()` records the starting time.
2. `queue = deque([[start]])` creates a queue containing the initial path.
3. `visited = {start}` stores already visited nodes.
4. `nodes_explored = 0` initializes the node counter.
5. `while queue:` continues searching while paths remain in the queue.
6. `queue.popleft()` removes the first path (FIFO).
7. `node = path[-1]` gets the last node of the current path.
8. `nodes_explored += 1` increments the explored-node counter.
9. `if node == goal:` checks whether the destination is reached.
10. The function returns the path, nodes explored and execution time when the goal is found.
11. The `for` loop checks neighboring nodes.
12. `visited.add(neighbor)` marks a new node as visited.
13. A new path is created and added to the queue.

If the goal cannot be reached, the function returns `None`.

**BFS guarantees the shortest path in an unweighted graph.**

### D. Depth First Search (DFS)

```python
def dfs_route(graph, start, goal):
```

This function finds a route using DFS.

1. `start_time = time.time()` records the starting time.
2. `stack = [[start]]` creates a stack containing the initial path.
3. `visited = set()` stores visited nodes.
4. `nodes_explored = 0` initializes the counter.
5. `while stack:` continues searching while paths remain.
6. `stack.pop()` removes the most recently added path (LIFO).
7. `node = path[-1]` gets the current node.
8. `if node not in visited:` prevents repeated exploration.
9. `visited.add(node)` marks the node as visited.
10. `nodes_explored += 1` increments the counter.
11. `if node == goal:` checks whether the destination is reached.
12. `reversed(graph.get(node, []))` reverses the neighbor order before pushing paths onto the stack.
13. New paths are created and added to the stack.

If the goal cannot be reached, the function returns `None`.

**DFS does not guarantee the shortest path.**

### E. Testing the Algorithms

```python
print("BFS:", bfs_route(route_graph, 'A', 'F'))
print("DFS:", dfs_route(route_graph, 'A', 'F'))
```

Both algorithms are executed with:

- Starting node: A
- Goal node: F

The results display the discovered path, number of nodes explored and execution time.

## 5. Performance Comparison

| Parameter | BFS | DFS |
|---|---|---|
| Data structure | Queue | Stack |
| Search strategy | Level by level | Depth first |
| Path found | A → C → F | A → B → E → F |
| Path length (edges) | 2 | 3 |
| Nodes explored | 6 | 5 |
| Shortest path guaranteed? | Yes, for unweighted graphs | No |

Execution time is measured using the `time` module. It may vary slightly between executions.

### Evaluation Parameters

**1. Path Length:** Number of edges between the starting location and destination. A smaller path length indicates a shorter route.

**2. Nodes Explored:** Number of nodes processed by the search algorithm before finding the goal.

**3. Execution Time:** Time taken by the algorithm to find the goal, measured in seconds.

## 6. Time and Space Complexity

Let V represent the number of vertices and E represent the number of edges.

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |

These are graph-traversal complexities using an adjacency list.

## 7. Conclusion

BFS and DFS were successfully implemented for a route-finding problem.

BFS found the shortest route from A to F, whereas DFS found a valid route that was longer. Their performance was compared using path length, nodes explored and execution time.

Thus, BFS is suitable when the shortest path is required, while DFS is useful for exploring graph branches.

## 8. Dependencies and Execution

Python 3 is required. The program uses only built-in Python modules, so no additional packages need to be installed.

Run the program using:

```bash
python3 BFS_DFS.py
```

