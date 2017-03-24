import pandas as pd

def test_run():
    # Defining Date Range
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)


    #Empty Data Frame
    df1 = pd.DataFrame(index = dates)

    dfSPY = pd.read_csv("SPY.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])

    #Join Two Dataframe
    df1=df1.join(dfSPY,how='inner')
    print (df1)




if __name__ ==  "__main__":
    test_run()