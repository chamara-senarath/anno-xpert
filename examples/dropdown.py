import os
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk
from tkinter import ttk, filedialog

def find_schema_file(current_folder):
    for file_name in os.listdir(current_folder):
        if file_name.lower().endswith('.xsd'):
            return os.path.join(current_folder, file_name)
    return None

def extract_types_and_subtypes(schema_file):
    types_and_subtypes = {}
    tree = ET.parse(schema_file)
    root = tree.getroot()

    for element in root.findall('.//xs:element', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'}):
        element_name = element.get('name')
        if element_name not in types_and_subtypes:
            types_and_subtypes[element_name] = []

        type_element = element.find('.//xs:complexType', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'})
        if type_element is not None:
            for subtype_element in type_element.iterfind('.//xs:restriction/xs:enumeration', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'}):
                subtype_name = subtype_element.get('value')
                types_and_subtypes[element_name].append(subtype_name)

    return types_and_subtypes

def on_parent_selected(event):
    selected_parent = parent_var.get()
    children = types_and_subtypes.get(selected_parent, [])
    
    child_var.set("")
    child_dropdown['values'] = children

def on_child_selected(event):
    selected_child = child_var.get()
    grandchildren = types_and_subtypes.get(selected_child, [])

    if grandchildren:
        grandchild_var.set("")
        grandchild_dropdown['values'] = grandchildren
        grandchild_dropdown.grid(row=2, column=0, padx=10, pady=5)
    else:
        grandchild_dropdown.grid_forget()

if __name__ == "__main__":
    # Task 1: Let the user upload the .xsd file
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    schema_file_path = filedialog.askopenfilename(filetypes=[("XML Schema Files", "*.xsd")])
    if not schema_file_path:
        print("No file selected. Exiting.")
        exit()

    # Task 2 and 3: Identify types and subtypes
    types_and_subtypes = extract_types_and_subtypes(schema_file_path)

    # Create the GUI
    root = tk.Tk()
    root.title("Type and Subtype Selection")

    parent_var = tk.StringVar(root)
    child_var = tk.StringVar(root)
    grandchild_var = tk.StringVar(root)

    parent_label = ttk.Label(root, text="Select Parent:")
    parent_label.grid(row=0, column=0, padx=10, pady=5)

    parent_dropdown = ttk.Combobox(root, textvariable=parent_var, values=list(types_and_subtypes.keys()))
    parent_dropdown.grid(row=0, column=1, padx=10, pady=5)
    parent_dropdown.bind("<<ComboboxSelected>>", on_parent_selected)

    child_label = ttk.Label(root, text="Select Child:")
    child_label.grid(row=1, column=0, padx=10, pady=5)

    child_dropdown = ttk.Combobox(root, textvariable=child_var, values=[])
    child_dropdown.grid(row=1, column=1, padx=10, pady=5)
    child_dropdown.bind("<<ComboboxSelected>>", on_child_selected)

    grandchild_dropdown = ttk.Combobox(root, textvariable=grandchild_var, values=[])
    grandchild_dropdown.grid(row=2, column=0, padx=10, pady=5)

    root.mainloop()
