import sys, time

class Map:
    def __init__(self):
        self.map = [["*","*","*","*"],
                    ["*","*","*","*"],
                    ["*","*","*","*"],
                    ["*","*","*","*"]]
        self.solution = [(0,0)]

    def print_display(self):
        for row in self.map:
            for cell in row:
                print(f"{cell} ", end='')
            print()
    
    def print_solution(self):
        sol_map = [["*","*","*","*"],
                   ["*","*","*","*"],
                   ["*","*","*","*"],
                   ["*","*","*","*"]]
        for act in self.solution:
            sol_map[act[0]][act[1]] = "#"
            for row in sol_map:
                for cell in row:
                    print(f"{cell} ", end='')
                print()
            time.sleep(0.5)
            LINE_UP = '\033[1A'
            LINE_CLEAR = '\x1b[2K'
            for row in sol_map:
                print(LINE_UP, end=LINE_CLEAR)
            if act  == (0,0):
                sol_map[act[0]][act[1]] = "*"

    def move(self, next_cell):
        if next_cell != (0,0):
            self.map[next_cell[0]][next_cell[1]] = "#"
        self.solution.append(next_cell)
    
    def backtrack(self, current_cell):
        self.solution.pop()
        self.map[current_cell[0]][current_cell[1]] = "*"

    def SolveProblem(self):
        if self.map == [["*","#","#","#"],
                        ["#","#","#","#"],
                        ["#","#","#","#"],
                        ["#","#","#","#"]]:
            # print(self.solution)
            self.print_solution()
        
        current_cell = self.solution[-1]
        left = (current_cell[0], current_cell[1]-1)
        down = (current_cell[0]+1, current_cell[1])
        right = (current_cell[0], current_cell[1]+1)
        up = (current_cell[0]-1, current_cell[1])

        # check move to left
        if current_cell[1] != 0 and self.map[left[0]][left[1]] == "*":
            self.move(left)
            self.SolveProblem()
            self.backtrack(left)

        # check move to down
        if current_cell[0] != 3 and self.map[down[0]][down[1]] == "*":
            if down != (3,3) or self.map == [["*","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","*"]]:
                self.move(down)
                self.SolveProblem()
                self.backtrack(down)

        # check move to right
        if current_cell[1] != 3 and self.map[right[0]][right[1]] == "*":
            if right != (3,3) or self.map == [["*","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","*"]]:
                self.move(right)
                self.SolveProblem()
                self.backtrack(right)

        # check move to up
        if current_cell[0] != 0 and self.map[up[0]][up[1]] == "*":
            self.move(up)
            self.SolveProblem()
            self.backtrack(up)


if __name__ == "__main__":
    map = Map()
    map.SolveProblem()