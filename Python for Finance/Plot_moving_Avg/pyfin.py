import datetime as dt 
import matplotlib as plt 
from matplotlib import style 
import pandas as pd 
import pandas_datareader.data as web 

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

#teslas data from yahoo finance data

df = web.DataReader('TSLA','yahoo', start, end)

print (df.head(6))

df.to_csv('tsla.csv')

# df.tail to get last values
