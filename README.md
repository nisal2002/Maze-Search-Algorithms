b) The (x, y) coordinates of each node are defined by the column and the rowshown at the top and left of the maze, respectively. For example, node 15 has(x, y) coordinates (2, 3).
c) Randomly select a node within the 0-11 nodes as the stating node. For example, node 8 is the starting node for the above maze.
d) Randomly select a node within the 24-35 nodes as the goal node. For example, node 27 is the goal node for the above maze.
e) Randomly select four barrier nodes from the remaining 34 nodes in the maze. For example, nodes 6, 19, 22 and 31 are the barrier node in the above maze.

f) Process neighbors in increasing order. For example, if processing theneighbors of node 8 , first process 2, then 7, then 9, then 14.
g) Only valid moves are going horizontal, vertical and diagonal.
h) No moves are allowed through the barrier nodes.
i) It takes 1 minute to explore a single node. The time to find the goal will be the sum of all nodes explored, not just the length of the final path.
j) All edges have equal costs for traversal.

k) Develop a function to calculate the heuristic cost for each node using the Manhattan distance.
d(N, G) = |Nx - Gx| + |Ny - Gy|
l) Where, d(N, G) is the Manhattan distance from the node N to Goal node and the (Nx, Ny) are the node N coordinates and the (Gx, Gy) are the Goal nodecoordinates

m) Using the heuristic cost calculated in Task 3, perform A* search and output the visited nodes list, time to find the goal and the final path. 
n) Repeat the above for three different random mazes.
