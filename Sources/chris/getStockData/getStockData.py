#!/usr/bin/python
#########################################################################
# Copyright (C) 2016-2017 Team Pythia
#													   
# Basic python script to request stock names from user and then
# pull historical data from Yahoo API.  Data is parsed and saved in CSV
# or textfile for both the FPGA and the SW
#
# Last Updated: 10/10/2016
#########################################################################


import yahoo_finance
import pprint
import pandas as pd
import datetime
import sys
import os

NUM_STOCKS = 10

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
	file = "\data\stockNames.txt"
	path = os.getcwd()+file
	stockNamesTextFile = open(path, "r")

	# read the file into a list
	stockNameList = stockNamesTextFile.read().split(',')

	# display the stocks
	print("\nTen stocks to analyze: " + str(stockNameList))

	# close the file
	stockNamesTextFile.close()

	# return the list of stock names
	return stockNameList



################################################
# get the file paths for stock data csv files
################################################	
def getCsvFilePaths(stockNameList, base_dir="data"):
    stockCsvPathList = ['0'] * NUM_STOCKS

    print ("\nFile Paths: \n")    
    
    for x in range(NUM_STOCKS):
        stockCsvPathList[x] = os.path.join(base_dir,"{}.csv".format(str(stockNameList[x])))
        print(stockCsvPathList[x]) # print the file path for debugging
    return stockCsvPathList
	
 
################################################
# get the stock data from Yahoo API and put in 
# csv files in the subdirectory \data\
################################################ 
 
 

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
        df = stockDataFrames[x]
        print (df[:10])
    
    
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
howToGetNames = '0'
while howToGetNames not in ["1","2"]:
    howToGetNames = input("Get stock names from (1) user or (2) from text file: ")
    if howToGetNames == '1':
        stockNameList = getStockNamesUser()
    elif howToGetNames == '2':
        stockNameList = getStockNamesText()
    else:
        print("invalid entry. enter 1 for console input or 2 for text file")



### make a list of the csv file paths ###	
stockCsvPathList = getCsvFilePaths(stockNameList)



### put the csv files in a list of data frames ###
stockDataFramesList = ['0'] * NUM_STOCKS
getDataFrames(stockNameList, stockCsvPathList)


######################################################################### END
