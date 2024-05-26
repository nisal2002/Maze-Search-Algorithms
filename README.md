# Maze Search Algorithms

This repository contains a Python implementation of two search algorithms (Depth First Search (DFS) and A*) for finding the shortest path in a six-by-six maze. The application includes the setup of a random maze with barriers and performs searches to find the path from a starting node to a goal node.

## Objective

The objective of this coursework is to implement DFS and A* algorithms to find the shortest path in a maze, and to compare their performance in terms of completeness, optimality, and time complexity.

## Features of the System

1. **Setup Maze**:
    - Randomly select a starting node from nodes 0-11.
    - Randomly select a goal node from nodes 24-35.
    - Randomly select four barrier nodes from the remaining nodes.

2. **Perform DFS Search**:
    - Output the list of visited nodes.
    - Calculate and output the time to find the goal.
    - Output the final path found.

3. **Perform A* Search**:
    - Calculate heuristic cost using Manhattan distance.
    - Output the list of visited nodes.
    - Calculate and output the time to find the goal.
    - Output the final path found.

4. **Repeat Searches**:
    - Perform DFS and A* search on three different random mazes.
    - Analyze the results in terms of completeness, optimality, and time complexity.
    - Report the mean and variance of the solution time and path length.

## Maze Setup

The maze is a 6x6 grid with the following rules:
- The (x, y) coordinates of each node are defined by the column and row.
- Random starting node within nodes 0-11.
- Random goal node within nodes 24-35.
- Four randomly selected barrier nodes from the remaining nodes.

## Implementation Details

### Task 1: Setup Maze

- Define the maze with nodes and coordinates.
- Randomly select starting node, goal node, and barrier nodes.

### Task 2: Perform DFS Search

- Implement DFS algorithm considering valid moves (horizontal, vertical, diagonal) and avoiding barrier nodes.
- Process neighbors in increasing order.
- Calculate time to find the goal and output visited nodes list and final path.

### Task 3: Calculate Heuristic Cost

- Develop a function to calculate the heuristic cost for each node using Manhattan distance.
- Example:
  ```plaintext
  h(8, G) = |4 - 1| + |3 - 2| = 4
  ```

### Task 4: Perform A* Search

- Implement A* algorithm using the heuristic cost calculated in Task 3.
- Output visited nodes list, time to find the goal, and final path.

### Task 5: Repeat Searches and Analyze Results

- Repeat DFS and A* searches on three different random mazes.
- Analyze and compare the results for completeness, optimality, and time complexity.
- Report mean and variance of solution time and path length.

## Project Structure

- **main.py**: The main Python file containing the implementation of the maze search algorithms.

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nisal2002/Maze-Search-Algorithms.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Maze-Search-Algorithms
   ```

3. **Run the Python program:**

   ```bash
   python main.py
   ```

   The program will execute the setup of the maze, perform DFS and A* searches, and output the required results.

## Technologies Used

- Python

## Author

- [Author](nisal2002) - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
