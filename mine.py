import pygame
import random

BOMB_NUMBER = 10

class MineSweeperCell:
    value: int
    is_mine: bool = False

    def __init__(self, value: int) -> None:
        self.value = value

    def show(self) -> int:
        self.revealed = True
        return self.value

def create_grid(grid_cells_width: int = 10, grid_cells_height: int = 10, bomb_count: int = 10):
    assert bomb_count < grid_cells_height * grid_cells_width, "Bomb count cannot excceed grid size." # type: ignore
    
    new_grid: list[list] = []

    for x in range(grid_cells_width):
        new_grid.append([])
        for y in range(grid_cells_height):
            new_grid[x].append(0)

    created_bomb_count = 0

    while created_bomb_count < bomb_count:
        new_bomb_coordinate_x = random.randint(0, grid_cells_width - 1)
        new_bomb_coordinate_y = random.randint(0, grid_cells_height - 1)
        if not type(new_grid[new_bomb_coordinate_x][new_bomb_coordinate_y]) == MineSweeperCell:
            new_grid[new_bomb_coordinate_x][new_bomb_coordinate_y] = MineSweeperCell(BOMB_NUMBER)
            created_bomb_count += 1
    
    print(new_grid)

create_grid()