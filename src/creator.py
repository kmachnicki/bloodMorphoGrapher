# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class Window(Frame):
    def __init__(self, root):
        self.root = root
        self.csv_file = "./data.csv"
        self.data = {}
        self.status_bar_text = StringVar()

        Frame.__init__(self, self.root)
        self.set_up_root_properties()
        self.create_menu_bar()
        self.create_input_frame()
        self.create_button_frame()
        self.create_status_bar()

    def set_up_root_properties(self):
        self.root.title("Creator")
        self.root.resizable(False, False)

    def create_menu_bar(self):
        menu_bar = Menu(self.root)
        self.root.config(menu = menu_bar)

        file_menu = Menu(menu_bar, tearoff = 0)
        file_menu.add_command(label = "Choose other input csv file", command = self.choose_csv_file)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.root.quit)
        menu_bar.add_cascade(label = "File", menu = file_menu)

        help_menu = Menu(menu_bar, tearoff = 0)
        help_menu.add_command(label = "Help", command = self.show_help_window)
        help_menu.add_command(label = "About", command = self.show_about_window)
        menu_bar.add_cascade(label = "Help", menu = help_menu)

    def create_input_frame(self):
        input_frame = Frame(self.root)
        input_frame.pack()

        row_index = 0
        for property in ["RBC","HGB","HCT","MCV","MCH","MCHC","RDW","PLT","PDW","MPV","WBC","PCT"]:
            label = Label(input_frame, text = property + ":")
            label.grid(row = row_index, sticky = E)
            entry = Entry(input_frame)
            entry.grid(row = row_index, column = 1)
            self.data[property] = entry
            row_index += 1

    def create_button_frame(self):
        button_frame = Frame(self.root)
        button_frame.pack(side = TOP)
        
        save_button = Button(button_frame, text = "Add data to csv", command = self.save_to_csv)
        save_button.grid(row = 0, column = 0)

    def create_status_bar(self):
        status_bar = Label(self.root, textvariable = self.status_bar_text, bd = 1, relief = SUNKEN, anchor = W)
        status_bar.pack(side = BOTTOM, fill = X)
        self.update_status_bar()

    def update_status_bar(self):
        self.status_bar_text.set(u"Selected csv: %s" % self.csv_file)

    def choose_csv_file(self):
        self.csv_file = askopenfilename(parent = self.root)
        self.update_status_bar()

    def show_help_window(self):
        help_window = Toplevel(self.root)
        button = Button(help_window, text="TODO1")
        button.pack()

    def show_about_window(self):
        about_window = Toplevel(self.root)
        button = Button(about_window, text="TODO2")
        button.pack()

    def save_to_csv(self):
        message_window = messagebox.showinfo("Info", "Saved to a file")

if __name__ == "__main__":
    root = Tk()
    window = Window(root)
    window.mainloop()
