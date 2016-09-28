#!/usr/bin/python
import yahoo_finance
from pprint import pprint
import pandas as pd

#LIST OF STOCKS
# FACEBOOK = FB
# APPLE = AAPL
# COKE = KO
# TESLA = TSLA
# GOOGLE = GOOGL
# TWITTER = TWTR
# MICROSOFT = MSFT
# XILINX = XLNX
# INTEL = INTC
# AMD = AMD
#
#

############################################################################
##FACEBOOK SYMBOL FB
############################################################################
symbol_fb1 = yahoo_finance.Share('FB')
symbol_fb2 = yahoo_finance.Share('FB')
symbol_fb3 = yahoo_finance.Share('FB')

data_fb1 = symbol_fb1.get_historical("2012-06-01", "2013-12-31")
data_fb2 = symbol_fb2.get_historical("2014-01-01", "2015-12-31")
data_fb3 = symbol_fb3.get_historical("2016-01-01", "2016-06-30")

df_fb1 = pd.DataFrame(data_fb1)
df_fb2 = pd.DataFrame(data_fb2)
df_fb3 = pd.DataFrame(data_fb3)

#output is in csv 
df_fb1.to_csv("facebook_part1")
df_fb2.to_csv("facebook_part2")
df_fb3.to_csv("facebook_part3")

############################################################################

############################################################################
##APPLE SYMBOL AAPL
############################################################################
symbol_apple1 = yahoo_finance.Share('AAPL')
symbol_apple2 = yahoo_finance.Share('AAPL')
symbol_apple3 = yahoo_finance.Share('AAPL')

data_apple1 = symbol_apple1.get_historical("2011-01-01", "2012-12-31")
data_apple2 = symbol_apple2.get_historical("2013-01-01", "2014-12-31")
data_apple3 = symbol_apple3.get_historical("2015-01-01", "2016-06-30")

df_apple1 = pd.DataFrame(data_apple1)
df_apple2 = pd.DataFrame(data_apple2)
df_apple3 = pd.DataFrame(data_apple3)

#output is in csv 
df_apple1.to_csv("apple_part1")
df_apple2.to_csv("apple_part2")
df_apple3.to_csv("apple_part3")

############################################################################

############################################################################
##COKE SYMBOL KO
############################################################################
symbol_coke1 = yahoo_finance.Share('KO')
symbol_coke2 = yahoo_finance.Share('KO')
symbol_coke3 = yahoo_finance.Share('KO')

data_coke1 = symbol_coke1.get_historical("2011-01-01", "2012-12-31")
data_coke2 = symbol_coke2.get_historical("2013-01-01", "2014-12-31")
data_coke3 = symbol_coke3.get_historical("2015-01-01", "2016-06-30")

df_coke1 = pd.DataFrame(data_coke1)
df_coke2 = pd.DataFrame(data_coke2)
df_coke3 = pd.DataFrame(data_coke3)

#output is in csv 
df_coke1.to_csv("coke_part1")
df_coke2.to_csv("coke_part2")
df_coke3.to_csv("coke_part3")

############################################################################

############################################################################
##TESLA TSLA
############################################################################
symbol_tesla1 = yahoo_finance.Share('TSLA')
symbol_tesla2 = yahoo_finance.Share('TSLA')
symbol_tesla3 = yahoo_finance.Share('TSLA')

data_tesla1 = symbol_tesla1.get_historical("2011-01-01", "2012-12-31")
data_tesla2 = symbol_tesla2.get_historical("2013-01-01", "2014-12-31")
data_tesla3 = symbol_tesla3.get_historical("2015-01-01", "2016-06-30")

df_tesla1 = pd.DataFrame(data_tesla1)
df_tesla2 = pd.DataFrame(data_tesla2)
df_tesla3 = pd.DataFrame(data_tesla3)

#output is in csv 
df_tesla1.to_csv("tesla_part1")
df_tesla2.to_csv("tesla_part2")
df_tesla3.to_csv("tesla_part3")

############################################################################

############################################################################
##GOOGLE GOOGL
############################################################################
symbol_google1 = yahoo_finance.Share('GOOGL')
symbol_google2 = yahoo_finance.Share('GOOGL')
symbol_google3 = yahoo_finance.Share('GOOGL')

data_google1 = symbol_google1.get_historical("2011-01-01", "2012-12-31")
data_google2 = symbol_google2.get_historical("2013-01-01", "2014-12-31")
data_google3 = symbol_google3.get_historical("2015-01-01", "2016-06-30")

df_google1 = pd.DataFrame(data_google1)
df_google2 = pd.DataFrame(data_google2)
df_google3 = pd.DataFrame(data_google3)

#output is in csv 
df_google1.to_csv("google_part1")
df_google2.to_csv("google_part2")
df_google3.to_csv("google_part3")

############################################################################


############################################################################
##TWITTER  TWTR
############################################################################
symbol_twitter1 = yahoo_finance.Share('TWTR')
symbol_twitter2 = yahoo_finance.Share('TWTR')
#symbol_twitter3 = yahoo_finance.Share('TWTR')

data_twitter1 = symbol_twitter1.get_historical("2013-01-01", "2014-12-31")
data_twitter2 = symbol_twitter2.get_historical("2015-01-01", "2016-06-30")
#data_twitter3 = symbol_twitter3.get_historical("2015-01-01", "2016-06-30")

df_twitter1 = pd.DataFrame(data_twitter1)
df_twitter2 = pd.DataFrame(data_twitter2)
#df_twitter3 = pd.DataFrame(data_twitter3)

#output is in csv 
df_twitter1.to_csv("twitter_part1")
df_twitter2.to_csv("twitter_part1")
#df_twitter3.to_csv("twitter_part2")

############################################################################


############################################################################
##MICROSOFT MSFT
############################################################################
symbol_microsoft1 = yahoo_finance.Share('MSFT')
symbol_microsoft2 = yahoo_finance.Share('MSFT')
symbol_microsoft3 = yahoo_finance.Share('MSFT')

data_microsoft1 = symbol_microsoft1.get_historical("2011-01-01", "2012-12-31")
data_microsoft2 = symbol_microsoft2.get_historical("2013-01-01", "2014-12-31")
data_microsoft3 = symbol_microsoft3.get_historical("2015-01-01", "2016-06-30")

df_microsoft1 = pd.DataFrame(data_microsoft1)
df_microsoft2 = pd.DataFrame(data_microsoft2)
df_microsoft3 = pd.DataFrame(data_microsoft3)

#output is in csv 
df_microsoft1.to_csv("microsoft_part1")
df_microsoft2.to_csv("microsoft_part2")
df_microsoft3.to_csv("microsoft_part3")

############################################################################


############################################################################
##XILINX XLNX
############################################################################
symbol_xilinx1 = yahoo_finance.Share('XLNX')
symbol_xilinx2 = yahoo_finance.Share('XLNX')
symbol_xilinx3 = yahoo_finance.Share('XLNX')

data_xilinx1 = symbol_xilinx1.get_historical("2011-01-01", "2012-12-31")
data_xilinx2 = symbol_xilinx2.get_historical("2013-01-01", "2014-12-31")
data_xilinx3 = symbol_xilinx3.get_historical("2015-01-01", "2016-06-30")

df_xilinx1 = pd.DataFrame(data_xilinx1)
df_xilinx2 = pd.DataFrame(data_xilinx2)
df_xilinx3 = pd.DataFrame(data_xilinx3)

#output is in csv 
df_xilinx1.to_csv("xilinx_part1")
df_xilinx2.to_csv("xilinx_part2")
df_xilinx3.to_csv("xilinx_part3")

############################################################################


############################################################################
##INTEL INTC
############################################################################
symbol_intel1 = yahoo_finance.Share('INTC')
symbol_intel2 = yahoo_finance.Share('INTC')
symbol_intel3 = yahoo_finance.Share('INTC')

data_intel1 = symbol_intel1.get_historical("2011-01-01", "2012-12-31")
data_intel2 = symbol_intel2.get_historical("2013-01-01", "2014-12-31")
data_intel3 = symbol_intel3.get_historical("2015-01-01", "2016-06-30")

df_intel1 = pd.DataFrame(data_intel1)
df_intel2 = pd.DataFrame(data_intel2)
df_intel3 = pd.DataFrame(data_intel3)

#output is in csv 
df_intel1.to_csv("intel_part1")
df_intel2.to_csv("intel_part2")
df_intel3.to_csv("intel_part3")

############################################################################

############################################################################
##AMD AMD
############################################################################
symbol_amd1 = yahoo_finance.Share('AMD')
symbol_amd2 = yahoo_finance.Share('AMD')
symbol_amd3 = yahoo_finance.Share('AMD')

data_amd1 = symbol_amd1.get_historical("2011-01-01", "2012-12-31")
data_amd2 = symbol_amd2.get_historical("2013-01-01", "2014-12-31")
data_amd3 = symbol_amd3.get_historical("2015-01-01", "2016-06-30")

df_amd1 = pd.DataFrame(data_amd1)
df_amd2 = pd.DataFrame(data_amd2)
df_amd3 = pd.DataFrame(data_amd3)

#output is in csv 
df_amd1.to_csv("amd_part1")
df_amd2.to_csv("amd_part2")
df_amd3.to_csv("amd_part3")

############################################################################




# MICROSOFT = MSFT
# XILINX = XLNX
# INTEL = INTC
# AMD = AMD
#




# MICROSOFT = MSFT
# XILINX = XLNX
# INTEL = INTC
# AMD = AMD
#
