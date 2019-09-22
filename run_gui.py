import tkinter as tk
from tkinter import ttk

# TODO
# Validate inputs
# use actual file input
# Make it look nice

class MusicMaterializerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.tempo = 0
        self.master = master

        self.initialize_widgets()
        self.pack()
    
    def initialize_widgets(self):
        self.tempo_var = tk.StringVar()
        self.tempo_input = ttk.Entry(self)
        self.tempo_input['textvariable'] = self.tempo_var
        self.tempo_input.grid(row=0, column=1)

        self.tempo_input_label = ttk.Label(self)
        self.tempo_input_label['text'] = 'Tempo of piece'
        self.tempo_input_label.grid(row=0, column=0)
        self.audio_file_entry = ttk.Entry(self)

        self.audio_file_input_label = ttk.Label(self)
        self.audio_file_input_label['text'] = 'Audio file'
        self.audio_file_input_label.grid(row=1, column=0)

        self.audio_file_var = tk.StringVar()
        self.audio_file_entry = ttk.Entry(self)
        self.audio_file_entry['textvariable'] = self.audio_file_var
        self.audio_file_entry.grid(row=1, column=1)

        self.run_button = ttk.Button(self)
        self.run_button['command'] = self.run_analysis
        self.run_button['text'] = "Run Analyses"
        self.run_button.grid(row=2)


    def run_analysis(self):
        print(self.tempo_var.get())
        print(self.audio_file_var.get())

root = tk.Tk()
app = MusicMaterializerGUI(master=root)
app.mainloop()
