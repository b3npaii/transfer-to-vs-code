from cmu_graphics import *
from game import *
from minimaxPlayer import *
from PIL import Image

def onAppStart(app):
    reset(app)
    loadImages(app)

def reset(app):
    app.width = 660
    app.height = 660
    app.rows = 8
    app.cols = 8
    app.boardLeft = 50
    app.boardTop = 50
    app.boardWidth = 560
    app.boardHeight = 560
    app.cellBorderWidth = 2
    app.board = [([None] * app.cols) for row in range(app.rows)]
    for i in range(0, 8):
        for j in range(0, 8):
            if i % 2 == j % 2:
                app.board[i][j] = ["white"]
            else:
                app.board[i][j] = ["black"]
    app.inGame = False
    app.newGame = Game(ManualPlayer(1), ManualPlayer(2))
    for row in range(0, 8):
        for col in range(0, 8):
            app.board[row][col].append(app.newGame.board[row][col])
    app.selectedPiece = None
    app.gameOver = False
    app.computerPlays = False
    
def redrawAll(app):
    drawBoard(app)
    drawBoardBorder(app)

def drawBoard(app):
    if app.inGame:
        for row in range(app.rows):
            for col in range(app.cols):
                drawCell(app, row, col, app.board[row][col][0])
                x, y = findCellCenter(app, row, col)
                if app.board[row][col][1] != 0:
                    drawPiece(app, row, col, app.board[row][col][1])
        if app.selectedPiece != None:
            x, y = app.newGame.findPiece(app.selectedPiece)
            highlightSquare(app, x, y)
    else:
        drawLabel("Chess", app.width / 2, 150, size=50)
        drawRect(205, 200, 250, 50, fill=None, border="black")
        drawLabel("Play vs Computer", 330, 225)
        drawRect(205, 300, 250, 50, fill=None, border="black")
        drawLabel("Play vs Human", 330, 325)
    if app.newGame.winner != None:
        drawGameOver(app)

def drawPiece(app, row, col, piece):
    x, y = getCellLeftTop(app, row, col)
    if "wp" in piece:
        drawImage(app.whitePawn, x, y)
    elif "wn" in piece:
        drawImage(app.whiteKnight, x, y)
    elif "wb" in piece:
        drawImage(app.whiteBishop, x, y)
    elif "wr" in piece:
        drawImage(app.whiteRook, x, y)
    elif "wk" in piece:
        drawImage(app.whiteKing, x, y)
    elif "wq" in piece:
        drawImage(app.whiteQueen, x, y)

def loadImages(app):
    app.whitePawn = CMUImage(Image.open("white_pawn.png"))
    app.whiteKnight = CMUImage(Image.open("white_knight.png"))
    app.whiteBishop = CMUImage(Image.open("white_bishop.png"))
    app.whiteRook = CMUImage(Image.open("white_rook.png"))
    app.whiteKing = CMUImage(Image.open("white_king.png"))
    app.whiteQueen = CMUImage(Image.open("white_queen.png"))

def drawBoardBorder(app):
  # draw the board outline (with double-thickness):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = 70, 70
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='black',
             borderWidth=app.cellBorderWidth)

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = 70, 70
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def findCellCenter(app, row, col):
    x, y = getCellLeftTop(app, row, col)
    return x + 25, y + 25

def onMousePress(app, mouseX, mouseY):
    if app.inGame:
        if mouseX in range(50, 610):
            if mouseY in range(50, 610):
                col = ((mouseX + 20) // 70) - 1
                row = ((mouseY + 20)// 70) - 1
                if app.selectedPiece == None:
                    if app.newGame.turn == 1:
                        if type(app.newGame.board[row][col]) == str and app.newGame.board[row][col][0] == "w":
                            app.selectedPiece = app.newGame.board[row][col]
                    else:
                        if type(app.newGame.board[row][col]) == str and app.newGame.board[row][col][0] == "b":
                            app.selectedPiece = app.newGame.board[row][col]
                elif app.selectedPiece != None:
                    app.newGame.makeMove(app.selectedPiece, (row, col))
                    updateBoard(app)
                    app.selectedPiece = None
                    if app.computerPlays:
                        if app.newGame.turn == 1:
                            run(app)
                            updateBoard(app)
        else:
            app.selectedPiece = None
    else:
        if mouseX in range(305, 405):
            if mouseY in range(200, 250):
                app.inGame = True
                app.newGame = Game(MinimaxPlayer(2, 1), ManualPlayer(2))
                app.computerPlays = True
                run(app)
                updateBoard(app)
            elif mouseY in range(300, 350):
                app.inGame = True
                app.newGame = Game(ManualPlayer(1), ManualPlayer(2))
    #need to implement castling here
    #show legal moves for a piece

def run(app):
    if app.computerPlays:
        if app.newGame.turn == 1:
            x, y = app.newGame.chooseMove()
            app.newGame.makeMove(x, y)

def updateBoard(app):
    for i in range(0, 8):
        for j in range(0, 8):
            app.board[i][j].pop(1)
            app.board[i][j].append(app.newGame.board[i][j])

def drawGameOver(app):
    drawLabel("The game is over!", 330, 250, size=50, fill="red")
    drawLabel(str(app.newGame.winner) + "wins!", 330, 300, fill="red", size=30)
    drawLabel("Press r to reset to the menu", 330, 350, fill="red", size=30)

def highlightSquare(app, row, col):
    x, y = getCellLeftTop(app, row, col)
    drawRect(x, y, 70, 70, fill=None, border="yellow")

def onKeyPress(app, key):
    if app.newGame.winner != None:
        if key == "r":
            reset(app)

def main():
    runApp()

main()