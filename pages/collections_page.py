import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from services.schema_processor import SchemaProcessor

import pydot
from PIL import Image, ImageTk

class CollectionsPage(tb.Frame):

    def __init__(self, parent, controller):
        tb.Frame.__init__(self, parent)
        self.controller = controller
        label = tb.Label(self, text="This is page 1",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tb.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()
        xml_processor = SchemaProcessor(self.browse_schema_file())

    def browse_schema_file(self):
        return filedialog.askopenfilename(filetypes=[("XSD Files", "*.xsd")])
    