# 3-Omega Helping Software by Némo CAZIN

## Some details on this project

This software was developed during my 4-week internship in the 3rd year of the Embedded Systems course at Polytech Lille. This internship was carried out in the MITEC research group of the IEMN laboratory (Institute of Electronics, Microelectronics and Nanotechnology).

## Resume of this software

This software can be used to carry out theoretical characterisation of polymer materials and plot graphs of the results obtained. It can also receive data from an SR860 lock-in amplifier and add it to the graphs.
As this software is intended for a research laboratory, some of the work on the software has been removed to remain confidential.
Finally, this software mainly uses the tkinter graphics library and the cmath, sympy and numpy mathematics libraries. The pyvisa library is slightly used to communicate with the SR860 lock-in amplifier. Finaly, the matplotlib library is also used for the display of equation results.

### Preparation before use

You can use the software as is, but you may not be able to use all its functions, such as amplifier data retrieval, unless you have the NI-VISA driver installed. First, connect the amplifier to your computer using the USB-A to USB-B cable. If your operating system doesn't recognize the amplifier in the device manager, you'll need to download the NI-VISA driver.
You can download the NI-VISA driver here: https://www.ni.com/fr-fr/support/downloads/drivers/download.ni-visa.html#329456
To check that the driver works and is correctly installed, launch the NI MAX applicator. You'll then see a panel on the left with the label "Peripherals and interfaces". If you find the amplifier, you can use the software to its full potential.  

### Easy use of the software

An executable file is available to launch the application. You will then need to choose the number of layers to match your materials and insert the parameters for each layer.
After that, simply press the "Simulate" button to obtain the graph. You can also press the "Lockin Collect Data" button to retrieve data from the amplifier and add it to the graph.

## Details about the code

### Main part

This part of the code performs all the calculations required for the application to function correctly. It also provides the link between the calculations made and their display, thanks to the graphics section that we'll explain next. It can also communicate with the amplifier and retrieve data from it.

### Graphic part

The graphical part of the code is made up of a single class, the window class, containing each widget and its display. Functions are provided to display the results curves using the matplotlib library. 

## In case of an equipment change

If the amplifier is changed, the identifier must be changed in the source code and a new executable created using the "pyinstaller" library.
To change the identifier, use NI MAX and in "Peripherals and interface", you'll find the new identifier. Copy it and replace it in the "main.py" code in the AMPLIFIER_ID constant.
Depending on the amplifier model you're using, you may need to modify the commands to be sent to the amplifier. Refer to the manual for your new amplifier in the "Data Transfer Commands" section and find the commands to be replaced in the "collect_data_lockin" function in the "main.py" file.

## Conclusion

This software is easy to use but is reserved for experienced users of the 3 omega method. The code is complex, but allows you to do a lot of things and help the user in his manipulation. 