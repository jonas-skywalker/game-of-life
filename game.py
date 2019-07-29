"""
Python script to simulate conways game of life
Things to add:
    user interaction
"""
import pygame
import time
import random
pygame.init()

size = 800, 800
spawn_probability = 16
screen = pygame.display.set_mode(size)

# colors
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

square_size = 10, 10

squares = []


class Square:
    square_num = 0
    # boolean to check if square is populated
    is_pop = False
    # positions of the square
    pos_x = 0
    pos_y = 0
    rect = (pos_x, pos_y), square_size

    def draw(self, posx, posy, num):
        self.square_num = num
        self.rect = (posx, posy), square_size
        rand_int = random.randint(0, spawn_probability)
        if rand_int == 1:
            pygame.draw.rect(screen, green, self.rect, 0)
            self.is_pop = True
        else:
            pygame.draw.rect(screen, black, self.rect, 0)
            self.is_pop = False

    def update(self):
        # print("Updating: " + str(self.square_num))
        if self.is_pop:
            # make square green
            # print("this should happen")
            pygame.draw.rect(screen, green, self.rect, 0)
        else:
            pygame.draw.rect(screen, black, self.rect, 0)

    def check_neighbour(self):
        neighbour_count = 0
        # please make this a function
        try:
            if squares[int(self.square_num - (size[0]/10))].is_pop and 0 < int(self.square_num - (size[0]/10)) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num - ((size[0]/10) - 1))].is_pop and 0 < int(self.square_num - ((size[0]/10) - 1)) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num - ((size[0]/10) + 1))].is_pop and 0 < int(self.square_num - ((size[0]/10) + 1)) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num + (size[0]/10))].is_pop and 0 < int(self.square_num + (size[0]/10)) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num + ((size[0]/10) - 1))].is_pop and 0 < int(self.square_num + ((size[0]/10) - 1)) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num + ((size[0]/10) + 1))].is_pop and 0 < int(self.square_num + ((size[0]/10) + 1)) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num + 1)].is_pop and 0 < int(self.square_num + 1) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass
        try:
            if squares[int(self.square_num - 1)].is_pop and 0 < int(self.square_num - 1) < len(squares):
                neighbour_count += 1
        except IndexError:
            pass

        if self.is_pop:
            # underpopulation
            if neighbour_count < 2:
                self.is_pop = False
            # right population
            if neighbour_count == 2 or neighbour_count == 3:
                self.is_pop = True
            # over population
            if neighbour_count > 3:
                self.is_pop = False
        else:
            if neighbour_count == 3:
                self.is_pop = True

        # print("Checked square: " + str(self.square_num))
        # print(neighbour_count)


def main():
    # main function that initializes the chaos game
    pygame.display.set_caption("Game of Life")
    screen.fill(white)

    # generate list of objects
    for i in range(int((size[0]/square_size[0]) * (size[1]/square_size[0]))):
        object1 = Square()
        squares.append(object1)

    # draw the objects
    count = 0
    for x in range(0, size[0], 10):
        for y in range(0, size[1], 10):
            squares[count].draw(x, y, count)
            # print(x, y, count)
            count += 1
    """
    for square in squares:
        if square.pos_x < 100 or square.pos_x > 700:
            if square.pos_y < 100 or square.pos_x > 700:
                square.is_pop = False
        square.update()
    """


if __name__ == '__main__':
    main()


while True:
    # function for Pygame updating the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    for i in range(len(squares)):
        squares[i].check_neighbour()
    for i in range(len(squares)):
        squares[i].update()
        # print(squares[i].is_pop)
    time.sleep(0)
