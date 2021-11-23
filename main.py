import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
import subprocess
import simpleaudio as sa


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "buttons.ui"
proc = 0

class ButtonsApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.mainwindow = tk.Frame(self.toplevel1)
        self.label1 = tk.Label(self.mainwindow)
        self.label1.configure(background='#ecf0f1', font='{Noto Sans} 16 {}', foreground='#2c3e50', text='ELEC3848 Project Demo')
        self.label1.pack(anchor='center', pady='20', side='top')
        self.label2 = tk.Label(self.mainwindow)
        self.label2.configure(background='#ecf0f1', font='{Noto Sans} 12 {}', foreground='#2c3e50', text='Click on the desired feature to demonstrate.')
        self.label2.pack(pady='7', side='top')
        self.frame2 = tk.Frame(self.mainwindow)
        self.button1 = tk.Button(self.frame2)
        self.button1.configure(background='#34495e', font='{Noto Sans} 12 {}', foreground='#ecf0f1', relief='flat')
        self.button1.configure(takefocus=False, text='Gesture Recognition')
        self.button1.pack(ipady='10', pady='5', side='top')
        self.button1.bind('<1>', self.btn1_callback, add='')
        self.button2 = tk.Button(self.frame2)
        self.button2.configure(background='#34495e', font='{Noto Sans} 12 {}', foreground='#ecf0f1', relief='flat')
        self.button2.configure(text='View Gyroscope visualization')
        self.button2.pack(ipady='10', pady='5', side='top')
        self.button2.bind('<1>', self.btn2_callback, add='')
        self.button3 = tk.Button(self.frame2)
        self.button3.configure(background='#34495e', font='{Noto Sans} 12 {}', foreground='#ecf0f1', text='Exit')
        self.button3.pack(ipady='10', pady='5', side='top')
        self.button3.pack_propagate(0)
        self.button3.bind('<1>', self.btn3_callback, add='')
        self.frame2.configure(background='#ecf0f1', height='200', width='200')
        self.frame2.pack(pady='15', side='top')
        self.mainwindow.configure(background='#ecf0f1', cursor='arrow', height='480', width='640')
        self.mainwindow.pack(side='top')
        self.mainwindow.pack_propagate(0)
        self.toplevel1.configure(height='480', width='640')
        self.toplevel1.geometry('800x480')
        self.toplevel1.maxsize(800, 480)
        self.toplevel1.minsize(800, 480)
        self.toplevel1.resizable(False, False)
        self.toplevel1.title('ELEC3848 Proejct Demo')

        # Main widget
        self.mainwindow = self.toplevel1
    
    def run(self):
        self.mainwindow.mainloop()

    def btn1_callback(self, event=None):
        print("Starting dog mode..")
        grp = subprocess.Popen(["python3", "gesreg.py"])
        proc = grp
        pass

    def btn2_callback(self, event=None):
        print("Starting gyroscope...")
        grp = subprocess.Popen(["python3", "accl_view.py"])
        proc = grp
        pass

    def btn3_callback(self, event=None):
        print("Exiting...")
        wave_obj = sa.WaveObject.from_wave_file('audio/exit.wav')
        wave_obj.play()
        try:
            proc.kill()
        except Exception:
            pass
        quit()
        pass
        


if __name__ == '__main__':
    wave_obj = sa.WaveObject.from_wave_file('audio/hello.wav')
    wave_obj.play()
    app = ButtonsApp()
    app.run()

