import customtkinter as ctk
from customtkinter import *
from customtkinter import filedialog
import ctypes
import os
from jsonGen import csv_to_json, jsonGenerator, delayTime, delete_files, createFolders
import webbrowser

class App():

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctypes.windll.shcore.SetProcessDpiAwareness(True) #upscale
        bgColor = '#292929'
        self.csvLocation = ''

        root = ctk.CTk()
        root.title("Hello World")
        root.geometry('600x600')

        mainframe = ctk.CTkFrame(root, bg_color=bgColor)
        mainframe.pack(fill='both', expand=True)
        text = ctk.CTkLabel(mainframe, text='Converter', font=("HelveticaNowDisplay-Black", 30))
        text.pack(pady=80)

        self.display_path = ctk.CTkLabel(mainframe, text="")
        self.display_path.pack()

        select_file_button = ctk.CTkButton(mainframe, text="Select CSV", border_width=0, command=self.select_file)
        select_file_button.pack()

        self.process_button = ctk.CTkButton(mainframe, text="Process & Convert", border_width=0, state= DISABLED, command=self.c2j)
        self.process_button.pack(pady=10)

        self.progressNum = ctk.CTkLabel(mainframe, text='0/0')
        self.progressNum.pack()
        
        open_file_button = ctk.CTkButton(mainframe, text="Open File Location", border_width=0, command=self.open_file)
        open_file_button.pack(pady=20)

        purge_past_data = ctk.CTkButton(mainframe, text="Purge Previous Data", border_width=0, command=self.purgeF)
        purge_past_data.pack(pady=20)

        #stay on top
        root.attributes('-topmost', True)
        root.mainloop()

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("CSV", "*.csv")])
        self.csvLocation = file_path
        self.display_path.configure(text=os.path.basename(file_path))
        if self.display_path._text.endswith('.csv'):
            self.process_button.configure(state=NORMAL)
        else: self.process_button.configure(state=DISABLED)

    def c2j(self):
        createFolders()
        csv_to_json(self.csvLocation)
        delayTime(os.path.dirname(__file__), 'dict')
        jsonGenerator(self, self.csvLocation)

    def open_file(self):
        webbrowser.open(os.path.join(os.path.dirname(__file__), 'output'))

    def purgeF(self):
        thePath = os.path.dirname(__file__)
        delete_files(os.path.join(thePath, 'dict'))
        delete_files(os.path.join(thePath, 'source'))
        delete_files(os.path.join(thePath, 'output'))
        



if __name__ == '__main__':
    App()


#temp close button
#closeBtn = Button(self.mainframe, text='Close', font=('HelveticaNowDisplay-Black, 32'), command=root.quit)
#closeBtn.pack(pady=100)

'''
        #[START] fake title bar 
        root.overrideredirect(True) #deletes top bar

        def move_app(e):
            root.geometry(f'+{e.x_root-300}+{e.y_root-10}')

        title_bar = ctk.CTkFrame(root, bg_color=bgColor, border_width=0)
        title_bar.pack(fill=X)

        title_bar.bind("<B1-Motion>", move_app)

        title_lable = ctk.CTkLabel(title_bar, text="Whatsapp json Converter", fg_color='#03dac5', pady=10, font=('HelveticaNowDisplay-Black', 10))
        title_lable.pack(side=LEFT, pady=4)

        close_button = ctk.CTkButton(title_bar, text="  X  ", bg_color=bgColor, fg_color='red', border_width=0,command=root.quit)
        close_button.pack(side=RIGHT, pady=4)
        #[END] fake title bar 
        '''