import main
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import matplotlib.patches as mpatches
from matplotlib.figure import Figure

#Constantes
HEIGHT = 700
HEIGHT_FRAME = 700
WIDTH_FRAME = 300
WIDTH = 1200
WIDTH_ENTRY = 12
BACKGROUND_MAIN_FRAME = "#6dd5db" #Coueur hexa 6dd5db
BACKGROUND_BUTTON = "#abe8eb"
BACKGROUND_ENTRY = "#ffffff"
RELIEF = tk.GROOVE
FONT = "Helvetica"
FONT_SIZE = 13
BORDERWIDTH = 7
PADY_WIDGETS = 5 
PADX_WIDGETS = 5
MAX_ROW = 15
MAX_COLUMN = 2

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('  3-Omega Helping Application')
        self.iconbitmap('icon.ico')
        self.geometry("1200x700")
        self.widgets_init()
        self.init_canvas()

    def widgets_init(self):
        #Constants
        self.mode = tk.StringVar()
        self.mode.set(1)
        self.var_status = tk.StringVar()
    
        #Frames
        self.main_frame = tk.Frame(self, height = HEIGHT_FRAME, width = WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND_MAIN_FRAME)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(MAX_ROW, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(MAX_COLUMN-1, weight=1)
        self.main_frame.grid_propagate(0)
        self.main_frame.pack(side=tk.LEFT, padx=0, pady=0, fill = tk.BOTH, expand=True, anchor='w')

        self.second_frame = tk.Frame(self, height = HEIGHT - HEIGHT_FRAME, width = WIDTH - WIDTH_FRAME, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND_BUTTON)
        self.main_frame.pack_propagate(0)
        self.second_frame.pack(side=tk.RIGHT, padx=0, pady=0, fill = tk.BOTH, expand=True, anchor='e')

        #Scrollbar
        self.scrollbar = tk.Scrollbar(self.main_frame)
        self.scrollbar.grid(column=2, sticky='e')

        #Resistance widgets
        self.resistance_label = tk.Label(self.main_frame, text="Resistance (Ω)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.resistance_label.grid(row=0, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='sw')

        self.resistance_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.resistance_entry.grid(row=0, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='se')

        #Current widgets
        self.current_label = tk.Label(self.main_frame, text="Current (A)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.current_label.grid(row=1, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.current_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.current_entry.grid(row=1, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Lenght widgets
        self.length_label = tk.Label(self.main_frame, text="Length ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.length_label.grid(row=2, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.length_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.length_entry.grid(row=2, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Width widgets
        self.width_label = tk.Label(self.main_frame, text="Width ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.width_label.grid(row=3, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.width_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.width_entry.grid(row=3, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Thermal Conductivity widgets
        self.thermal_cond_label = tk.Label(self.main_frame, text="Thermal Conductivity (W/m.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thermal_cond_label.grid(row=4, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.thermal_cond_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.thermal_cond_entry.grid(row=4, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Density widgets
        self.density_label = tk.Label(self.main_frame, text="Density (Kg/m3)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.density_label.grid(row=5, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.density_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.density_entry.grid(row=5, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Heat Capacity widgets
        self.heat_capa_label = tk.Label(self.main_frame, text="Heat Capacity (J/Kg.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.heat_capa_label.grid(row=6, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.heat_capa_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.heat_capa_entry.grid(row=6, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Thickness widgets
        self.thickness_label = tk.Label(self.main_frame, text="Thickness (m)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thickness_label.grid(row=7, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.thickness_entry = tk.Entry(self.main_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY)
        self.thickness_entry.grid(row=7, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='e')

        #Status Label
        self.var_status.set("Status : Enter parameters")
        self.thickness_label = tk.Label(self.main_frame, textvariable=self.var_status, font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.thickness_label.grid(row=8, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        #Select Simulation
        
        self.first_mode = tk.Radiobutton(self.main_frame, text="Semi-Infinite Substrate", variable = self.mode, font=(FONT, FONT_SIZE), value = 0, bg=BACKGROUND_BUTTON,  indicatoron=0, command=lambda:self.get_value_mode())
        self.first_mode.deselect()
        self.first_mode.grid(row=9, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.second_mode = tk.Radiobutton(self.main_frame, text="Finite Substrate Adiabaticisothermal", variable = self.mode, font=(FONT, FONT_SIZE), value = 1, bg=BACKGROUND_BUTTON,  indicatoron=0, command=lambda:self.get_value_mode())
        self.second_mode.deselect()
        self.second_mode.grid(row=10, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')

        self.third_mode = tk.Radiobutton(self.main_frame, text="Finite Substrate Isothermal", variable = self.mode, font=(FONT, FONT_SIZE), value = 2, bg=BACKGROUND_BUTTON, indicatoron=0, command=lambda:self.get_value_mode())
        self.third_mode.deselect()
        self.third_mode.grid(row=11, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='w')
        
        #bouton = tk.Radiobutton(Frame1, variable=variable, text=wafers[i], value=i, background=BACKGROUND, indicatoron=0, command=afficher )

        #Simulation Button
        #self.simu_button = tk.Button(self.main_frame, text="Start Simulation", font=(FONT, FONT_SIZE), bg=BACKGROUND_SECOND_FRAME, command = lambda: main.point_calculation(11.212, 0.028907, 0.0025, 0.000034/2, 0.297, 1350, 1300, 0.0004, self))
        # self.simu_button = tk.Button(self.main_frame, text="Start Simulation", font=(FONT, FONT_SIZE), bg=BACKGROUND_SECOND_FRAME, command = lambda:main.point_calculation(float(self.resistance_entry.get()),
        #                                                                                                                                                            float(self.current_entry.get()),
        #                                                                                                                                                            float(self.length_entry.get()),
        #                                                                                                                                                            float(self.width_entry.get())/2,
        #                                                                                                                                                            float(self.thermal_cond_entry.get()),
        #                                                                                                                                                            float(self.density_entry.get()),
        #                                                                                                                                                            float(self.heat_capa_entry.get()),
        #                                                                                                                                                            float(self.thickness_entry.get()),
        #           
        self.simu_button = tk.Button(self.main_frame, text="Start Simulation", width=160 ,font=(FONT, FONT_SIZE), bg=BACKGROUND_BUTTON, command = lambda:main.zero_verification(self.length_entry.get(),
                                                                                                                                                                            self.thermal_cond_entry.get(),
                                                                                                                                                                            self.density_entry.get(),
                                                                                                                                                                            self.heat_capa_entry.get(),
                                                                                                                                                                            self))
        self.simu_button.grid(row=12, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='sw')

        # Clear Button
        self.clear_button = tk.Button(self.main_frame, text="Clear Plot", width=140, font=(FONT, FONT_SIZE), bg=BACKGROUND_BUTTON, command = lambda: self.clear_canvas())
        self.clear_button.grid(row=12, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='se')
    
    def init_canvas(self):
        self.figure_plot = Figure(figsize=(6,6), dpi = 100) 
        self.figure_axis = self.figure_plot.add_subplot(111)
        self.figure_axis.set_xlabel("Frequency (ln(2w))")
        self.figure_axis.set_autoscalex_on(True)
        self.figure_axis.grid()

        self.canvas = FigureCanvasTkAgg(self.figure_plot, self.second_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar_plot = NavigationToolbar2Tk(self.canvas, self.second_frame)
        toolbar_plot.update()
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def canvas_draw(self, freq, reel, imag):
        self.figure_one = self.figure_axis.plot(freq, reel)
        self.figure_two = self.figure_axis.plot(freq, imag)   
        reel_legend = mpatches.Patch(color='blue', label='Reel')
        imag_legend = mpatches.Patch(color='orange', label='Imaginary')
        self.figure_axis.grid()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.draw()
        self.canvas.blit()
        self.figure_axis.legend(handles = [reel_legend, imag_legend])


    def get_value_mode(self):
        value_mode = self.mode.get()
        return value_mode
    

    def clear_canvas(self):
        return 0

        # self.figure_plot.clear()
        # self.figure_plot.add_subplot(111)         
        # self.canvas.draw_idle()
        # self.figure_axis.grid()

        # for item in self.canvas.get_tk_widget().find_all():
        #     self.canvas.get_tk_widget().delete(item)
        #self.toolbar_plot.get_tk_widget().delete()


    def modify_status(self, event):
        if (event == 1):
            self.var_status.set("Status : Simulation Completed")
        if (event == 2):
            self.var_status.set("Status : Necessary parameters empty")
        if (event == 3):
            self.var_status.set("Status : Parameters equal to zero")