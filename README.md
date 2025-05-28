# 🧩 Maze Solver in Python

A terminal-based maze solver implemented in Python that reads mazes from text files and solves them using **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** algorithms.

---

## 📁 Project Structure

```
maze-solver/
├── maze.py         # Main program with all classes and logic
├── maze.txt        # Maze file (input)
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
3. Run the program from the terminal:

```bash
python maze.py
```

The solution will be printed directly in the terminal using Unicode blocks for walls and asterisks for the path.

---

## ✅ Output Symbols

| Symbol | Meaning |
|--------|---------|
| `A` | Start position |
| `B` | Goal position |
| `█` | Wall |
| `*` | Solution path |
| (space) | Walkable path |

---

## 🧠 How It Works

The program includes the following components:

### 🔹 Node
A class to represent each state in the maze, including the path taken to reach it.

### 🔹 StackFrontier (DFS)
Implements a stack-based frontier for **Depth-First Search**.

### 🔹 QueueFrontier (BFS)
Extends `StackFrontier` with queue behavior for **Breadth-First Search**.

### 🔹 Maze
- Reads the maze from file
- Finds neighbors of a cell
- Solves the maze using a chosen frontier
- Prints the maze and solution

---

## ✨ Optional Enhancements

- ✅ Animate solving with `time.sleep()`
- ✅ Use full Unicode blocks (`█`) for wall rendering
- 🔄 Highlight explored nodes
- 💡 Add A* or Dijkstra's algorithm
- 🎨 Use colored output with ANSI codes

---

## 🔧 Requirements

- Python 3.x
- No external libraries needed

---

## 🧑‍💻 Author

A Computer Science student exploring AI, algorithms, and game development. Feel free to contribute or fork the project!

---
