import tkinter as tk

#Constantes
HEIGHT = 700
WIDTH = 1200
HEIGHT_FRAME = 700
WIDTH_FRAME = 700
BACKGROUND = "#50AA95" #Coueur hexa
FONT = "Helvetica"
FONT_SIZE = 20
BORDERWIDTH = 7

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Application MITEC')
        self.geometry("1200x700")
        self.widgets_init()

    def widgets_init(self):
        main_frame = tk.Frame(self, height = HEIGHT_FRAME, width = WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=tk.GROOVE, background=BACKGROUND)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.pack(side=tk.LEFT, padx=0, pady=0, expand=True, anchor='w')

        f_label = tk.Label(main_frame, text="Frequency", font=(FONT, FONT_SIZE))
        f_label.grid(row=0, column=0)

        f_entry = tk.Entry(main_frame, font=(FONT, FONT_SIZE))
        f_entry.grid(row=0, column=1)

window = Window()
window.mainloop()