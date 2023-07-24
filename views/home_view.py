import ttkbootstrap as tb

def home_view(container,change_frame):
    frame = tb.Frame(container)
    # button
    convert_button = tb.Button(text='Home',command=lambda: change_frame('collection')).grid(column=2, row=0, sticky='w')
    tb.Button(text='Haaa').grid(column=3, row=3, sticky='s')
    frame.grid(column=0, row=1, padx=15, pady=15, sticky="nsew")
    return frame
