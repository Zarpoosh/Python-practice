import tkinter as tk
class Calculator(tk.Frame):
    result = 0
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.label = tk.Label(self, text="0")
        self.label.pack()
