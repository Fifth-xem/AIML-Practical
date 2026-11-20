## 9. Conceptual Understanding

### 1. What are Uninformed Search Algorithms?

Uninformed Search Algorithms are search techniques that find a solution without using additional knowledge or heuristics about the goal.

They explore the available states or nodes systematically until the goal is found.

In this practical, we use a graph representing a route map, where:
- Nodes represent different locations.
- Edges represent connections between locations.
- Start node represents the starting location.
- Goal node represents the destination.

We implement BFS and DFS to find a route between the starting and destination locations.

### 2. Breadth First Search (BFS)

BFS explores the graph level by level. It first visits all neighboring nodes of the starting node, then moves to the next level.

**Working:**
1. Start from the initial node.
2. Insert it into a queue.
3. Remove the first node from the queue.
4. Check whether it is the goal.
5. If not, add its unvisited neighbors to the queue.
6. Repeat until the goal is found or the queue becomes empty.

**Important points:**
- Uses a Queue (FIFO – First In, First Out).
- Finds the shortest path in an unweighted graph.
- May require more memory because it stores multiple paths or nodes.

### 3. Depth First Search (DFS)

DFS explores one branch of the graph as deeply as possible before returning to explore other branches. This process is called backtracking.

**Working:**
1. Start from the initial node.
2. Insert it into a stack.
3. Remove the most recently added node.
4. Check whether it is the goal.
5. If not, add its unvisited neighbors to the stack.
6. Repeat until the goal is found or the stack becomes empty.

**Important points:**
- Uses a Stack (LIFO – Last In, First Out).
- Does not guarantee the shortest path.
- Can find a solution without exploring every level of the graph.

### 4. Graph Representation – Adjacency List

A graph consists of vertices (nodes) and edges (connections).

In our program, the graph is represented using a Python dictionary called `route_graph`.

For example:

```python
'A': ['B', 'C']
```

This means location A is directly connected to locations B and C.

An adjacency list stores the neighboring nodes of each vertex and provides an efficient way to represent a graph.

### 5. Evaluation Metrics

In this practical, BFS and DFS are compared using three evaluation parameters.

**A. Path Length**

Path length represents the number of edges or connections between the starting node and the destination.

Formula:

Path Length = Number of nodes in the path - 1

Example:
- BFS: A → C → F = 2 edges.
- DFS: A → B → E → F = 3 edges.

A shorter path means fewer connections are required to reach the destination.

**B. Nodes Explored**

Nodes explored represents the number of nodes processed by the algorithm before finding the goal.

In our program, the variable `nodes_explored` counts how many nodes are processed.

- BFS explores nodes level by level.
- DFS explores nodes by going deeper into a branch.

Fewer explored nodes may indicate less search work for a particular graph, but the result depends on the graph structure and neighbor ordering.

**C. Execution Time**

Execution time represents the time taken by an algorithm to find the destination.

Our program uses the Python `time` module:

```python
start_time = time.time()
```

The execution time is calculated by subtracting the starting time from the finishing time.

Execution Time = End Time - Start Time

It is measured in seconds.

A lower execution time indicates faster execution for that particular run. However, execution time can vary depending on system performance and graph size.

### 6. Performance Comparison – What Are We Actually Doing?

We start both algorithms from node A and set node F as the destination.

Both algorithms search the same graph, but use different search strategies.

| Evaluation Metric | BFS | DFS |
|---|---|---|
| Search strategy | Level by level | Depth first |
| Data structure | Queue | Stack |
| Path found | A → C → F | A → B → E → F |
| Path length | 2 edges | 3 edges |
| Nodes explored | 6 | 5 |
| Shortest path | Yes | Not guaranteed |

The results show that BFS finds a shorter route in this example, while DFS explores fewer nodes before finding its route.

The execution time is also measured to compare how quickly each algorithm completes the search.

**Note:** The execution-time values are very small because our graph contains only six nodes. Therefore, small differences in execution time should not be treated as proof that one algorithm is always faster.

### 7. Time and Space Complexity

Complexity describes the resources required by an algorithm as the input graph grows.

For graph traversal using an adjacency list:

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |

Where:
- V = Number of vertices (nodes).
- E = Number of edges (connections).

Time complexity represents the amount of computational work, while space complexity represents the additional memory required.

### 8. Practical Applications

- GPS navigation and route finding.
- Maze solving.
- Network traversal.
- Web crawling.
- Social network connections.
- Pathfinding in games and robotics.

### 9. Overall Understanding

The main objective of this practical is to understand how two uninformed search algorithms solve the same route-finding problem using different strategies.

BFS is preferred when the shortest path is required in an unweighted graph, whereas DFS is useful for exploring deeper branches.

By comparing path length, nodes explored and execution time, we understand the differences in their search performance.
