import heapq  # heapq for priority queue
import random

rows = 6
columns = rows

maze = []

# iterations
dfs_results = []
astar_results = []

for i in range(rows):
    row = []
    for j in range(columns):
        cell_value = i + j * rows
        row.append(cell_value)
    maze.append(row)

print("-------------------- Task 1 --------------------")
print("\n\tThe Maze")
for row in maze:
    print(row)


# funtion for getting (x, y) coordinates of a node
def get_coordi(node):
    for row_index, row in enumerate(maze):
        if node in row:
            col_index = row.index(node)
            return col_index, row_index


# repeat the code for three different random mazes
def itr():
    # start node
    start_node = random.randint(0, 11)
    start_coordi = get_coordi(start_node)
    print(f"Starting node: {start_node}")
    print(f"Coordinates: {start_coordi} \n")

    # goal node
    goal_node = random.randint(24, 35)
    goal_coordi = get_coordi(goal_node)
    print(f"Goal node: {goal_node}")
    print(f"Coordinates: {goal_coordi} \n")

    # barrier nodes
    all_nodes = [node for row in maze for node in row]
    available_nodes = list(set(all_nodes) - {start_node, goal_node})
    barrier_nodes = random.sample(available_nodes, 4)
    barrier_coordi = [get_coordi(node) for node in barrier_nodes]
    print(f"Barrier nodes: {barrier_nodes}")
    print(f"Coordinates: {barrier_coordi} \n")

    print("-------------------- Task 2 --------------------")

    # process neighbors function for DFS search
    def get_neighbors(node):
        x, y = get_coordi(node)
        neighbors = [
            maze[y][x - 1]
            if x > 0
            else None,  # Left
            maze[y][x + 1]
            if x < 5
            else None,  # Right
            maze[y - 1][x]
            if y > 0
            else None,  # Up
            maze[y + 1][x]
            if y < 5
            else None,  # Down
            maze[y - 1][x - 1]
            if x > 0 and y > 0
            else None,  # Up-Left
            maze[y - 1][x + 1]
            if x < 5 and y > 0
            else None,  # Up-Right
            maze[y + 1][x - 1]
            if x > 0 and y < 5
            else None,  # Down-Left
            maze[y + 1][x + 1]
            if x < 5 and y < 5
            else None  # Down-Right
        ]
        return [neighbor for neighbor in neighbors if neighbor is not None and neighbor not in barrier_nodes]

    # DFS function
    def dfs(current_node, visited, path):
        visited.append(current_node)
        if current_node == goal_node:
            return True

        for neighbor in sorted(get_neighbors(current_node)):
            if neighbor not in visited:
                if dfs(neighbor, visited, path):
                    path.append(current_node)
                    return True
        return False

    # perform DFS
    visit_dfs = []
    path_dfs = []

    dfs_start_time = 0
    if dfs(start_node, visit_dfs, path_dfs):
        dfs_start_time = len(visit_dfs)  # Each node takes 1 minute to explore
    dfs_results.append({'visited_nodes': visit_dfs, 'time_to_goal': dfs_start_time, 'path_length': len(path_dfs)})

    print(f"DFS Visited Nodes: {visit_dfs}")
    print(f"Time to find goal (DFS): {dfs_start_time} minutes")
    print(f"DFS Final Path: {path_dfs[::-1] + [goal_node]}")
    print(f"DFS Final Path: {len(path_dfs)} nodes\n")

    print("-------------------- Task 3 --------------------")

    # heuristic calculation using Manhattan distance
    def calculate_manhattan_distance(node, goal_coordi):
        node_coordi = get_coordi(node)
        return abs(node_coordi[0] - goal_coordi[0]) + abs(node_coordi[1] - goal_coordi[1])

    heuristic_cost = calculate_manhattan_distance(start_node, goal_coordi)
    print(f"Heuristic cost for node: {heuristic_cost}\n")

    print("-------------------- Task 4 --------------------")

    # A* search
    def astar_search():
        open_set = [(0, start_node)]  # priority queue with tuple
        closed_set = set()
        g_cost = {start_node: 0}
        parent = {start_node: None}

        while open_set:
            _, current_node = heapq.heappop(open_set)

            if current_node == goal_node:
                path_astar = [goal_node]
                while parent[current_node] is not None:
                    path_astar.append(parent[current_node])
                    current_node = parent[current_node]
                path_astar.reverse()
                return path_astar

            closed_set.add(current_node)

            for neighbor in get_neighbors(current_node):
                if neighbor in closed_set:
                    continue

                tentative_g_cost = g_cost[current_node] + 1
                if neighbor not in [node[1] for node in open_set] or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + calculate_manhattan_distance(neighbor, goal_coordi)
                    heapq.heappush(open_set, (f_cost, neighbor))
                    parent[neighbor] = current_node
        return []

    # perform A* search
    path_astar = astar_search()
    astar_start_time = len(path_astar) - 1  # find goal is the number of steps - 1
    astar_results.append({'visited_nodes': path_astar, 'time_to_goal': astar_start_time, 'path_length': len(path_astar)})

    print(f"A* Visited Nodes: {path_astar}")
    print(f"Time to find goal (A*): {astar_start_time} minutes")
    print(f"A* Final Path: {path_astar}\n")
    print(f"A* Final Path: {len(path_astar)} nodes")

    # calculate mean and variance for solution time
    def calculate_mean_variance_time(data):
        values = [result['time_to_goal'] for result in data]
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return mean, variance

    # calculate mean and variance for path length
    def calculate_mean_variance_length(data):
        values = [result['path_length'] for result in data]
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return mean, variance


    # DFS Mean and Variance for solution time
    dfs_mean, dfs_variance = calculate_mean_variance_time(dfs_results)
    print(f"DFS Mean Time: {dfs_mean} minutes")
    print(f"DFS Variance Time: {dfs_variance}\n")

    # DFS Mean and Variance for length
    dfs_mean_length, dfs_variance_length = calculate_mean_variance_length(dfs_results)
    print(f"DFS Mean Length: {dfs_mean_length} size")
    print(f"DFS Variance Length: {dfs_variance_length}\n")

    # A* Mean and Variance for solution time
    astar_mean, astar_variance = calculate_mean_variance_time(astar_results)
    print(f"A* Mean Time: {astar_mean} minutes")
    print(f"A* Variance Time: {astar_variance}\n")

    # A* Mean and Variance for length
    astar_mean_length, astar_variance_length = calculate_mean_variance_length(astar_results)
    print(f"A* Mean Length: {astar_mean_length} size")
    print(f"A* Variance Length: {astar_variance_length}\n")

itr()
print("-------------------- Task 5 --------------------")
attempt = 1
while attempt != 4:
    print("|||||||||||||||||| Attempt", attempt, "||||||||||||||||||")
    itr()
    attempt += 1