import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk

def load_parent_elements():
    try:
        tree = ET.parse("schema.xsd")
        root = tree.getroot()
        elements = set()

        # Find parent elements in the schema
        for elem in root.iter():
            if elem.tag.endswith('element') and 'name' in elem.attrib:
                elements.add(elem.attrib['name'])

        # Clear and populate dropdown menu
        element_var.set('')
        element_dropdown['values'] = list(elements)

        # Clear results
        result_text.configure(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.configure(state='disabled')

    except ET.ParseError:
        messagebox.showerror("Invalid Schema", "The 'schema.xsd' file is not valid XML.")

def find_results(*args):
    selected_element = element_var.get()

    if not selected_element:
        return

    search_text = search_var.get()

    try:
        tree = ET.parse(data_file)
        root = tree.getroot()

        # Find results for the selected element
        results = []
        ancestors_stack = []
        for elem in root.iter():
            if elem.text is not None and elem.text.strip():
                ancestors = [e.tag.split('}')[-1] for e in ancestors_stack]
                if selected_element in ancestors:
                    if search_text.lower() in elem.text.lower():
                        results.append(elem.text)

            ancestors_stack.append(elem)  # Update ancestors stack

        # Clear results
        result_text.configure(state='normal')
        result_text.delete('1.0', tk.END)

        if results:
            result_text.insert(tk.END, f"Results for '{selected_element}' containing '{search_text}':\n\n")
            for result in results:
                result_text.insert(tk.END, f"{result}\n\n")  # Add extra newline between results
        else:
            result_text.insert(tk.END, f"No results found for '{selected_element}' containing '{search_text}'.")

        result_text.configure(state='disabled')

    except ET.ParseError:
        messagebox.showerror("Invalid Data", "The selected 'data.xml' file is not valid XML.")





# Create the main window
window = tk.Tk()
window.title("XML Parser")

# Calculate window size as 90% of screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)
x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
window.resizable(False, False)

# Load parent elements
load_button = tk.Button(window, text="Load Elements", command=load_parent_elements)
load_button.pack(pady=10)

# Dropdown menu for elements
element_var = tk.StringVar(window)
element_dropdown = ttk.Combobox(window, textvariable=element_var, state='readonly')
element_dropdown.pack()

# Search box
search_var = tk.StringVar(window)
search_entry = ttk.Entry(window, textvariable=search_var)
search_entry.pack(pady=10)

# Find button
find_button = tk.Button(window, text="Find", command=find_results)
find_button.pack(pady=10)

# Results display
result_frame = tk.Frame(window)
result_frame.pack(pady=10)

scrollbar = ttk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(result_frame, height=int(window_height * 0.9), width=int(window_width * 0.9))
result_text.pack(side=tk.LEFT, fill=tk.BOTH)
result_text.configure(state='disabled')

scrollbar.config(command=result_text.yview)
result_text.config(yscrollcommand=scrollbar.set)

# Start the GUI event loop
window.mainloop()
