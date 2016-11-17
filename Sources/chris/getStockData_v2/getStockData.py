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
NUM_STOCKS = 3
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
 # This serves as a baseline to ensure complete
 # data for each stock 
 ################################################
def getBaseline():
	# make an empty df with just dates
	dates = pd.date_range(START_DATE,END_DATE)													# date range for our datafram
	df1 = pd.DataFrame(index=dates)																# empty dataframe
	#pprint.pprint(df1)																			# check the dataframe


	# get our baseline stock data
	SPY = yahoo_finance.Share('SPY')															# use SPY because it always trades
	SPY_stockData = SPY.get_historical(str(START_DATE), str(END_DATE))							# get the data from yahoo
	SPY_df = pd.DataFrame(SPY_stockData)														# put it in a df
	SPY_df.to_csv(os.path.join("data","SPY.csv"), columns=HEADER)								# then put the df in a csv
	#pprint.pprint(baseline_df)


	# join the dates df and the baseline df														# note you have to change the index to get the dataframes to match up
	df2 = pd.read_csv((os.path.join("data","SPY.csv")), index_col="Date", parse_dates=True, \
						usecols=HEADER, na_values=['nan'])
	baseline_df = df1.join(df2)
	baseline_df = baseline_df.dropna()															# drop the NaN's..only do this from the baseline.  fill the actual stocks		
	#pprint.pprint(baseline_df)
	return True
 
 

################################################
# get the stock data from Yahoo API and put in 
# csv files in the subdirectory   cwd\data\*.csv
################################################ 
def getHistoricalData(stockNameList):
    for x in range(NUM_STOCKS):
        stockName = yahoo_finance.Share(str(stockNameList[x]))
        
        data_stockData = stockName.get_historical(str(START_DATE), str(END_DATE))
        
        df_stockData = pd.DataFrame(data_stockData)
        
        df_stockData.to_csv((os.path.join("data","data_" + str(stockNameList[x]) + ".csv")), columns=HEADER)

        print ("getHistoricalData " + str(stockNameList[x]))
        
    print ("done getting historical data")
    return True



################################################
# make sure teh data is complete
################################################	
def checkStockData(stockNameList):
    for x in range(NUM_STOCKS):		
        # reloads the baseline into a DF, then the stock to check into a DF, then joins the two DFs

        df_BaseLine = pd.read_csv(os.path.join("data","SPY.csv"), index_col="Date", parse_dates=True)
		

        df_Unchecked = pd.read_csv(os.path.join("data","data_" + str(stockNameList[x]) + ".csv"), index_col="Date", parse_dates=True)
        
        df_Checked = df_BaseLine.join(df_Unchecked)
		
        #df_Checked.fillna(method="ffill", inplace="TRUE")				# fills any missing data that was found
		
        #df_Checked.fillna(method="bfill", inplace="TRUE")
		
        df_Checked.to_csv(os.path.join("data","data_" + str(stockNameList[x]) + ".csv"), columns=HEADER)
        print ('filled any missing data for ' + str(stockNameList[x]))

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


### get a baseline dataframe
getBaseline()


### compare the data to the baseline to ensure it is complete
checkStockData(stockNameList)



print("Script complete")
######################################################################### END
