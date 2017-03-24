import pandas as pd

def test_run():
    # Defining Date Range
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)


    #Empty Data Frame
    df1 = pd.DataFrame(index = dates)

    dfSPY = pd.read_csv("SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])

    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
    #Join Two Dataframe
    df1=df1.join(dfSPY,how='inner')
    #print (df1)

    # Read more into Stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol), index_col="Date", parse_dates=True,usecols=['Date','Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1=df1.join(df_temp, how="left")
    print (df1)



if __name__ ==  "__main__":
    test_run()