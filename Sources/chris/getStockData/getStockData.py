#!/usr/bin/python
#########################################################################
# Copyright (C) 2016-2017 Team Pythia
#													   
# Basic python script to request stock names from user and then
# pull historical data from Yahoo API.  Data is parsed and saved in CSV
# or textfile for both the FPGA and the SW
#
# Last Updated: 10/12/2016      v1
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
# print (str(END_DATE) + " -- " + str(START_DATE))



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
# get the file paths for stock data csv files
################################################	
def getCsvFilePaths(stockNameList):
    stockCsvPathList = ['0'] * NUM_STOCKS

    print ("\nFile Paths:")    
    
    for x in range(NUM_STOCKS):
        stockCsvPathList[x] = os.path.join(os.getcwd(),"data","data_{}.csv".format(str(stockNameList[x])))
        print(stockCsvPathList[x]) # print the file path for debugging
    print ("end getCsvFilePaths\n")
    return stockCsvPathList
	
 
 
################################################
# get the stock data from Yahoo API and put in 
# csv files in the subdirectory   cwd\data\*.csv
################################################ 
def getHistoricalData(stockNameList):
    for x in range(NUM_STOCKS):
        stockName = yahoo_finance.Share(str(stockNameList[x]))
        
        # data_stockData = stockName.get_historical("beginning", "end")
        # data_stockData = stockName.get_historical("2012-06-01", "2016-06-01")
        
        data_stockData = stockName.get_historical(str(START_DATE), str(END_DATE))
        df_stockData = pd.DataFrame(data_stockData)
        df_stockData.to_csv((os.path.join("data","data_" + str(stockNameList[x]) + ".csv")))
        # print(stockData)
        print ("getHistoricalData " + str(str(stockNameList[x])))
    print ("done getting historical data")
    return True
 
 
 
################################################
# get the stock data from csv files and put in 
# data frames (pandas)
################################################
def getDataFrames(stockNameList, stockCsvPathList):
    stockDataFrames = ['0'] * NUM_STOCKS
    for x in range(NUM_STOCKS):
        stockDataFrames[x] = pd.read_csv(str(stockCsvPathList[x]))
        # print (stockDataFrames[x])    # full CSV data
        
        # temp df for parsing
        df = stockDataFrames[x]
        
        # parse out only the columns needed
        stockDataFrames[x] = df[['Date','Symbol','High','Low']]
        
        # print out the first ten rows to verify it's functioning correct
        # df = stockDataFrames[x]
        # print (df[:10])
    
    print("end getDataFrames\n")
    return stockDataFrames



################################################
# put stock data in a file for the FPGA format
################################################




################################################
# put stock data in a file for the SW format
################################################




################################################
#    main    ###################################
################################################
# important variables
#       stockNameList       :    a list of the ten stock names
#       stockCsvPathList    :    a list of all the csv file paths
#       stockDataFramesList :    a list of the ten df's



### get the stock names from console or text file ###
while True:
    try:
        howToGetNames = int(input("Get stock names from (1) user or (2) from text file: "))
        if howToGetNames == 1:
            stockNameList = getStockNamesUser()
            break
        elif howToGetNames == 2:
            stockNameList = getStockNamesText()
            break
        else:
            print ("Invalid Entry. Enter 1 or 2")
    except ValueError:
        print ("Invalid Entry. Enter 1 or 2")

### generate the csv files for all ten stocks
getHistoricalData(stockNameList)

### make a list of the csv file paths ###	
stockCsvPathList = getCsvFilePaths(stockNameList)

### put the csv files in a list of data frames ###
stockDataFramesList = ['0'] * NUM_STOCKS
getDataFrames(stockNameList, stockCsvPathList)






print("Reached end of script")
######################################################################### END
