from tkinter import *
import random
import msvcrt

class Dot_Hunt(Frame):
    """ Move the P with WASD to eat the dots. """

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.accum = 0
        self.xP = random.randint(1,8)
        self.yP = random.randint(1,8)
        self.create_board()

    def create_board(self):
        self.prompt = Label(self, text = "Move the P with WASD.  Eat the dots!")
        self.prompt.grid(row = 0, column = 0, columnspan = 8, sticky = W)

        for j in range(1,9):
            self.border = Label(self, text = "[")
            self.border.grid(row = j, column = 0, sticky = W)
            for i in range(1,9):
                self.board = Label(self, text = "-")
                self.board.grid(row = j, column = i, sticky = W)
            self.border = Label(self, text = "]")
            self.border.grid(row = j, column = 9, sticky = W)
        
        self.counter = Label(self, text = "You have eaten " + str(self.accum) + " dots.")
        self.counter.grid(row = 9, column = 0, columnspan = 8, sticky = W)
        
        self.P = Label(self, text = "P")
        self.P.grid(row = self.yP, column = self.xP, sticky = W)

        self.xdot = random.randint(1,8)
        self.ydot = random.randint(1,8)

        self.dot = Label(self, text = "o")
        self.dot.grid(row = self.ydot, column = self.xdot, sticky = W)

        while self.xdot != self.xP and self.ydot != self.yP:
            move = msvcrt.getch()
            move = move.upper()

            while move not in ["W","A","S","D"]:
                move = msvcrt.getch()
                move = move.upper()

            self.board = Label(self, text = "-")
            self.board.grid(row = self.yP, column = self.xP, sticky = W)
                
            if move == "W":
                self.yP -= 1
                if self.yP < 1:
                    self.yP = 1
            elif move == "A":
                self.xP -= 1
                if self.xP < 1:
                   self.xP = 1
            elif move == "S":
                self.yP += 1
                if self.yP > 8:
                    self.yP = 8
            elif move == "D":
                self.xP += 1
                if self.xP > 8:
                    self.xP = 8

            self.P = Label(self, text = "P")
            self.P.grid(row = self.yP, column = self.xP, sticky = W)
            
        
root = Tk()
root.title("Test GUI")
root.geometry("300x300")
app = Dot_Hunt(root)
root.mainloop()
