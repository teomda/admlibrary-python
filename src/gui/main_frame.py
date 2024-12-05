import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()