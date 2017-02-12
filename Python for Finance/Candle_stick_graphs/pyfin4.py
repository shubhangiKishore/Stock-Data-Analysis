import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style 
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates 
import pandas as pd 
import pandas_datareader.data as web 

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)


# resampling data

#open high low close, 10 day mean

#df_mean = df['Adj Close'].resample('10D').mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_vol = df['Volume'].resample('10D').sum()


#print (df_ohlc.head())

df_ohlc.reset_index(inplace = True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


print(df_ohlc.head())

# comvert dates to m dates data time object to m date numbers 



ax1 = plt.subplot2grid((6,1),(0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1),(5,0), rowspan = 1, colspan = 1, sharex = ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width = 2, colorup = 'g')
ax2.fill_between(df_vol.index.map(mdates.date2num), df_vol.values,0)

plt.show()