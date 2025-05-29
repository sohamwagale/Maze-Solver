import sys
import os

class Node():
    def __init__(self, state,parent, action,mandis,cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = mandis
        self.cost = cost

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self,node):
        self.frontier.append(node) # last la add hotay mhanun last pasun cha kadhaycha

    def contains_state(self,state):
        return any(node.state == state for node in self.frontier)  # seld.frontier madhe node store kelelea ahet
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else: 
            last_node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return last_node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else: 
            front_node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return front_node

class Maze():

    #class variables
    #contents   lsit of strings
    #height   int
    #width  int
    #walls   list of lists named row boolean
    #solution   tuple(actions,cells)   actions-> list of strings   cells->list of states (coordinates)
    #start   tuple(i,j)    coordinates 
    #state   ->   coordinate
    #explored -> list of coordinates
    #frontier -> list of data type Nodes


    def __init__(self,file_name):
        with open(file_name) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("Only one starting point 'A'")
        if contents.count("B") != 1:
            raise Exception("Only one ending point 'B'")
        
        contents = contents.splitlines() # contents is now an array split into rows
        self.height = len(contents) # height 
        self.width = max(len(line) for line in contents)  # len of maximum line is width

        # keeping track of walls
        self.walls = []    # walls is a list of lists of rows all with "True" for wall and "False" for not wall
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None   # set solution as none
        
    def print(self):
        # soltion is the set of cells where the desired path is 
        solution_cells = self.solution[1] if self.solution is not None else None
        print()
        for i,row in enumerate(self.walls):
            for j,cols in enumerate(row):    #i,j just to remember the coordinates
                if cols:
                    print("\u2588", end = "")
                elif (i,j) == self.start:
                    print("A", end ="")
                elif (i,j) == self.goal:
                    print("B", end = "")
                elif self.solution is not None and (i,j) in solution_cells:
                    print("*", end="") #prints the solution path
                else:
                    print(" ", end="")
            print()
        print()

    def neighbours(self, state): # returns list of neighbouring possible coordinates      
        # neigtbours of the node NOT of the coordinate
        
        row, col = state
        candidates = [ #candidates for the upcomming states
            ("left",(row,col -1)),
            ("right",(row,col+1)), #("Action",(state))
            ("up",(row-1,col)),
            ("down",(row+1,col))
        ]
        
        result = []
        for action, (r,c) in candidates:# result vaild ahe ka nahi check kela jatay
            if 0 <= r < self.height and 0<= c < self.width and not self.walls[r][c]:    # ek ek coordinate karun pudha jatay ekekta
                result.append((action,(r,c)))
        return result
    
    def solve(self,algo):
        self.num_explored = 0 #num of states explored

        #start node is created
        start = Node(state=self.start,parent=None, action=None,mandis=abs(self.goal[0]-self.start[0])+abs(self.goal[1]-self.start[1]),cost=0)  # State is set to the coordinate of the start state
        
        if(algo == 1):
            frontier = StackFrontier()
        elif(algo == 2):
            frontier = QueueFrontier()
        elif(algo == 3):
            frontier = QueueFrontier()
        elif(algo==4):
            frontier= QueueFrontier()
        else:
            frontier=StackFrontier()


        frontier.add(start)

        self.explored = set()

        while True:

            if frontier.empty():
                raise Exception("Frontier is empty, No solution exists !")
            
            if(algo == 3):
                frontier.frontier = sorted(frontier.frontier, key=lambda node : node.heuristic)
            elif(algo == 4):
                frontier.frontier = sorted(frontier.frontier, key=lambda node : node.heuristic + node.cost)
            curr_node = frontier.remove()

            self.num_explored +=1

            if curr_node.state == self.goal:  # store all the info of the answer in solution
                actions = []
                cells = []

                while curr_node.parent is not None:
                    actions.append(curr_node.action)
                    cells.append(curr_node.state)
                    curr_node = curr_node.parent
                
                actions.reverse()
                cells.reverse()

                self.solution = (actions, cells)
                return
            
            self.explored.add(curr_node.state)

            for action, curr_state in self.neighbours(curr_node.state):   # Sagle child nodes create karun te frontier madhe add karat jaycha 
                if not frontier.contains_state(curr_state) and curr_state not in self.explored:   # jar already add nasle tar ch
                    mandis = (
                        abs(self.goal[0]-curr_state[0])+
                        abs(self.goal[1]-curr_state[1])
                    )
                    child = Node(state = curr_state, parent = curr_node, action = action,mandis=mandis,cost=curr_node.cost+1)     # navin node create karun and tyacha parent current node mhanun
                    frontier.add(child)
    
    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
        os.makedirs("images", exist_ok=True)
        img.save(f"images/{filename}")

if len(sys.argv) !=2:
    sys.exit("Usage: python main.py maze.txt")

def diff_algo(algo,maize):
    if(algo == 1):
        algon = "BFS"
    elif(algo == 2):
        algon = "DFS"
    elif(algo == 3):
        algon = "GBFS"
    elif(algo == 4):
        algon = "A-star"
    else:
        algon = "_"

    print(f"Solving Maze using {algon}")
    maize.solve(algo)
    print("Stated Explored : ",maize.num_explored)
    print("Solution : ")
    maize.print()
    maize.output_image(f"{algon.lower()}_maze_solution.png", show_explored=True)

def main(algo):
    maize = Maze(sys.argv[1])
    print("Maze: ")
    maize.print()
    if(algorithm!=5):
        diff_algo(algorithm,maize)
    else:
        diff_algo(algo=1,maize=maize)
        diff_algo(algo=2,maize=maize)
        diff_algo(algo=3,maize=maize)
        diff_algo(algo=4,maize=maize)

if __name__ == "__main__":
    algorithm = int(input("Enter the algorithm \n1->DFS \n2->BFS \n3->GBFS\n4->A*\n5->All\n"))
    main(algorithm)