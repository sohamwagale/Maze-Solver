# 🧩 Maze Solver in Python

A comprehensive maze solver implemented in Python that reads mazes from text files and solves them using multiple search algorithms including **DFS**, **BFS**, **Greedy Best-First Search (GBFS)**, and **A* Search**.

---

## 📁 Project Structure

```
maze-solver/
├── maze.py         # Main program with all classes and logic
├── maze.txt        # Maze file (input)
├── images/         # Generated solution images (created automatically)
└── README.md       # Documentation
```

---

## 📌 Maze Format

Each maze is stored in a `.txt` file using the following characters:

- `A` → Start point (must appear exactly once)
- `B` → Goal point (must appear exactly once)  
- Space (` `) → Walkable path
- Any other character (e.g., `#`) → Wall

### Example (`maze.txt`):

```
########
#A     #
# #### #
#    B #
########
```

---

## 🚀 How to Run

1. Save your maze in a file named `maze.txt`
2. Make sure Python 3 is installed
3. Install required dependencies:
   ```bash
   pip install Pillow
   ```
4. Run the program from the terminal:
   ```bash
   python maze.py maze.txt
   ```
5. Choose your algorithm:
   - `1` → Depth-First Search (DFS)
   - `2` → Breadth-First Search (BFS) 
   - `3` → Greedy Best-First Search (GBFS)
   - `4` → A* Search
   - `5` → Run all algorithms for comparison

The solution will be printed in the terminal and saved as PNG images in the `images/` folder.

---

## 📊 Output Features

The program provides both **terminal visualization** and **PNG image generation**:

### Terminal Output
| Symbol | Meaning |
|--------|---------|
| `A` | Start position |
| `B` | Goal position |
| `█` | Wall |
| `*` | Solution path |
| (space) | Walkable path |

### PNG Images
- **Black**: Walls
- **Red**: Start position  
- **Green**: Goal position
- **Yellow**: Solution path
- **Light Red**: Explored nodes (when enabled)
- **Light Blue**: Empty walkable cells

Images are automatically saved in the `images/` folder with algorithm-specific names.

---

## 🧠 How It Works

The program implements several search algorithms following this general approach:

### 🔄 Search Algorithm Framework
1. **Start** with a frontier containing the initial state
2. **Initialize** an empty explored set
3. **Repeat** until solution found:
   - If frontier is empty → no solution exists
   - Remove a node from the frontier:
     - **Stack (DFS)**: Latest added node explored first → deepest nodes searched first
     - **Queue (BFS)**: Oldest added node explored first → shallowest nodes searched first
     - **Priority Queue (GBFS/A*)**: Node with best heuristic/cost explored first
   - If node contains goal state → return solution
   - Add the node to the explored set
   - Expand node, add resulting nodes to frontier if not already explored

### 🔹 Core Components

**Node**  
Represents each state in the maze with position, parent, action, heuristic value, and path cost.

**StackFrontier (DFS)**  
Implements stack-based frontier for Depth-First Search - explores deepest paths first.

**QueueFrontier (BFS)**  
Extends StackFrontier with queue behavior for Breadth-First Search - explores shallowest paths first.

**Maze**  
- Reads maze from file and validates start/goal positions
- Finds valid neighbors for each cell
- Implements all search algorithms with heuristic calculations
- Generates both terminal output and PNG visualizations

### 🧭 Search Algorithms

**DFS (Depth-First Search)**  
Explores as far as possible along each branch before backtracking. May not find optimal solution.

**BFS (Breadth-First Search)**  
Explores all nodes at current depth before moving deeper. Guarantees shortest path in unweighted graphs.

**GBFS (Greedy Best-First Search)**  
Uses Manhattan distance heuristic to prioritize nodes closer to goal. Fast but not guaranteed optimal.

**A* Search**  
Combines actual path cost with heuristic estimate (f = g + h). Guarantees optimal solution with admissible heuristic.

---

## ✨ Features

- ✅ **Multiple algorithms**: DFS, BFS, GBFS, A*
- ✅ **Visual PNG output** with color-coded paths
- ✅ **Performance comparison** across all algorithms  
- ✅ **Heuristic-based search** (Manhattan distance)
- ✅ **Explored nodes visualization**
- 🔄 **Potential enhancements**:
  - Real-time solving animation
  - Custom heuristic functions
  - Diagonal movement support
  - Interactive maze editor

---

## 🔧 Requirements

- **Python 3.x**
- **Pillow (PIL)** - for PNG image generation
  ```bash
  pip install Pillow
  ```

## 📈 Performance Comparison

When you select option `5`, the program runs all algorithms and displays:
- Number of states explored by each algorithm
- Visual comparison of solution paths
- Performance differences between algorithms

This helps understand the trade-offs between different search strategies.

---

## 🧑‍💻 Author

A Computer Science student exploring AI, algorithms, and game development. Feel free to contribute or fork the project!

---

## 📜 License

This project is licensed under the MIT License.
