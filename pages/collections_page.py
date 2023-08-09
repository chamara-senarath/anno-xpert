import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from services.schema_processor import SchemaProcessor


class CollectionsPage(tb.Frame):

    def __init__(self, parent, controller):
        self.level = 2
        self.maximum_dropdowns = 3
        self.combo_boxes = []

        tb.Frame.__init__(self, parent)
        self.controller = controller

        header_frame =  tb.Frame(self, padding=16)
        header_frame.pack(fill=tk.BOTH)        

        label_header = tb.Label(header_frame, text="This is page 1",font=controller.title_font)
        label_header.pack(side="left", anchor='n', fill=tk.X, expand=True)

        button_load_schema = tb.Button(header_frame, text="Load Schema", command=self.load_schema)
        button_load_data = tb.Button(header_frame, text="Load Data", command=self.load_data)
        button_load_schema.pack(side="left", anchor='n',fill=tk.X, padx=10)
        button_load_data.pack(side="left", anchor='n', fill=tk.X)

        self.dropdown_frame = tb.Frame(self, padding=16)
        self.dropdown_frame.pack(expand=True, fill=tk.BOTH)  
        label_dropdowns = tb.Label(self.dropdown_frame, text="Select Elements: ")      
        label_dropdowns.pack(side='left', anchor='n')
        button_search_dropdown = tb.Button(self.dropdown_frame, text="Search")
        button_search_dropdown.pack(side='right', anchor='n')

    def create_dropdowns(self,values):
        combo_box = tb.Combobox(self.dropdown_frame, width=14 ,values = [self.format_text(value) for value in values], state='readonly')
        combo_box.bind('<<ComboboxSelected>>', lambda x: self.load_dependent_dropdown(combo_box))
        self.combo_boxes.append(combo_box)
        combo_box.pack(side="left",anchor='n', padx=10)
    
    def clear_dropdowns(self,combo_box=None):
        start = self.combo_boxes.index(combo_box)+1 if combo_box is not None else 0
        for i in self.combo_boxes[start:]:
            i.destroy()
            self.combo_boxes.remove(i)

    def load_parent_dropdown(self):
        values = [x.name for x in self.schema_processor.get_nodes_by_level(self.level)]
        self.create_dropdowns(values)

    def load_dependent_dropdown(self, combo_box):
        self.clear_dropdowns(combo_box)

        if len(self.combo_boxes) >= self.maximum_dropdowns:
            return

        item = self.schema_processor.get_nodes_by_level(self.combo_boxes.index(combo_box)+2)[combo_box.current()]

        if isinstance(item.get_attr("enumerations"), list) :
            values = item.get_attr("enumerations")
            self.create_dropdowns(values)

        if isinstance(item.children, tuple) and len(item.children) > 0:
            values = [x.name for x in item.children]
            self.create_dropdowns(values)

    def load_schema(self):
        self.clear_dropdowns()
        schema_file = filedialog.askopenfilename(filetypes=[("XSD Files", "*.xsd")])
        if not schema_file:
            return
        self.schema_processor = SchemaProcessor(schema_file)
        self.load_parent_dropdown()

    def load_data(self):
        pass

    def format_text(self, input_text):
        words = input_text.split('_')
        formatted_words = [word.capitalize() for word in words]
        formatted_text = ' '.join(formatted_words)
        return formatted_text