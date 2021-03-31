import time
import os
from math import floor
import keyboard
from random import random

class Snake:
    def __init__(self, SIZE, apple_rate, time_step):
        # SIZE = 30 # Must be even so we don't need to use floor
        self.n = SIZE
        self.p = apple_rate
        self.t = time_step 
        self.snake = [[floor(SIZE/2 -1), floor(SIZE/2 - 1)]]
        self.direction = (1,0)
        self.board = [['_' for _ in range(SIZE)] for _ in range(SIZE)]
        self.apples = []

    def show_board(self):
        os.system('clear')
        b = [[cell for cell in row] for row in self.board]
        for a in self.apples:
            b[a[0]][a[1]] = '*'
        for s in self.snake:
            b[s[0]][s[1]] = '#'
        for row in b:
            print(*row, flush=True)

    def step_board(self):
        # Move the snake
        print(self.snake)
        new_head =  ((self.snake[-1][0] + self.direction[0]) % self.n , (self.snake[-1][1] + self.direction[1]) % self.n)
        if new_head in self.snake[1:]:
            raise Exception("Game Over: Ran into tail! "+len(self.snake))
        print(new_head)
        print(self.apples)
        if new_head in self.apples:
            self.snake = self.snake + [new_head]
            self.apples = [a for a in self.apples if a != new_head]
            return
        self.snake = self.snake[1:] + [new_head]

    def make_apples(self):
        if random() < self.p and len(self.apples) < 4:
            new_apple = (floor(random()*self.n),floor(random()*self.n))
            while(new_apple in self.snake):
                new_apple = (floor(random()*self.n),floor(random()*self.n))
            self.apples += [new_apple]
    
    def level(self):
        speed = 0
        for i in range(len(self.snake)):
            if i < 5:
                speed += 0.03
            elif i < 10:
                speed += 0.02
            elif i < 20:
                speed += 0.01

        return max(self.t - speed, 0.02)


    def game_loop(self): 
        def handle_press(key):
            if(key.scan_code == 103):
                self.direction = (-1,0)
            elif(key.scan_code == 108 ):
                self.direction = (1,0)
            elif(key.scan_code == 105):
                 self.direction = (0,-1)
            elif(key.scan_code == 106):
                self.direction = (0,1)
        keyboard.on_press(handle_press)
        while(True):
            self.step_board()
            self.show_board()
            self.make_apples()
            time.sleep(self.level())

def main():
    s = Snake(30, 0.1, 0.5)
    s.game_loop()

if __name__ == "__main__":
    main()

            
