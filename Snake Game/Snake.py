import tkinter as tk
import random

#INSTRUCTIONS:
# TO START GAME TYPE A NUMBER IN FOR THE GAME MODE 1,2 OR 3 THEN PRESS ENTER
# PRESS R TO RESET GAME
# PRESS C TO CHANGE MODE OF GAME


#==========================================
# Purpose: The object for this class represents a the GUI for the game
# Instance variables: (What are the instance variables for this class,
# and what does each represent?)
# no instances variables
# Methods: (What methods does this class have, and what does each do?)
# change - method for binding key for changing levels
# reset - method for binding key for reseting game
# gameloop - method where objects are ran and game is played
#==========================================
class SnakeGUI:
    def __init__(self):
        self.user1= int(input("What game mode do you want to play on?" + "\n" +
                              "1 = Hard 2 = Mid or 3 = Esy "+ "\n" + "Pick a number and press ENTER "+ "\n"))
        self.user1 = self.user1 *40
        self.game = True
        self.win = tk.Tk()
        
        self.canvas = tk.Canvas(self.win, width = 660, height = 660)
        self.canvas.pack()
        self.board = self.canvas.create_rectangle(0, 0, 660, 660, fill= "blue", outline = "blue")
        self.board = self.canvas.create_rectangle(30, 30, 630, 630, fill= "black", outline = "blue")
        
            
        
        self.a = Snake(330,330, "green", self.canvas)
        self.e = ESnake(int(random.randint(1,20)*30),int(random.randint(1,20)*30), "red", self.canvas) 
        self.win.bind('<Down>',self.a.go_down)
        self.win.bind('<Up>',self.a.go_up)
        self.win.bind('<Left>',self.a.go_left)
        self.win.bind('<Right>',self.a.go_right)
        self.win.bind('r',self.reset)
        self.win.bind('c',self.change)
        self.fx = int(random.randint(1,20)*30)
        self.fy= int(random.randint(1,20)*30)
        
        self.scirc = self.canvas.create_oval(self.fx,self.fy,self.fx+30,30+self.fy,fill = "purple")
        a = "a"
        self.gameloop()
    def reset(self,event):
        self.game = True
        #self.win = tk.Tk()
        #self.canvas = tk.Canvas(self.win, width = 660, height = 660)
        #self.canvas.pack()
        self.canvas.delete(tk.ALL)
        self.board = self.canvas.create_rectangle(0, 0, 660, 660, fill= "blue", outline = "blue")
        self.board = self.canvas.create_rectangle(30, 30, 630, 630, fill= "black", outline = "blue")
        self.a = Snake(330,330, "green", self.canvas)
        self.e = ESnake(int(random.randint(1,20)*30),int(random.randint(1,20)*30), "red", self.canvas)
        self.win.bind('<Down>',self.a.go_down)
        self.win.bind('<Up>',self.a.go_up)
        self.win.bind('<Left>',self.a.go_left)
        self.win.bind('<Right>',self.a.go_right)
        
        #self.win.bind('r',self.reset)
        self.fx = int(random.randint(1,20)*30)
        self.fy= int(random.randint(1,20)*30)
        
        self.scirc = self.canvas.create_oval(self.fx,self.fy,self.fx+30,30+self.fy,fill = "purple")
        
        self.gameloop()
        
    def change(self,event):
        
        self.user1= int(input("What game mode do you want to play on?" + "\n" +
                              "1 = Hard 2 = Mid or 3 = Esy "+ "\n"))
        self.user1 = self.user1 *40
        
        self.game = True
        #self.win = tk.Tk()
        #self.canvas = tk.Canvas(self.win, width = 660, height = 660)
        #self.canvas.pack()
        self.canvas.delete(tk.ALL)
        self.board = self.canvas.create_rectangle(0, 0, 660, 660, fill= "blue", outline = "blue")
        self.board = self.canvas.create_rectangle(30, 30, 630, 630, fill= "black", outline = "blue")
        self.a = Snake(330,330, "green", self.canvas)
        self.e = ESnake(int(random.randint(1,20)*30),int(random.randint(1,20)*30), "red", self.canvas)
        self.win.bind('<Down>',self.a.go_down)
        self.win.bind('<Up>',self.a.go_up)
        self.win.bind('<Left>',self.a.go_left)
        self.win.bind('<Right>',self.a.go_right)
        
        #self.win.bind('r',self.reset)
        self.fx = int(random.randint(1,20)*30)
        self.fy= int(random.randint(1,20)*30)
        
        self.scirc = self.canvas.create_oval(self.fx,self.fy,self.fx+30,30+self.fy,fill = "purple")
        
        self.gameloop()
        
    
        
    def gameloop(self):
       
        if self.game == True and  self.a.bound() != False:
            var1 = self.a.move(self.fx,self.fy)
            var2 = self.e.move1(self.fx,self.fy)
            a = self.a.attack(self.e)
            if a == True:
                self.game = False
                
            if var1 == True or var2 == True:
                self.canvas.delete(self.scirc)
                self.fx = int(random.randint(1,20)*30)
                self.fy= int(random.randint(1,20)*30)
                self.scirc = self.canvas.create_oval(self.fx,self.fy,self.fx+30,30+self.fy,fill = "purple")
           
            if self.a.x > 600 or self.a.y > 600 or self.a.x < 30 or self.a.y < 30:
                self.game = False
               
            
            self.canvas.after(self.user1, self.gameloop)
        else:
            self.canvas.create_text(350, 300, text='You Lost', fill = "white")
            self.canvas.create_text(350, 350, text='PRESS R TO PLAY AGAIN',fill = "white")
            self.canvas.create_text(350, 620, text='PRESS C TO CHANGE MODE', fill = "white")
            self.canvas.create_text(350, 50, text='Score: '+ str(len(self.a.segments)-1), fill = "white")



            

        

#==========================================
# Purpose: The object for this class represents the users snake
# Instance variables: (What are the instance variables for this class,
# x - is the int value of snake xcord
# y - is the int vaue of snake y 
# color 0 is a string value which represents the color of the snake
# s - is the canvas of the snake object
# Methods: (What methods does this class have, and what does each do?)
# move - a method for making the snake object move
# bound - a method that keeps the snake in bounds
# attack - a method that takes another snake object and checks if the two snakes touc
# go_down - a method that moves snake down and gets binded in snake GU
# go_up - a method that moves snake up and gets binded in snake GU
# go_left - a method that moves snake left and gets binded in snake GU
# go_right - a method that moves snake right and gets binded in snake GUI
#==========================================
class Snake:
    def __init__(self, x,y, color, s ):
        self.x = x
        self.y = y
        self.color = color
        self.s = s
        #self.board = self.s.create_rectangle(x,y,x+30,y+30, fill = color)
        self.segments = []
        self.vx = 30
        self.vy = 0


    def move(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.x = self.x +self.vx
        self.y= self.y + self.vy
       
        self.srec = self.s.create_rectangle(self.x,self.y,self.x+30,self.y+30, fill = self.color)
        #self.rec = self.s.create_rectangle(30,30,60,60, fill = self.color)
        self.segments.insert(0,self.srec)

        if len(self.segments) > 1:
            if self.s.coords(self.srec)[0] == self.cx and self.s.coords(self.srec)[1] == self.cy:
                return True
            else:
                self.b = self.segments.pop()
                self.s.delete(self.b)
                return False
            
            
        

    def bound(self):
        for x in range(4, len(self.segments)):
            if self.s.coords(self.segments[x])[0] == self.x and self.s.coords(self.segments[x])[1] == self.y:
                return False

    def attack(self,other):
    
        for segx in other.esegments:
            x = other.e.coords(segx)[0]
            y = other.e.coords(segx)[1]
            if (self.x == x and self.y ==y):
                return True

        return False
        
       
            
    def go_down(self,event):
        self.vx = 0
        self.vy = 30
    def go_up(self,event):
        self.vx = 0
        self.vy = -30
    def go_left(self,event):
        self.vx = -30
        self.vy = 0
    def go_right(self,event):
        self.vx = 30
        self.vy = 0


    
#==========================================
# Purpose: The object for this class represents the enemy snake
# Instance variables: (What are the instance variables for this class,
# x - is the int value of enemy snake xcord
# y - is the int vaue of the enemy snake y 
# color 0 is a string value which represents the color of the snake
# e - is the canvas of the enemy snake object
# Methods: (What methods does this class have, and what does each do?)
# move1 - a method for making the enemy snake object move
#==========================================
class ESnake:
    def __init__(self, x,y, color, e ):
        self.x = x
        self.y = y
        self.color = color
        self.e = e
        self.board = self.e.create_rectangle(x,y,x+30,y+30, fill = color)
        self.esegments = []
        self.esegments.append(self.board)
        #self.vy = int(random.randint(1,20)*30)
        #self.vx= 0


    def move1(self,cx,cy):
        self.cx = cx
        self.cy = cy
        self.choice = [-30,30,0]
        self.vx = 0
        self.vy = 0

        
        if self.cx > self.x:
            self.vx = 30
            
        elif self.cx == self.x:
            if self.cy > self.y:
                self.vy = 30
                
            else:
                self.vy = -30
    
        else:
            self.vx = -30
            
            
        self.x = self.x +self.vx
        self.y= self.y + self.vy

        
        self.Erec = self.e.create_rectangle(self.x,self.y,self.x+30,self.y+30, fill = self.color)
        self.esegments.insert(0,self.Erec)
        #if len(self.esegments) > 1:
        if self.e.coords(self.Erec)[0] == self.cx and self.e.coords(self.Erec)[1] == self.cy:
            return True
        else:
            self.b = self.esegments.pop()
            self.e.delete(self.b)
            return False
                


            


  

        
SnakeGUI()
