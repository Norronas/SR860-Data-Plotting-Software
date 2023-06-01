import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

#Constantes
HEIGHT = 700
WIDTH = 1200
HEIGHT_FRAME = 700
WIDTH_FRAME = 400
BACKGROUND_MAIN_FRAME = "#6dd5db" #Coueur hexa
BACKGROUND_SECOND_FRAME = "#8fe6eb"
BACKGROUND_ENTRY = "#ffffff"
RELIEF = tk.GROOVE
FONT = "Helvetica"
FONT_SIZE = 14
BORDERWIDTH = 7
PADY_WIDGETS = 5 
PADX_WIDGETS = 5
MAX_ROW = 10

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Application MITEC')
        self.geometry("1200x700")
        self.widgets_init()

    def widgets_init(self):
        mode = tk.IntVar()
    
        self.main_frame = tk.Frame(self, height = HEIGHT_FRAME, width = WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND_MAIN_FRAME)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(MAX_ROW, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(MAX_ROW, weight=1)
        self.main_frame.pack(side=tk.LEFT, padx=0, pady=0, fill = tk.BOTH, expand=True, anchor='w')

        self.second_frame = tk.Frame(self, height = HEIGHT - HEIGHT_FRAME, width = WIDTH - WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND_SECOND_FRAME)
        self.second_frame.pack(side=tk.RIGHT, padx=0, pady=0, fill = tk.BOTH, expand=True, anchor='e')

        #self.button_frame = tk.Frame(self.main_frame, height = 50, width = WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND_SECOND_FRAME)
        #self.button_frame.pack(side=tk.BOTTOM, padx=0, pady=0, fill = tk.BOTH, expand=True, anchor='s')

        #Resistance widgets
        self.resistance_label = tk.Label(self.main_frame, text="Resistance (Ω)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.resistance_label.grid(row=0, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='sw')

        self.resistance_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.resistance_entry.grid(row=0, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='sw')

        #Current widgets
        self.current_label = tk.Label(self.main_frame, text="Current (A)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.current_label.grid(row=1, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.current_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.current_entry.grid(row=1, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Lenght widgets
        self.length_label = tk.Label(self.main_frame, text="Length ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.length_label.grid(row=2, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.length_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.length_entry.grid(row=2, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Width widgets
        self.width_label = tk.Label(self.main_frame, text="Width ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.width_label.grid(row=3, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.width_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.width_entry.grid(row=3, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Thermal Conductivity widgets
        self.thermal_cond_label = tk.Label(self.main_frame, text="Thermal Conductivity (W/m.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thermal_cond_label.grid(row=4, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.thermal_cond_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.thermal_cond_entry.grid(row=4, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Density widgets
        self.density_label = tk.Label(self.main_frame, text="Density (Kg/m3)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.density_label.grid(row=5, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.density_cond_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.density_cond_entry.grid(row=5, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Heat Capacity widgets
        self.heat_capa_label = tk.Label(self.main_frame, text="Heat Capacity (J/Kg.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.heat_capa_label.grid(row=6, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.heat_capa_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY)
        self.heat_capa_entry.grid(row=6, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Select Simulation
        
        self.first_mode = tk.Radiobutton(self.main_frame, text="First Mode", variable = mode, font=(FONT, FONT_SIZE), value = 0, bg=BACKGROUND_MAIN_FRAME,  indicatoron=0)
        self.first_mode.deselect()
        self.first_mode.grid(row=7, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.second_mode = tk.Radiobutton(self.main_frame, text="Second Mode", variable = mode, font=(FONT, FONT_SIZE), value = 1, bg=BACKGROUND_MAIN_FRAME,  indicatoron=0)
        self.second_mode.deselect()
        self.second_mode.grid(row=8, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.third_mode = tk.Radiobutton(self.main_frame, text="Third Mode", variable = mode, font=(FONT, FONT_SIZE), value = 2, bg=BACKGROUND_MAIN_FRAME, indicatoron=0)
        self.third_mode.deselect()
        self.third_mode.grid(row=9, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')
        
        #bouton = tk.Radiobutton(Frame1, variable=variable, text=wafers[i], value=i, background=BACKGROUND, indicatoron=0, command=afficher )

        #Simulation Button
        self.simu_button = tk.Button(self.main_frame, text="Start Simulation", font=(FONT, FONT_SIZE), bg=BACKGROUND_SECOND_FRAME)
        self.simu_button.grid(row=10, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='s')

    def canvas_draw(self, freq, reel, imag):
        figure_plot = Figure(figsize=(5,5), dpi = 100)
        figure_axis = figure_plot.add_subplot(111)
        figure_one = figure_axis.plot(freq, reel)
        figure_two = figure_axis.plot(freq, imag)
        figure_axis.set_xlabel("Frequency (ln(2w))")
        figure_axis.grid()
        #figure_plot.legend((figure_one, figure_two), ('Reel', 'Imaginary'), 'upper right')

        self.canvas = FigureCanvasTkAgg(figure_plot, self.second_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.draw()

        toolbar_plot = NavigationToolbar2Tk(self.canvas, self.second_frame)
        toolbar_plot.update()
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def main():
    window = Window()
    #window.current_entry.grid(row=1, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS)
    window.canvas_draw([1,2,3,4,5,6,7,8,9], [5,8,9,4,7,3,2,1,4], [4,7,5,-8,2,6,5,4,4])
    window.mainloop()

if __name__ == '__main__':
    main()