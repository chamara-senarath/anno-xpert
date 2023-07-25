import tkinter as tk               
from tkinter import font as tkfont
import ttkbootstrap as tb
from pages.collections_page import CollectionsPage

from pages.home_page import HomePage 

class App(tb.Window):

    def __init__(self):
        tb.Window.__init__(self)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("800x600")
        self.resizable(False, False)

        container = tb.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = [HomePage, CollectionsPage]

        self.frames = {}
        for F in self.pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()