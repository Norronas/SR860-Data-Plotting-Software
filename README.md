# 3-Omega Helping Software by Némo CAZIN

## Some details on this project

This software was developed during my 4-week internship in the 3rd year of the Embedded Systems course at Polytech Lille. This internship was carried out in the MITEC research group of the IEMN laboratory (Institute of Electronics, Microelectronics and Nanotechnology).

## Resume of this software

This software can be used to carry out theoretical characterisation of polymer materials and plot graphs of the results obtained. It can also receive data from an SR860 lock-in amplifier and add it to the graphs.
As this software is intended for a research laboratory, some of the work on the software has been removed to remain confidential.
Finally, this software mainly uses the tkinter graphics library and the cmath, sympy and numpy mathematics libraries. The pyvisa library is slightly used to communicate with the SR860 lock-in amplifier. Finaly, the matplotlib library is also used for the display of equation results.

### Easy use of the software

An executable file is available to launch the application. You will then need to choose the number of layers to match your materials and insert the parameters for each layer.
After that, simply press the "Simulate" button to obtain the graph. 

## Details about the code

### Main part

This part of the code performs all the calculations required for the application to function correctly. It also provides the link between the calculations made and their display, thanks to the graphics section that we'll explain next.

### Graphic part

The graphical part of the code is made up of a single class, the window class, containing each widget and its display. Functions are provided to display the results curves using the matplotlib library.

## Conclusion

I know I could have done better on certain points of the code, but these are just small details to be corrected. The software still works and allows you to do great things, but it's not for everyone.