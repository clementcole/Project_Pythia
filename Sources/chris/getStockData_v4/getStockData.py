#!/usr/bin/python
#########################################################################
# Copyright (C) 2016-2017 Team Pythia
#													   
# Basic python script to request stock names from user and then
# pull historical data from Yahoo API.  Data is parsed and saved in CSV
# or textfile for both the FPGA and the SW-implementation
#
#
#
# This version will catch JSONDecodeError's but it will not catch the
# error that resutls from trying to pull more data about a stock than
# exists (i.e. Twitter beign elss than five years old)  -CMR
#
#
#
#                  Last Updated: 11/23/2016      v4
#########################################################################



import yahoo_finance
import pprint
import pandas as pd
import datetime
import sys
import os



################################################
# "Globals"
################################################
NUM_STOCKS = 10
END_DATE = datetime.date.today() - datetime.timedelta(days=1)   # yesterday
START_DATE = datetime.date.today() - datetime.timedelta(days=(365*4))
HEADER = ['Date','Open','Close','Adj_Close','High','Low','Symbol']



################################################
# get stock names from user or txt; save in list 
# and return the list. this function can easily 
# be changed to accept the stock names from some
# other source (i.e. the UI)
################################################

def getStockNamesUser():
	# initialize empty list
	stockNameList = ['0'] * NUM_STOCKS

	# get all ten stock names from user
	for x in range(NUM_STOCKS):
		stockNameList[x] = input(str(x + 1) + ") Stock Name: ")

	# display the stocks
	print("Ten stocks: " + str(stockNameList))

	# return the list of stock names
	return stockNameList

def getStockNamesText():
	# initialize empty list
	stockNameList = ['0'] * NUM_STOCKS

	# open the file from current working dir
	# file = "\data\stockNames.txt"
	path = os.path.join(os.getcwd(), "data", "stockNames.txt")
	stockNamesTextFile = open(path, "r")

	# read the file into a list
	stockNameList = stockNamesTextFile.read().split(',')

	# display the stocks
	print("\nTen stocks to analyze: " + str(stockNameList) + "\n")

	# close the file
	stockNamesTextFile.close()

	# return the list of stock names
	return stockNameList
 
 

################################################
# get the stock data from Yahoo API and put in 
# csv files in the subdirectory   cwd\data\*.csv
################################################ 
def getHistoricalData(stockNameList):
    print("Gathering data...")
    for x in range(NUM_STOCKS):
        while True:
            try: 
                stockName = yahoo_finance.Share(str(stockNameList[x]))
        
                data_stockData = stockName.get_historical(str(START_DATE), str(END_DATE))
        
                df_stockData = pd.DataFrame(data_stockData)
		
                # reverse the order of the dat...oldest first
                df_stockData = df_stockData.iloc[::-1].reset_index(drop=True)
        
                df_stockData.to_csv((os.path.join("data","data_" + str(stockNameList[x]) + ".csv")), columns=HEADER)

                print ("   Refreshed data for " + str(stockNameList[x]))
                break # exit the while true loop if success
        
            except:      		#should catch JSONDecodeError and network errors
                print("      Error on Yahoo's end, trying again...")
    
    return True


################################################
# put stock data in a file for the FPGA format
################################################




################################################
# put stock data in a file for the SW format
################################################
# for now the SW will just read from the CSV files



################################################
#    main    ###################################
################################################

#### get the stock names from console or text file ###

#while True:
#    try:
#        howToGetNames = int(input("Get stock names from (1) user or (2) from text file: "))
#        if howToGetNames == 1:
#            stockNameList = getStockNamesUser()
#            break
#        elif howToGetNames == 2:
#            stockNameList = getStockNamesText()
#            break
#        else:
#            print ("Invalid Entry. Enter 1 or 2")
#    except ValueError:
#        print ("Invalid Entry. Enter 1 or 2")

### for now the list is hardcoded but this can be easily changed by uncommenting
### the above block and commenting out this line ###
stockNameList = ["AAPL","AMD","FB","GOOGL","INTC","KO","MSFT","TSLA","SBUX","XLNX"]
	


### create the directory "data" if it doesn't exist already ###
if not os.path.exists("data"):
	os.makedirs("data")	

	
### generate the csv files for all ten stocks ###
getHistoricalData(stockNameList)




print("All requested stock data has been refreshed")
######################################################################### END
