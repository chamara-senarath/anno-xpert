import ttkbootstrap as tb

class HomePage(tb.Frame):

    def __init__(self, parent, controller):
        tb.Frame.__init__(self, parent)
        self.controller = controller
        label = tb.Label(self, text="This is the start page",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tb.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("CollectionsPage"))
        button1.pack()
