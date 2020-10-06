from bangtal import *
import random

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)

scene=Scene("마리오","images/problem.png")

def find_index(object):
    for index in range(16):
        if game_board[index]==object:return index

def movable(index):
    if index<0:return False
    if index>16:return False
    if index%4>0and index-1==blank:return True
    if index%4<3and index+1==blank:return True
    if index>3 and index-4==blank:return True
    if index<12 and index+4==blank:return True
    return False

def move(index):
    global blank

    game_board[index].locate(scene,360+140*(blank%4),500-140*(blank//4))
    game_board[blank].locate(scene,360+140*(index%4),500-140*(index//4))

    game_board[index],game_board[blank]= game_board[blank],game_board[index]
    #object=game_board[index]
    #game_board[index]=game_board[blank]
    #game_board[blank]=object

    blank=index
def completed():
    for index in range(16):
        if game_board[index]!=init_board[index]:return False
    return True

def onMouseAction_piece(object,x,y,action):
    index=find_index(object)
    if movable(index):
        move(index)
        if completed()==True:showMessage("끗")
Object.onMouseActionDefault=onMouseAction_piece

game_board=[]
init_board=[]
for index in range(16):
    piece=Object("images/"+str(index+1)+".png")
    piece.locate(scene,360+140*(index%4),500-140*(index//4))
    piece.show()

    game_board.append(piece)
    init_board.append(piece)

blank=15
game_board[blank].hide()

delta=[-1,1,-4,4]
def random_move():
    while True:
        index=blank+delta[random.randrange(4)]
        if movable(index): break
    move(index)


count =50
timer =Timer(1)
def onTimeout():
    random_move()
    global count 
    print(count)
    count =count-1
    if count>0:

        timer.set(0.1)
        timer.start()
timer.onTimeout=onTimeout

timer.start()
startGame(scene)
