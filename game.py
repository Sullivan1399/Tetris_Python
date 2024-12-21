from grid import Grid
from blocks import *
import random, pygame, time

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), LBlock(), JBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.velx = 0
        self.vely = 0
        self.game_over = False
        self.score = 0

    def update_score(self, lines_cleared, move_down_points):
        score_board = {
            0: 0,
            1: 100,
            2: 300,
            3: 500,
            4: 800
        }
        self.score += move_down_points
        self.score += score_board[lines_cleared] 
        
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), LBlock(), JBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)  
        self.blocks.remove(block)
        return block  # Return object

    def update(self):
        self.current_block.col_offset += self.velx
        self.current_block.row_offset += self.vely
        time.sleep(0.1)
        # check bounds
        if self.block_inside() == False or self.block_fits() == False:
            # out of bounds, undo movement
            self.current_block.col_offset -= self.velx
            self.current_block.row_offset -= self.vely

    def stop(self):
        self.velx = 0
        self.vely = 0

    def reset(self):
        self.grid.reset()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def move_left(self):
        # self.current_block.move(0, -1)
        self.velx -= 1
        # if self.block_inside() == False:
        #     self.current_block.move(0, 1)

    def move_right(self):
        # self.current_block.move(0, 1)
        self.velx += 1
        # if self.block_inside() == False:
        #     self.current_block.move(0, -1)

    def move_down(self): 
        # self.current_block.move(1, 0)
        self.vely += 1
        # if self.block_inside() == False:
        #     self.current_block.move(-1, 0)
    
    def drop_down(self): 
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        row_cleared = self.grid.clear_full_rows()
        self.update_score(row_cleared, 1)
        if self.block_fits() == False:
            self.game_over = True

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.col) == False:
                return False
        return True
        
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotate()
    
    def drop_now(self):
        for i in range(20):
            self.current_block.move(i, 0)
            if self.block_inside() == False or self.block_fits() == False:
                self.current_block.move(-1, 0)
                self.lock_block()
                break
            self.current_block.move(-i, 0)

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.col) == False:
                return False
        return True
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)