import tkinter as tk

#Constantes
HEIGHT = 700
WIDTH = 1200
HEIGHT_FRAME = 700
WIDTH_FRAME = 700
BACKGROUND = "#50AA95" #Coueur hexa
RELIEF = tk.GROOVE
FONT = "Helvetica"
FONT_SIZE = 20
BORDERWIDTH = 7
PADY_WIDGETS = 5 
PADX_WIDGETS = 5

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Application MITEC')
        self.geometry("1200x700")
        self.widgets_init()

    def widgets_init(self):
        main_frame = tk.Frame(self, height = HEIGHT_FRAME, width = WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.pack(side=tk.LEFT, padx=0, pady=0, expand=True, anchor='w')

        resistance_label = tk.Label(main_frame, text="Resistance", font=(FONT, FONT_SIZE), background=BACKGROUND)
        resistance_label.grid(row=0, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS)

        resistance_entry = tk.Entry(main_frame, font=(FONT, FONT_SIZE))
        resistance_entry.grid(row=0, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS)

        current_label = tk.Label(main_frame, text="Current", font=(FONT, FONT_SIZE), background=BACKGROUND)
        current_label.grid(row=1, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS)

        current_entry = tk.Entry(main_frame, font=(FONT, FONT_SIZE))
        current_entry.grid(row=1, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS)

window = Window()
window.mainloop()