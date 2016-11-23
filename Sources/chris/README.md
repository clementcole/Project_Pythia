# Project Name: 		FPGA Based Stock Prediction





This version adds error handling so the program doesn't crash when their is a JSON error from Yahoo's end.  Also, the stock names are hardcoded in so all you 
have to do is run the script.  No user input is required.  This will allow it to be scheduled for auto-running easier.




StockData is a Linux executable





Known Bugs:   on some systems, an error is thrown when you attempt to retrieve historical data on a stock that has been around for less than five years (i.e. TWTR).