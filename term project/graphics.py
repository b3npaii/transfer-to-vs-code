from cmu_graphics import *
from game import *
from minimaxPlayer import *

def onAppStart(app):
    app.width = 500
    app.height = 500
    app.rows = 8
    app.cols = 8
    app.boardLeft = 50
    app.boardTop = 50
    app.boardWidth = 400
    app.boardHeight = 400
    app.cellBorderWidth = 2
    app.board = [([None] * app.cols) for row in range(app.rows)]
    for i in range(0, 8):
        for j in range(0, 8):
            if i % 2 == j % 2:
                app.board[i][j] = ["white"]
            else:
                app.board[i][j] = ["black"]
    app.inGame = False
    newGame = Game(ManualPlayer(1), ManualPlayer(2))
    for row in range(0, 8):
        for col in range(0, 8):
            app.board[row][col].append(newGame.board[row][col])

    
def redrawAll(app):
    drawLabel('Chess', app.width/2, 30, size=16)
    drawBoard(app)
    drawBoardBorder(app)

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col, app.board[row][col][0])

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = 50, 50
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = 50, 50
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)




def main():
    runApp()

main()