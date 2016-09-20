# Project Name: 		FPGA Based Stock Prediction

Team Name: 	        Pythia

Project Manager:	  Clement Cole

Team Members: 	  Christopher Roche,      Elijah Adedapo,      Enrique Torres





Summary


The purpose of this project is to develop an algorithm to predict daily high and low values for various stocks and then to implement it on a field programmable gate array (FPGA) and a standard computer system CPU.  Performance of the two systems will then be compared and contrasted.  Utilization of an algorithm that can take advantage of parallel programming will run faster on the FPGA than on the sequential CPU.

Stock identifies for ten stocks will be selected using a graphical user interface (GUI).  Historical data for those stocks will be pulled from Yahoo! Finance or a similar source and passed to the FPGA via the computer system.  This data will be used to make predictions for the high and low values of the stocks for the day.  

Real Time stock data will be pulled from Yahoo! Finance and passed to the FPGA.  The real time data will be used to adjust daily predictions while the market is open as well as make predictions for the following day.
