# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class Window(Frame):
    def __init__(self, root):
        self.root = root
        Frame.__init__(self, self.root)
        self.root.title("Creator")
        self.root.resizable(False, False)

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

        input_frame = Frame(self.root)
        input_frame.pack()

        button_frame = Frame(self.root)
        button_frame.pack(side = TOP)
        
        #date;RBC;HGB;HCT;MCV;MCH;MCHC;RDW;PLT;PDW;MPV;WBC;PCT
        RBC_label = Label(input_frame, text = "RBC:")
        RBC_label.grid(row = 0, sticky = E)
        RBC_entry = Entry(input_frame)
        RBC_entry.grid(row = 0, column = 1)

        HGB_label = Label(input_frame, text = "HGB:")
        HGB_label.grid(row = 1, sticky = E)
        HGB_entry = Entry(input_frame)
        HGB_entry.grid(row = 1, column = 1)

        save_button = Button(button_frame, text = "Add data to csv", command = self.save_to_csv)
        save_button.grid(row = 0, column = 0)

        status_bar = Label(self.root, text = "Status", bd = 1, relief = SUNKEN, anchor = W)
        status_bar.pack(side = BOTTOM, fill = X)

    def choose_csv_file(self):
        csv_filename = askopenfilename()
        print("Filename: %s" % filename)

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
