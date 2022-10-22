import pygame
import sys
import solver

#default board
board = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

#start pygame
pygame.init()

#solver window
window = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Sudoku Solver")

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#solver font
font = pygame.font.SysFont("Arial", 48)

#game board 3x3
def drawBoard():
    for x in range(0, 450, 150):
        for y in range(0, 450, 150):
            pygame.draw.rect(window, BLACK, (x, y, 150, 150), 2)
    for x in range(0, 450, 50):
        for y in range(0, 450, 50):
            pygame.draw.rect(window, BLACK, (x, y, 50, 50), 1)

#draw numbers that are set
def drawNumbers():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                window.blit(text, (j*50+13, i*50))

#draw solution
def drawSolvedNumbers():
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, GREEN)
                window.blit(text, (j*50+13, i*50))

#main game loop
def main():
    window.fill(WHITE)
    drawBoard()
    drawNumbers()
    pygame.display.update()
    #main game loop
    while True:
        for event in pygame.event.get():

            #close solver
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #mouse press
            if event.type == pygame.MOUSEBUTTONDOWN:

                #left click
                if event.button == 1:
                    drawNumbers()
                    #get row col position
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // 50
                    row = pos[1] // 50
            
                    #click unfilled box
                    if board[row][column] == 0:
                        #fill box with 1
                        board[row][column] = 1
                        text = font.render(str(board[row][column]), True, BLUE)
                        window.blit(text, (column*50+13, row*50))
                        pygame.display.update()

                    #click filled box
                    else:
                        #increase by 1
                        board[row][column] += 1
                        #if greater than 9
                        if board[row][column] > 9:
                         board[row][column] = 1
                        window.fill(WHITE)
                        drawBoard()
                        drawNumbers()
                        pygame.display.update()
                        text = font.render(str(board[row][column]), True, BLUE)
                        window.blit(text, (column*50+13, row*50))
                        pygame.display.update()
                
                #right click
                if event.button == 3:
                    drawNumbers()
                    #get row col position
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // 50
                    row = pos[1] // 50
            
                    #click unfilled box
                    if board[row][column] == 0:
                        #fill box with 9
                        board[row][column] = 9
                        text = font.render(str(board[row][column]), True, BLUE)
                        window.blit(text, (column*50+13, row*50))
                        pygame.display.update()

                    #click filled box
                    else:
                        #decrease by 1
                        board[row][column] -= 1
                        #if less than 1
                        if board[row][column] < 1:
                         board[row][column] = 9
                        window.fill(WHITE)
                        drawBoard()
                        drawNumbers()
                        pygame.display.update()
                        text = font.render(str(board[row][column]), True, BLUE)
                        window.blit(text, (column*50+13, row*50))
                        pygame.display.update()

            #key press
            if event.type == pygame.KEYDOWN:

                #enter pressed
                if event.key == pygame.K_RETURN:
                   #if board is valid solve
                    if solver.checkBoard(board):
                        solver.solve(board)
                        window.fill(WHITE)
                        drawBoard()
                        drawSolvedNumbers()
                        pygame.display.update()

                    #if the board is not valid throw error
                    else:
                        #open error window
                        errorWindow = pygame.display.set_mode((300, 100))
                        pygame.display.set_caption("Error")
                        errorWindow.fill(WHITE)
                        errorText = font.render("Invalid Board", True, RED)
                        errorWindow.blit(errorText, (10, 10))
                        pygame.display.update()

                        #wait for window to be closed
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()

                #delete pressed
                if event.key == pygame.K_BACKSPACE:

                    #clear the board
                    for i in range(9):
                        for j in range(9):
                            board[i][j] = 0
                    window.fill(WHITE)
                    drawBoard()
                    drawNumbers()
                    pygame.display.update()
    
#call the main function
main()
