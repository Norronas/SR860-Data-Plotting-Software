# 3-Omega Helping Software by Némo CAZIN

## Some details on this project

This software was developed during my 4-week internship in the 3rd year of the Embedded Systems course at Polytech Lille. 
This internship was carried out in the MITEC research group of the IEMN laboratory (Institute of Electronics, Microelectronics and Nanotechnology).

## Resume of this software

This software can be used to carry out theoretical characterisation of polymer materials and plot graphs of the results obtained. 
It can also receive data from an SR860 lock-in amplifier and add it to the graphs.
As this software is intended for a research laboratory, some of the formulas can be complex to understand
Then, this software mainly uses the tkinter graphics library and the cmath and sympy mathematics libraries. 
The pyvisa library is slightly used to communicate with the SR860 lock-in amplifier. 
Finaly, the matplotlib library is also used for the display of equation results.

### Preparation before use

You can use the software as is, but you may not be able to use all its functions, such as amplifier data retrieval, unless you have the NI-VISA driver installed. 
First, connect the amplifier to your computer using the USB-A to USB-B cable. 
If your operating system doesn't recognize the amplifier in the device manager, you'll need to download the NI-VISA driver.
You can download the NI-VISA driver here: **_https://www.ni.com/fr-fr/support/downloads/drivers/download.ni-visa.html#329456_**
Choose the same operating system as your computer and for the driver version, choose : 
- 19.5 for **Windows**
- 2022 Q4 for **MAC OS**
- 2023 Q2 for **Linux**
When selecting driver extensions, uncheck those related to Labview and example C programs.
To check that the driver works and is correctly installed, launch the NI MAX applicator. 
You'll then see a panel on the left with the label *"Peripherals and interfaces"*. 
If you find the amplifier, you can use the software to its full potential.  

### Easy use of the software

An executable file is available to launch the application. 
You will then need to choose the number of layers to match your materials and insert the parameters for each layer.
After that, simply press the *"Simulate"* button to obtain the graph. 
You can also press the *"Lockin Collect Data"* button to retrieve data from the amplifier (if connected) and add it to the graph.

## Details about the code

### Main file

This part of the code performs all the calculations required for the application to function correctly. 
It also provides the link between the calculations made and their display, thanks to the graphics section that we'll explain next. 
It can also communicate with the amplifier and retrieve data from it.
The integration formulas named *"function"* in the file are very long because, ν being the variable of integration, we can't call on other equations. 
Therefore, we are obliged to replace each variable one by one by its calculation, hence the length of certain lines of code.
The equations used are commented on for a better understanding.


### Graphic file

The graphical part of the code is made up of a single class, the window class, containing each widget and its display. 
Functions are provided to display the results curves using the matplotlib library. 
If you want to add widgets to the graphics, you need to change the value of *"row "* and *"column "* so that the widgets follow each other. 
If you add a widget between two, don't forget to change the value of the following ones, otherwise they'll overwrite the new one.


### Setup file 

This file is used to create a program executable. There's nothing to change in this file unless you want to upgrade the program and use new Python libraries.
To create the executable, open a command terminal or use the VSCode terminal, and place yourself in the same directory as the *"setup.py"* file.
Then issue this command (several versions exist, depending on the version of Python you've downloaded) : 
- **py -m setup build**
or
- **python -m setup build**
*PS : Executable creation takes about 1~2 minutes*
If a recursion error occurs, change this line of code *"sys.setrecursionlimit(sys.getrecursionlimit() * 5)"* to *"sys.setrecursionlimit(20000)"*.
After this, a *"build"* file will be created in the current directory, with the executable created inside. 
Icons and images will not be displayed, so move the *"icon.ico"* and *"IEMN_logo"* files to the same directory as the executable.
You now have a perfectly usable executable.

## In case of an equipment change

If the amplifier is changed, the identifier must be changed in the source code and a new executable created using the *"setup.py"* file.
To change the identifier, use NI MAX and in *"Peripherals and interface"*, you'll find the new identifier. 
Copy it and replace it in the *"main.py"* code in the AMPLIFIER_ID constant.
Depending on the amplifier model you're using, you may need to modify the commands to be sent to the amplifier. 
Refer to the manual for your new amplifier in the *"Data Transfer Commands"* section and find the commands to be replaced in the
*"collect_data_lockin"* function in the *"main.py"* file.

## Conclusion

This software is easy to use but is reserved for experienced users of the 3 omega method. The code is complex, but allows you to do a lot of things and help the user in his manipulation. 

© 2023 Cazin Némo. TOUS DROITS RÉSERVÉS