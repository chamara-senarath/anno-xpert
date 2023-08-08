import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from services.schema_processor import SchemaProcessor


class CollectionsPage(tb.Frame):

    def __init__(self, parent, controller):
        self.level = 2
        tb.Frame.__init__(self, parent)
        self.controller = controller
        label = tb.Label(self, text="This is page 1",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button_load_schema = tb.Button(self, text="Load Schema", command=self.load_schema)
        button_load_data = tb.Button(self, text="Load Data", command=self.load_data)
        button_load_schema.pack()
        button_load_data.pack()

        self.combo_boxes = []

    def create_dropdowns(self,values):
        combo_box = tb.Combobox(self, width = 27, values = values, state='readonly')
        combo_box.bind('<<ComboboxSelected>>', lambda x: self.load_dependent_dropdown(combo_box))
        self.combo_boxes.append(combo_box)
        combo_box.pack()
    
    def clear_dependent_dropdowns(self,combo_box):
        pass
        # print(self.combo_boxes[self.combo_boxes.index(combo_box):])
        # print(type(self.combo_boxes[0]))
        # self.combo_boxes[0].destroy()
        # for i in self.combo_boxes[self.combo_boxes.index(combo_box):]:
            # print(i)
        #     self.combo_boxes.remove(i)

    def load_parent_dropdown(self):
        values = [x.name for x in self.schema_processor.get_nodes_by_level(self.level)]
        self.create_dropdowns(values)

    def load_dependent_dropdown(self, combo_box):
        self.clear_dependent_dropdowns(combo_box)

        item = self.schema_processor.get_nodes_by_level(self.level)[combo_box.current()]
        if isinstance(item.get_attr("enumerations"), list) :
            values = item.get_attr("enumerations")
            self.create_dropdowns(values)

    def load_schema(self):
        schema_file = filedialog.askopenfilename(filetypes=[("XSD Files", "*.xsd")])
        self.schema_processor = SchemaProcessor(schema_file)
        self.load_parent_dropdown()

    def load_data(self):
        pass