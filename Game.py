import constants
import random


class Game:
    def __init__(self):
        self.width = round(constants.GAME_WIDTH / constants.CELL_WIDTH)
        self.height = round(constants.GAME_HEIGHT / constants.CELL_WIDTH)

        self.cells = []
        self.init_cells()

    def init_cells(self):

        for numberX in range(self.width):
            line = []
            for numberY in range(self.height):
                line.append(0 if random.random() > 0.3 else 1)
            self.cells.append(line)

    def step(self):
        result = []
        newState = []

        for numberX in range(self.width):
            newLine = []
            for numberY in range(self.height):
                current_state = self.cells[numberX][numberY]
                count_neighbour = 0
                neighbour_left = numberX - 1 if numberX - 1 > 0 else self.width - 1
                neighbour_right = numberX + 1 if numberX + 1 < self.width else 0
                neighbour_top = numberY - 1 if numberY - 1 > 0 else self.height - 1
                neighbour_down = numberY + 1 if numberY + 1 < self.height else 0

                count_neighbour += self.cells[neighbour_left][neighbour_down]
                count_neighbour += self.cells[neighbour_left][numberY]
                count_neighbour += self.cells[neighbour_left][neighbour_top]
                count_neighbour += self.cells[numberX][neighbour_top]
                count_neighbour += self.cells[neighbour_right][neighbour_top]
                count_neighbour += self.cells[neighbour_right][numberY]
                count_neighbour += self.cells[neighbour_right][neighbour_down]
                count_neighbour += self.cells[numberX][neighbour_down]

                result.append([current_state, count_neighbour])

                if current_state == 1 and 1 < count_neighbour < 4:
                    newLine.append(1)
                elif current_state == 0 and count_neighbour == 3:
                    newLine.append(1)
                else:
                    newLine.append(0)
            newState.append(newLine)

        self.cells = newState
