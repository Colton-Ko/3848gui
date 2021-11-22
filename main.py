import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "buttons.ui"


class ButtonsApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('toplevel1', master)
        builder.connect_callbacks(self)
    
    def run(self):
        self.mainwindow.mainloop()

    def btn1_callback()(self, event=None):
        pass

    def (self, event=None):
        pass

    def btn2_callback()(self, event=None):
        pass

    def btn3_callback()(self, event=None):
        pass


if __name__ == '__main__':
    app = ButtonsApp()
    app.run()

