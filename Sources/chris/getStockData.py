#!/usr/bin/python
#########################################################################
# Copyright (C) 2016-2017 Team Pythia
#													   
# Basic python script to request stock names from user and then
# pull historical data from Yahoo API.  Data is parsed and saved in CSV
#
# Stock symbol can be passed by command line arg:
#    Example: "python getStockArgs.py AAPL ^DJI"
#    take one or more arguments
#
# If no args given stocks are taken from /data/stockName.txt
#    make sure this txt file has 12 stocks in it!
#
# Added a limit to how many times it retries an error to eliminate
# the chance of getting stuck in an infinite loop
#
#                  Last Updated: 3/5/2017
#########################################################################



import yahoo_finance
import pprint
import pandas as pd
import datetime
import sys
import os
import matplotlib										# this prevents some errors when SSH'ing into the server
matplotlib.use('Agg')										# this prevents some errors when SSH'ing into the server
import matplotlib.pyplot as plt



################################################
# "Globals"
################################################
END_DATE = datetime.date.today() - datetime.timedelta(days=1)   				# yesterday
START_DATE = datetime.date.today() - datetime.timedelta(days=(365*4))				# four years worth of data
HEADER = ['Date','Open','Close','Adj_Close','High','Low','Volume','Symbol']			# saves all data to CSV
HEADER_TWO = ['Date','Symbol','High','Low']							# saves only a few cols to CSV


################################################
# Functions
################################################
def getStockNamesText():
	# initialize empty list
	stockNameList = ['0'] * NUM_STOCKS

	# open the file from current working dir
	# file = "\data\stockNames.txt"
	path = os.path.join(os.getcwd(), "data", "stockNames.txt")
	stockNamesTextFile = open(path, "r")

	# read the file into a list
	stockNameList = stockNamesTextFile.read().split(',')

	# close the file
	stockNamesTextFile.close()

	# return the list of stock names
	return stockNameList



def getHistoricalData(stockNameList):
	NUMERROR = 0
	print("\nGathering data...")
	for x in range(NUM_STOCKS):
		while True:
            		try: 
				stockName = yahoo_finance.Share(str(stockNameList[x]))
        
      				data_stockData = stockName.get_historical(str(START_DATE), str(END_DATE))
        
                		df_stockData = pd.DataFrame(data_stockData)
		
                		# reverse the order of the dat...oldest first
                		df_stockData = df_stockData.iloc[::-1].reset_index(drop=True)
        
				# save to a csv
                		df_stockData.to_csv((os.path.join("data","data_" + str(stockNameList[x]) + ".csv")), columns=HEADER)

				# create a new directory for the high/low csv files
				if not os.path.exists(os.path.join("data", "highlow")):
					os.makedirs(os.path.join("data", "highlow"))

				# save the high/low csv's to their directory
				df_stockData.to_csv((os.path.join("data", "highlow", "data_High_Low_" + str(stockNameList[x]) + ".csv")), columns=HEADER_TWO)

				# call the graph function
				graphStockData(str(stockNameList[x]))

                		print ("   Refreshed data for " + stockNameList[x])
                		break # exit the while true loop if success
        
            		except:      					#should catch JSONDecodeError, network errors, incorrect symbols
                		print("   Error with " + stockNameList[x] + ", trying again...")
				NUMERROR = NUMERROR + 1
				if NUMERROR == 5:
					print("      Too many errors; skipping this stock request")
					break
	return True



def graphStockData(stockName):
	### uses the dataframe to graph the high, low, close and save them in data dir ###
	
	# create the directory "graphs" if it doesn't exist already
	if not os.path.exists(os.path.join("data", "graphs")):
		os.makedirs(os.path.join("data", "graphs"))

	# open the csv
	df_stockData = pd.read_csv(os.path.join("data", "data_" + str(stockName) + ".csv"), index_col='Date')
	
	# create the plot
	fig = df_stockData[['Close','High','Low']].plot(title=(str(stockName) + " Close Value"))
	fig.set(xlabel='Date', ylabel='Value (Dollars)')

	# save the plot to a jpg
	plt.savefig(os.path.join("data", "graphs", "graph_" + str(stockName) + ".jpg"))
	
	# you have to close the plot to make way for the next stock
	plt.clf()

	return True



################################################
#    main    ###################################
################################################
# determine how to get the stock symbols
if (len(sys.argv) > 1):
	NUM_STOCKS = len(sys.argv) - 1
	stockNameList = sys.argv 					# list of cmd line args
	stockNameList.pop(0)						# get rid of first arg; script name
else:
	NUM_STOCKS = 12
	stockNameList = getStockNamesText()



# create the directory "data" if it doesn't exist already ###
if not os.path.exists("data"):
	os.makedirs("data")	

	
	
# generate the csv files for all ten stocks
getHistoricalData(stockNameList)					# graphing is done in this function call



print("All available stock data has been refreshed \n")
######################################################################### END
