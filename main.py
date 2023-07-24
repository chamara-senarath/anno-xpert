from control_frames import control_frame_init
import ttkbootstrap as tb


def create_app():
    app = tb.Window()

    app.title('Temperature Converter')
    app.geometry('800x600')
    app.resizable(False, False)

    return app

if __name__ == "__main__":
    app = create_app()
    control_frame_init(app)
    app.mainloop()