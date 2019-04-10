import pygame, sys, random

w = 600
h = 600

pygame.init()
screen = pygame.display.set_mode((w, h))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()

frameRate = 10
resolution = 10

# board = [["0000000000000000000000001"]
# ["0000000000000000000000101"]
# ["000000000000110000001100000000000011"]
# ["000000000001000100001100000000000011"]
# ["1100000000100000100011"]
# ["1100000000100010110000101"]
# ["0000000000100000100000001"]
# ["0000000000010001"]
# ["00000000000011"]]

cols = int(w / resolution)
rows = int(h / resolution)
board = [[None for i in range(cols)] for j in range(rows)]
rect = [[None for i in range(cols)] for j in range(rows)]

def randomizeCells():
    for i in range(cols):
        for j in range(rows):
            board[i][j] = random.randint(0, 1)
randomizeCells()

def drawCells():
    global rect
    for i in range(cols):
        for j in range(rows):
            x = i * resolution
            y = j * resolution
            if board[i][j] == 1:
                rect[i][j] =  pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, x+resolution, y+resolution))  
            else:
                rect[i][j] =  pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, x+resolution, y+resolution))  
                
def countNeighbors(board, x, y):
    sum = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows
            sum += board[col][row]
    sum -= board[x][y]
    return sum

def draw():
    global board
    drawCells()
    nextGeneration = [[None for i in range(cols)] for j in range(rows)]
    for i in range(cols):
        for j in range(rows):
            state = board[i][j]
            neighbors = countNeighbors(board, i, j)
            if state == 0 and neighbors == 3:
                nextGeneration[i][j] = 1
            elif state == 1 and neighbors < 2 or neighbors > 3:
                nextGeneration[i][j] = 0
            else:
                nextGeneration[i][j] = state
    board = nextGeneration

while True:
    clock.tick(frameRate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    draw()
    pygame.display.flip()
