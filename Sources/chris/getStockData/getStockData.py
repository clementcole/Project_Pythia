#########################################################################
# Copyright (C) 2016-2017 Team Pythia
#													   
# Basic python script to request stock names from user and then
# pull historical data from Yahoo API.  Data is parsed and saved in CSV
# or textfile for both the FPGA and the SW
#
# Last Updated: 10/7/2016
#########################################################################


import yahoo_finance
import pprint
import pandas as pd
import datetime
import sys
import os


################################################
# get stock names from user or txt; save in list 
# and return the list. this function can easily 
# be changed to accept the stock names from some
# other source (i.e. the UI)
################################################

def getStockNamesUser():
	# initialize empty list
	stockNameList = ['0'] * 10

	# get all ten stock names from user
	for x in range(10):
		stockNameList[x] = input(str(x+1) + ") Stock Name: ")

	# display the stocks
	print("Ten stocks: " + str(stockNameList))

	# return the list of stock names
	return stockNameList

	
def getStockNamesText():
	# initialize empty list
	stockNameList = ['0'] * 10

	# open the file from current working dir
	file = "\data\stockNames.txt"
	path = os.getcwd()+file
	stockNamesTextFile = open(path, "r")

	# read the file into a list
	stockNameList = stockNamesTextFile.read().split(',')

	# display the stocks
	print("Ten stocks: " + str(stockNameList))

	# close the file
	stockNamesTextFile.close()

	# return the list of stock names
	return stockNameList


################################################
# get the stock data from Yahoo API and put in 
# data frames (pandas)
################################################




################################################
# put stock data in a file for the FPGA format
################################################




################################################
# put stock data in a file for the SW format
################################################




################################################
#    main    ###################################
################################################

### get the stock names ###
howToGetNames = '0'

while howToGetNames not in ["1","2"]:
    howToGetNames = input("get stock names from (1) user or (2) from text file: ")
    if howToGetNames == '1':
        stockNameList = getStockNamesUser()
    elif howToGetNames == '2':
        stockNameList = getStockNamesText()
    else:
        print("invalid entry. enter 1 for console input or 2 for text file")



# end
#########################################################################
