import ttkbootstrap as tb

def collections_view(container,change_frame):
    frame = tb.Frame(container)
    # button
    convert_button = tb.Button(text='Convert').grid(column=2, row=0, sticky='w')

    frame.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
    return frame