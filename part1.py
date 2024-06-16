import pygame as p
import time

p.init()

class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height 
        self.content = ''
        self.number = number
        self.image = blank_img
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
    
    def update(self):
        self.rect.topleft = (self.x, self.y)

    def clicked(self,x_cord,y_cord):
        global turn,won
        if self.content == '': # nothing has been placed at that point -- 
           if self.rect.collidepoint(x_cord,y_cord): #its going to return either true or false 
              self.content= turn
              board[self.number] =turn


              if turn == 'x':
                  self.image = x_img
                  self.image= p.transform.scale(self.image,(self.width,self.height))
                  turn = 'o'  #this is a global variable
                  checkWinner('x')

                  if not won:
                   Traverse()  #computer turn 
              else:
                  self.image = o_img
                  self.image= p.transform.scale(self.image,(self.width,self.height))
                  turn = 'x'  #this is a global variable
                  checkWinner('o')

def Update():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()


def checkCenter():
    global compMove,move
    
    if board[5]=="":
      compMove=5
      move=False


def checkCorner():
    global compMove,move
    
    for i in range(1,11,2):
      if board[i]=="":
        compMove=i
        move=False
        break


def checkEdge():
    global compMove,move
    
    for i in range(2,10,2):
      if board[i]=="":
        compMove=i
        move=False
        break
      



def winner(player): # it can be x or it can be y
   global compMove,move

   for i in range(8):
      
     if board[winners[i][0]] == player and board[winners[i][1]== player and board[winners[i][2]]]=="":
          compMove=winners[i][2]
          move = False


     elif board[winners[i][0]] == player and board[winners[i][1]== "" and board[winners[i][2]]]==player:
            compMove=winners[i][1]
            move = False
   
     elif board[winners[i][0]] == "" and board[winners[i][1]== player and board[winners[i][2]]]==player:
            compMove=winners[i][0]
            move = False



def checkWinner(player):
    global background, won
    
    for i in range(8):
       if(board[winners[i][0]] == player and board[winners[i][1]== player and board[winners[i][2]]]==player):
        won = True


    if won:
        Update()
        square_group.empty() 
        background = p.image.load(player.upper()+ ' Wins.png')
        background = p.transform.scale(background,(WIDTH,HEIGHT))

def Traverse():
#    time.sleep(2)
   global move

   move =True

   if move:
      winner('o')

   if move:
      winner('x')
   if move:
      checkCenter()

   if move:
      checkCorner()
   
   if move:
      checkEdge()

   if not move:
      for box in squares:
         if box.number==compMove:
            box.clicked(box.x,box.y)
   
WIDTH = 600
HEIGHT = 600


won =False
win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("TIC TAC TOE")
clock = p.time.Clock() ##it will just tick the clock for som reference somewhere in the code

blank_img = p.image.load('Blank.png')
background = p.image.load('Background.png')
x_img = p.image.load('x.png')
o_img = p.image.load('o.png')



move = True
compMove =1
square_group = p.sprite.Group()
squares = []


winners =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
# as there are 9 box only but our indexing is starting from 1 thus have taken 9
board =['' for i in range(10)]

num = 1


# as (1,4) means it will take three value only 
for y in range(3):  # creating a 3x3 grid
    for x in range(3):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)
        num += 1


turn='x'
run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        
        if event.type== p.MOUSEBUTTONDOWN and turn == 'x':
            x_addr,y_addr= p.mouse.get_pos()  #return the mouse position
            
            for box in squares:
               box.clicked(x_addr,y_addr)

    Update()

p.quit()
