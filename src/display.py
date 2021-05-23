from src.components import *
import tkinter as tk
from tkinter import Tk, Label, Button, Frame, Canvas
from PIL import Image, ImageTk



class MyFirstGUI:
    def __init__(self, masterWindow):
        self.masterWindow = masterWindow
        masterWindow.title('Starter GUI')

        im = Image.open('resources/board.png')
        better_im = ImageTk.PhotoImage(im)

        self.label = Label(masterWindow, text='Label', image=better_im)
        self.label.image = better_im
        self.label.pack()

        self.canvas = Canvas(masterWindow)
        self.canvas.pack()

gameBoard = Board()

root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
