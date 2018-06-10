# -*- coding:utf-8 -*-

from os import fstat
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from csv import DictWriter

class Window(Frame):
    def __init__(self, root):
        self.root = root
        self.csv_filename = "./data.csv"
        self.data = {}
        self.status_bar_text = StringVar()
        self.header = ["date", "RBC", "HGB", "HCT", "MCV", "MCH", "MCHC", "RDW", "PLT", "PDW", "MPV", "WBC", "PCT"]

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
        self.root.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Choose other input CSV file", command=self.choose_csv_file)
        file_menu.add_command(label="Choose parsed OCR file to fill data", command=self.process_ocr_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help", command=self.show_help_window)
        help_menu.add_command(label="About", command=self.show_about_window)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def create_input_frame(self):
        input_frame = Frame(self.root)
        input_frame.pack()

        row_index = 0
        for probe in self.header:
            label = Label(input_frame, text=probe + ":")
            label.grid(row=row_index, sticky=E, padx=2, pady=2)
            entry = Entry(input_frame)
            entry.grid(row=row_index, column=1, padx=2, pady=2)
            self.data[probe] = entry
            row_index += 1

    def create_button_frame(self):
        button_frame = Frame(self.root)
        button_frame.pack(side=TOP)

        save_button = Button(button_frame, text="Add data to CSV", command=self.save_to_csv)
        save_button.grid(row=0, column=1, padx=5, pady=5)

    def create_status_bar(self):
        status_bar = Label(self.root, textvariable=self.status_bar_text, bd=1, relief=SUNKEN, anchor=W)
        status_bar.pack(side=BOTTOM, fill=X)
        self.update_status_bar()

    def update_status_bar(self):
        self.status_bar_text.set(u"Selected CSV: %s" % self.csv_filename)

    def show_help_window(self):
        help_window = Toplevel(self.root)
        button = Button(help_window, text="TODO1")
        button.pack()

    def show_about_window(self):
        about_window = Toplevel(self.root)
        button = Button(about_window, text="TODO2")
        button.pack()

    def choose_csv_file(self):
        self.csv_filename = askopenfilename(parent=self.root)
        self.update_status_bar()

    @staticmethod
    def replace_entry_value(entry, value):
        if value is not None:
            entry.delete(0, END)
            entry.insert(0, value)

    def process_ocr_file(self):
        ocr_filename = askopenfilename(parent=self.root)
        with open(ocr_filename, "r") as ocr_file:
            ocr_data = ocr_file.read()
            date_match = re.search("(?:Data \D*: )(\d{2}-\d{2}-\d{4})", ocr_data)
            if date_match is not None:
                extracted_date = date_match.group(1)
                self.replace_entry_value(self.data["date"], extracted_date)
            for (key, input_field) in self.data.items():
                if key != "date":
                    parameter_match = re.search("(?:%s \[\D*\] )(\d{1,4}.?\d{1,4})" % key, ocr_data)
                    if parameter_match is not None:
                        extracted_value = parameter_match.group(1)
                        self.replace_entry_value(input_field, extracted_value)

    def is_data_valid(self):
        try:
            for (key, input_field) in self.data.items():
                if key != "date":
                    float(input_field.get().replace(",", "."))
            return True
        except ValueError:
            return False

    def save_data(self, row_values):
        with open(self.csv_filename, "a+", newline="", encoding="utf8") as csv_file:
            file_size = fstat(csv_file.fileno()).st_size
            writer = DictWriter(csv_file, delimiter=";", fieldnames=self.header)
            if file_size == 0:
                writer.writeheader()
            writer.writerow(row_values)

    def save_to_csv(self):
        if self.is_data_valid():
            row_values = {key: input_field.get().replace(",", ".") for (key, input_field) in self.data.items()}
            self.save_data(row_values)
            messagebox.showinfo("Info", "Saved to a file.")
        else:
            messagebox.showerror("Error", "Saving unsuccessful. Empty fields or wrongly formatted data.")

if __name__ == "__main__":
    root = Tk()
    window = Window(root)
    window.mainloop()
