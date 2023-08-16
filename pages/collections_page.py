import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from services.schema_processor import SchemaProcessor
from services.xml_processor import XMLProcessor
import re


class CollectionsPage(tb.Frame):

    def __init__(self, parent, controller):
        self.level = 2
        self.maximum_dropdowns = 3
        self.schema_processor = None
        self.xml_processor = None

        self.combo_boxes = []
        self.combo_box_node_map = {}
        self.entry_search = None
        self.applied_filters = []

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

        # Dropdown area
        self.dropdown_frame = tb.Frame(self, padding=16)
        self.dropdown_frame.pack(fill=tk.BOTH)  
        label_dropdowns = tb.Label(self.dropdown_frame, text="Select Elements: ")      
        label_dropdowns.pack(side='left', anchor='n')

        # Search area
        search_frame = tb.Frame(self,padding=16)
        search_frame.pack(fill=tk.BOTH)
        self.entry_search = tb.Entry(search_frame, width=50)
        self.entry_search.pack(side='left', anchor='n')
        button_search = tb.Button(search_frame, text="Search", command=self.handle_search)
        button_search.pack(side='right', anchor='n')

        # Results display
        result_frame = tb.Frame(self)
        result_frame.pack(padx=16, pady=16,fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(result_frame, width=780)
        canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tb.Scrollbar(result_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=self.scrollbar.set)

        self.result_content_frame = tb.Frame(canvas)
        canvas.create_window((0, 0), window=self.result_content_frame, anchor="nw")

        self.result_content_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

        self.results_filters_frame = tb.Frame(result_frame)
        self.results_filters_frame.pack(side="right", anchor='center', padx=10, expand=True)



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
        self.combo_box_node_map[0] = self.schema_processor.get_nodes_by_level(self.level)
        self.create_dropdowns(values)

    def load_dependent_dropdown(self, combo_box):
        self.clear_dropdowns(combo_box)

        if len(self.combo_boxes) >= self.maximum_dropdowns:
            return
        
        item = self.combo_box_node_map[self.combo_boxes.index(combo_box)][combo_box.current()]

        if isinstance(item, str):
            return 
        if  isinstance(item.get_attr("enumerations"), list) :
            values = item.get_attr("enumerations")
            self.combo_box_node_map[self.combo_boxes.index(combo_box)+1] = values
            self.create_dropdowns(values)

        if isinstance(item.children, tuple) and len(item.children) > 0:
            values = [x.name for x in item.children]
            self.combo_box_node_map[self.combo_boxes.index(combo_box)+1] = item.children
            self.create_dropdowns(values)

    def clearFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def load_result_data_elements(self, elements):
        self.clearFrame(self.result_content_frame)
        if len(elements)==0:
            data_label = tb.Label(self.result_content_frame, text="No Results Found")   
            data_label.pack(fill="both", anchor="center")
            self.scrollbar.pack_forget()
        for element in elements:
            data_label_frame = tb.LabelFrame(self.result_content_frame, text=element['local_name'], padding=5)
            data_label_frame.pack(side="top", anchor='w', fill="x", pady=10)
            data_label = tb.Label(data_label_frame, text=element['text'].strip(), wraplength=750)   
            data_label.pack(fill="x", anchor='w')   
            self.scrollbar.pack(side="left", fill="y")

            for index, attribute in enumerate(element['attributes']):
                attribute_label = tb.Label(data_label_frame,bootstyle="inverse-info", text=f"{attribute[0]}: {attribute[1]}", padding=2)
                attribute_label.pack(side="left", anchor='w', padx=0 if index==0 else 5, pady=2)
        
    def load_result_filters(self, elements):
        self.clearFrame(self.results_filters_frame)
        element_set = set()
        for element in elements:
            if element['local_name'] not in element_set:
                element_set.add(element['local_name'])
                filter_button = tb.Button(self.results_filters_frame, text=element['local_name'], bootstyle="success-outline")   
                filter_button.config(command=lambda btn=filter_button, results=elements: self.apply_filter(btn,results))
                filter_button.pack(fill="x", anchor='w', pady=10)

    def load_schema(self):
        self.clear_dropdowns()
        self.clear_result_section()
        schema_file = filedialog.askopenfilename(filetypes=[("XSD Files", "*.xsd")])
        if not schema_file: return
        self.schema_processor = SchemaProcessor(schema_file)
        self.load_parent_dropdown()

    def load_data(self):
        xml_file = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
        if not xml_file: return
        self.xml_processor = XMLProcessor(xml_file)

    def format_text(self, input_text):
        formatted_name = re.sub(r'_', ' ', input_text)        
        formatted_name = re.sub(r'([a-z])([A-Z])', r'\1 \2', formatted_name)
        formatted_name = formatted_name.title()
        return formatted_name
    
    def handle_search(self):
        if not self.xml_processor : return
        query = self.entry_search.get().strip()
        if not query: return
        results = self.xml_processor.query_xml(query)

        self.load_result_filters(results)
        self.load_result_data_elements(results)

    def apply_filter(self, button, results):        
        filter = button.config('text')[-1]
        if filter in self.applied_filters:
            self.applied_filters.remove(filter)
            button.config(bootstyle="success-outline")
        else:
            self.applied_filters.append(filter)
            button.config(bootstyle="success")
            
        self.update_result_with_filters(results)

    def update_result_with_filters(self, results):
        if not self.applied_filters: 
            self.load_result_data_elements(results)
            return 
        results = [element for element in results if element['local_name'] in self.applied_filters]
        self.load_result_data_elements(results)

    def clear_result_section(self):
        self.applied_filters = []
        self.clearFrame(self.result_content_frame)
        self.clearFrame(self.results_filters_frame)
        