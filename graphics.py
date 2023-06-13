import main
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image, ImageTk

#Constantes
HEIGHT = 700
HEIGHT_FRAME = 700
HEIGHT_SCROLLBAR = 1500
WIDTH = 700
WIDTH_FRAME = 700
WIDTH_ENTRY = 12
WIDTH_BUTTON = 40
WIDTH_RADIOBUTTON_LAYER = 20
WIDTH_RADIOBUTTON_MODE = 40
BACKGROUND_MAIN_FRAME = "#6dd5db"
BACKGROUND_BUTTON = "#abe8eb"
BACKGROUND_ENTRY = "#ffffff"
RELIEF = tk.GROOVE
FONT = "Helvetica"
SEPARATOR = "-----------------------------------------------------------------"
COPYRIGHT = "© 2023 Cazin Némo. TOUS DROITS RÉSERVÉS"
FONT_SIZE = 16
BORDERWIDTH = 7
PADY_WIDGETS = 5 
PADX_WIDGETS = 5
MAX_ROW = 30
MAX_COLUMN = 2
DISABLE_COLOR = "light gray"

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('  3-Omega Helping Software')
        try:
            self.iconbitmap('icon.ico')
        except:
            print("Could not load the icon")
        self.geometry("700x700")
        self.widgets_init()
        self.init_canvas()
        self.layer_lock()

    def widgets_init(self):

        #Constants
        self.mode_var = tk.StringVar()
        self.mode_var .set(3)
        self.layer_var = tk.StringVar()
        self.layer_var.set(0)
        self.var_fmin_result = tk.StringVar()
        self.var_fmin_result.set("   Result Fmin :")
        self.var_fmax_result = tk.StringVar()
        self.var_fmax_result.set("   Result Fmax :")
        self.var_status = tk.StringVar()
        
        #Canvas & Scollbar
        self.canvas_und = tk.Canvas(self, width=WIDTH_FRAME, height=HEIGHT_FRAME, scrollregion=(0,0,HEIGHT_SCROLLBAR,HEIGHT_SCROLLBAR), background=BACKGROUND_MAIN_FRAME)
        self.canvas_und.bind_all("<MouseWheel>", self._on_mousewheel)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas_und.yview)
        self.canvas_und.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,sticky='nsw')
        self.canvas_und.grid(row=0,column=0,sticky='nws')
        self.canvas_frame = tk.Frame(self.canvas_und, width=WIDTH_FRAME, height=3000, borderwidth=BORDERWIDTH, relief=RELIEF, background=BACKGROUND_MAIN_FRAME)
        self.canvas_frame.grid_rowconfigure(0, weight=1)
        self.canvas_frame.grid_rowconfigure(MAX_ROW, weight=1)
        self.canvas_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame.grid_columnconfigure(MAX_COLUMN-1, weight=1)
        # self.canvas_frame.grid_propagate(0)
        self.canvas_und.create_window(0, 0, anchor='nw', height=HEIGHT_SCROLLBAR, width=WIDTH_FRAME, window=self.canvas_frame)

        #Layers widgets
        self.layer_label = tk.Label(self.canvas_frame, text="Layers :", font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.layer_label.grid(row=0, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='sw')

        self.layer1_radiobutton = tk.Radiobutton(self.canvas_frame, text="Layer 1", width=WIDTH_RADIOBUTTON_LAYER, variable = self.layer_var, font=(FONT, FONT_SIZE), value = 1, bg=BACKGROUND_BUTTON,  indicatoron=0, command=lambda:self.layer_lock())
        self.layer1_radiobutton.deselect()
        self.layer1_radiobutton.grid(row=1, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.layer2_radiobutton = tk.Radiobutton(self.canvas_frame, text="Layer 2", width=WIDTH_RADIOBUTTON_LAYER, variable = self.layer_var, font=(FONT, FONT_SIZE), value = 2, bg=BACKGROUND_BUTTON,  indicatoron=0, command=lambda:self.layer_lock())
        self.layer2_radiobutton.deselect()
        self.layer2_radiobutton.grid(row=2, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        #Separator
        self.separator1_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator1_label.grid(row=3, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        #######################
        ### GENERAL WIDGETS ###
        #######################

        #General Label widget
        self.general_settings_label = tk.Label(self.canvas_frame, text="General Settings", font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.general_settings_label.grid(row=4, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        #Resistance widgets
        self.resistance_label = tk.Label(self.canvas_frame, text="   Resistance (Ω)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.resistance_label.grid(row=5, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        self.resistance_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.resistance_entry.grid(row=5, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Current widgets
        self.current_label = tk.Label(self.canvas_frame, text="   Current (A)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.current_label.grid(row=6, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.current_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.current_entry.grid(row=6, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Lenght widgets
        self.length_label = tk.Label(self.canvas_frame, text="   Length ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.length_label.grid(row=7, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.length_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.length_entry.grid(row=7, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Width widgets
        self.width_label = tk.Label(self.canvas_frame, text="   Width ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.width_label.grid(row=8, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.width_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.width_entry.grid(row=8, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #TCR widgets
        self.tcr_label = tk.Label(self.canvas_frame, text="   TCR ()", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.tcr_label.grid(row=9, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.tcr_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.tcr_entry.grid(row=9, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')
        self.tcr_entry.insert(0, "0.003")

        #Separator
        self.separator2_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator2_label.grid(row=10, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        #######################
        ### LAYER 1 WIDGETS ###
        #######################

        #Layer 1 Label widget
        self.layer1_settings_label = tk.Label(self.canvas_frame, text="Layer 1 Settings", font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.layer1_settings_label.grid(row=11, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        #Thermal Conductivity Layer 1 widgets
        self.thermal_cond1_label = tk.Label(self.canvas_frame, text="   Thermal Conductivity (W/m.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thermal_cond1_label.grid(row=12, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.thermal_cond1_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.thermal_cond1_entry.grid(row=12, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Density Layer 1 widgets
        self.density1_label = tk.Label(self.canvas_frame, text="   Density (Kg/m3)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.density1_label.grid(row=13, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.density1_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.density1_entry.grid(row=13, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Heat Capacity Layer 1 widgets
        self.heat_capa1_label = tk.Label(self.canvas_frame, text="   Heat Capacity (J/Kg.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.heat_capa1_label.grid(row=14, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.heat_capa1_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.heat_capa1_entry.grid(row=14, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Thickness Layer 1 widgets
        self.thickness1_label = tk.Label(self.canvas_frame, text="   Thickness (m)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thickness1_label.grid(row=15, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.thickness1_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.thickness1_entry.grid(row=15, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Separator
        self.separator3_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator3_label.grid(row=16, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        #######################
        ### LAYER 2 WIDGETS ###
        #######################

        #Layer 2 Label widget
        self.layer2_settings_label = tk.Label(self.canvas_frame, text="Layer 2 Settings", font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.layer2_settings_label.grid(row=17, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        #Thermal Conductivity Layer 2 widgets
        self.thermal_cond2_label = tk.Label(self.canvas_frame, text="   Thermal Conductivity (W/m.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thermal_cond2_label.grid(row=18, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.thermal_cond2_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.thermal_cond2_entry.grid(row=18, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Density Layer 2 widgets
        self.density2_label = tk.Label(self.canvas_frame, text="   Density (Kg/m3)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.density2_label.grid(row=19, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.density2_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.density2_entry.grid(row=19, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Heat Capacity Layer 2 widgets
        self.heat_capa2_label = tk.Label(self.canvas_frame, text="   Heat Capacity (J/Kg.K)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.heat_capa2_label.grid(row=20, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.heat_capa2_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.heat_capa2_entry.grid(row=20, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Thickness Layer 2 widgets
        self.thickness2_label = tk.Label(self.canvas_frame, text="   Thickness (m)", font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.thickness2_label.grid(row=21, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.thickness2_entry = tk.Entry(self.canvas_frame, font=(FONT, FONT_SIZE), bg=BACKGROUND_ENTRY, width=WIDTH_ENTRY, disabledbackground=DISABLE_COLOR)
        self.thickness2_entry.grid(row=21, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        #Separator
        self.separator4_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator4_label.grid(row=22, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        ################################
        ### SIMULATION MODE SELECTOR ###
        ################################

        #Simulation Mode Choice Label widget
        self.sim_mode_choice_label = tk.Label(self.canvas_frame, text="Simulation Mode Choice", font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.sim_mode_choice_label.grid(row=23, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')    

        #Select Simulation widgets
        
        self.first_mode = tk.Radiobutton(self.canvas_frame, text="Semi-Infinite Substrate", width=WIDTH_RADIOBUTTON_MODE, variable = self.mode_var, font=(FONT, FONT_SIZE), value = 0, bg=BACKGROUND_BUTTON,  indicatoron=0, command=lambda:self.delock_sim_button())
        self.first_mode.deselect()
        self.first_mode.grid(row=24, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.second_mode = tk.Radiobutton(self.canvas_frame, text="Finite Substrate Adiabaticisothermal", width=WIDTH_RADIOBUTTON_MODE, variable = self.mode_var, font=(FONT, FONT_SIZE), value = 1, bg=BACKGROUND_BUTTON,  indicatoron=0, command=lambda:self.delock_sim_button())
        self.second_mode.deselect()
        self.second_mode.grid(row=25, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        self.third_mode = tk.Radiobutton(self.canvas_frame, text="Finite Substrate Isothermal", width=WIDTH_RADIOBUTTON_MODE, variable = self.mode_var, font=(FONT, FONT_SIZE), value = 2, bg=BACKGROUND_BUTTON, indicatoron=0, command=lambda:self.delock_sim_button())
        self.third_mode.deselect()
        self.third_mode.grid(row=26, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        #Separator
        self.separator5_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator5_label.grid(row=27, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        ################################
        ###       RESULT LABEL       ###
        ################################

        #Results Title Label widget
        self.result_label = tk.Label(self.canvas_frame, text="Results :", font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.result_label.grid(row=28, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')  

        #Fmin result Label widget
        self.fmin_result_label = tk.Label(self.canvas_frame, textvariable=self.var_fmin_result, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.fmin_result_label.grid(row=29, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')
        
        #Fmax result Label widget
        self.fmax_result_label = tk.Label(self.canvas_frame, textvariable=self.var_fmax_result, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.fmax_result_label.grid(row=30, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        #Separator
        self.separator6_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator6_label.grid(row=31, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        ################################
        ###         BUTTONS          ###
        ################################

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
        self.simu_button = tk.Button(self.canvas_frame, text="Start Simulation", width=WIDTH_BUTTON ,font=(FONT, FONT_SIZE), bg=BACKGROUND_BUTTON, command = lambda:main.zero_verification(self.length_entry.get(),
                                                                                                                                                                            self.thermal_cond1_entry.get(),
                                                                                                                                                                            self.density1_entry.get(),
                                                                                                                                                                            self.heat_capa1_entry.get(),
                                                                                                                                                                            self))
        self.simu_button.grid(row=32, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        #Lockin Button
        self.lockin_button = tk.Button(self.canvas_frame, text="Lockin Collect Data", width=WIDTH_BUTTON-20, font=(FONT, FONT_SIZE), bg=BACKGROUND_BUTTON, command = lambda:main.collect_data_lockin(self))
        self.lockin_button.grid(row=32, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='ne')

        self.separator7_label = tk.Label(self.canvas_frame, text=SEPARATOR, font=(FONT, FONT_SIZE), bg=BACKGROUND_MAIN_FRAME)
        self.separator7_label.grid(row=33, column=0, padx=PADX_WIDGETS,pady=PADY_WIDGETS, sticky='nw')

        ################################
        ###        COPYRIGHT         ###
        ################################

        self.copyright_label = tk.Label(self.canvas_frame, text=COPYRIGHT, font=(FONT, FONT_SIZE-4, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        self.copyright_label.grid(row=34, column=0, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')

        try:
            self.img = ImageTk.PhotoImage(Image.open("IEMN_logo.png"))
            self.panel = tk.Label(self.canvas_frame, image=self.img, background=BACKGROUND_MAIN_FRAME)
            self.panel.photo = self.img
            self.panel.grid(row=34, column=1, padx=PADX_WIDGETS, pady=PADY_WIDGETS, sticky='nw')
        except:
            print("Couldn't load the IEMN picture")

    def init_canvas(self):
        plt.figure(figsize=(6,6)) 
        plt.subplot(111)
        plt.xlabel("ln(2w)")
        plt.ylabel("Voltage 3w (mV)")


    def canvas_draw(self, freq, reel, imag):
        self.figure_one = plt.plot(freq, reel, color ='Blue', label ='Reel')
        self.figure_two = plt.plot(freq, imag, color ='Green', label ='Imag')
        reel_legend = mpatches.Patch(color='Blue', label='Reel')
        imag_legend = mpatches.Patch(color='Green', label='Imaginary')   
        plt.legend(handles = [reel_legend, imag_legend])
        plt.show()


    def freq_change_label_value(self, fmin, fmax):
        self.var_fmin_result.set("   Result Fmin : " + str(round(fmin, 2)) + " Hz")
        self.var_fmax_result.set("   Result Fmax : " + str(round(fmax, 2)) + " Hz")


    def canvas_draw_freq(self, fmin, fmax):
        self.fmin_plot = plt.axvline(x=fmin, color = 'gray', linestyle='--')
        self.fmax_plot = plt.axvline(x=fmax, color = 'gray', linestyle='--')


    def canvas_draw_data_points(self, reel, imag, freq):
        self_data_real_plot = plt.plot(freq, reel, marker="o", color ='Red')
        self_data_imag_plot = plt.plot(freq, imag, marker="o", color ='Purple')


    def get_value_mode(self):
        value_mode = self.mode_var.get()
        return value_mode
    

    def get_value_layer(self):
        value_layer = self.layer_var.get()
        return value_layer
    

    def layer_lock(self):
        #LAYER 1 CHOSEN
        if(int(self.get_value_layer()) == 1):                
            self.resistance_entry.config(state= "normal")
            self.current_entry.config(state= "normal")
            self.length_entry.config(state= "normal")
            self.width_entry.config(state= "normal")
            self.tcr_entry.config(state= "normal")

            self.thermal_cond1_entry.config(state= "normal")
            self.density1_entry.config(state= "normal")
            self.heat_capa1_entry.config(state= "normal")
            self.thickness1_entry.config(state= "normal")

            self.thermal_cond2_entry.delete(0, 'end')
            self.density2_entry.delete(0, 'end')
            self.heat_capa2_entry.delete(0, 'end')
            self.thickness2_entry.delete(0, 'end')

            self.thermal_cond2_entry.config(state= "disabled")
            self.density2_entry.config(state= "disabled")
            self.heat_capa2_entry.config(state= "disabled")
            self.thickness2_entry.config(state= "disabled")

            self.delock_sim_button()

        #LAYER 2 CHOSEN
        elif(int(self.get_value_layer()) == 2):                 
            self.resistance_entry.config(state= "normal")
            self.current_entry.config(state= "normal")
            self.length_entry.config(state= "normal")
            self.width_entry.config(state= "normal")
            self.tcr_entry.config(state= "normal")

            self.thermal_cond1_entry.config(state= "normal")
            self.density1_entry.config(state= "normal")
            self.heat_capa1_entry.config(state= "normal")
            self.thickness1_entry.config(state= "normal")

            self.thermal_cond2_entry.config(state= "normal")
            self.density2_entry.config(state= "normal")
            self.heat_capa2_entry.config(state= "normal")
            self.thickness2_entry.config(state= "normal")

            self.delock_sim_button()

        #ALL DISABLE BY DEFAULT
        else:
            self.resistance_entry.config(state= "disabled")
            self.current_entry.config(state= "disabled")
            self.length_entry.config(state= "disabled")
            self.width_entry.config(state= "disabled")
            self.tcr_entry.config(state= "disabled")

            self.thermal_cond1_entry.config(state= "disabled")
            self.density1_entry.config(state= "disabled")
            self.heat_capa1_entry.config(state= "disabled")
            self.thickness1_entry.config(state= "disabled")

            self.thermal_cond2_entry.config(state= "disabled")
            self.density2_entry.config(state= "disabled")
            self.heat_capa2_entry.config(state= "disabled")
            self.thickness2_entry.config(state= "disabled")

            self.simu_button.config(state= "disabled")

    def delock_sim_button(self):
        if((int(self.get_value_layer()) != 0) and (int(self.get_value_mode()) != 3)):
            self.simu_button.config(state= "normal")

    def _on_mousewheel(self, event):
        self.canvas_und.yview_scroll(int(-1*(event.delta/120)), "units")


    def create_error_window(self, error_level):
        errow_window = tk.Toplevel(self, background=BACKGROUND_MAIN_FRAME)
        try:
            self.iconbitmap('icon.ico')
        except:
            print("Could not load the icon")
        self.geometry("1200x700")
        errow_window.title("   Error")
        error_label = tk.Label(errow_window, textvariable=self.var_status, font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_MAIN_FRAME)
        error_label.pack(side=tk.LEFT, padx=0, pady=0, fill = tk.BOTH, expand=True)
        if (error_level == 1):
            self.var_status.set("Status : Cannot connect to the lockin amplifier")
            self.lockin_button.config(state= "disabled")
        if (error_level == 2):
            self.var_status.set("Status : Necessary parameters empty")
        if (error_level == 3):
            self.var_status.set("Status : Parameters equal to zero")