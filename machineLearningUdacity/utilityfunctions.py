import pandas as pd
import os
import yahoo_finance
from matplotlib import pyplot as plt


def symbol_to_path(symbol):
    return os.path.join("{}.csv".format(str(symbol)))

def get_data(symbols,dates):
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0,'SPY')

    for symbol in symbols:

        df_temp = pd.read_csv(symbol_to_path(symbol),index_col="Date",parse_dates=True, usecols=['Date', 'Adj Close'],na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol=='SPY':
            df=df.dropna(subset=["SPY"])
    return df

def get_live_data(symbols_list, start_date,end_date,date):
    dff = pd.DataFrame(index=date)
    for symbol in symbols_list:
        data_list = yahoo_finance.Share(symbol).get_historical(start_date,end_date)
        data_df = pd.DataFrame(data_list, columns=['Date', 'Adj_Close'])
        data_df['Date'] = pd.to_datetime(data_df['Date'])
        data_df = data_df.set_index(data_df['Date'])
        data_df = pd.DataFrame(data_df, columns=['Adj_Close'])
        data_df = data_df.rename(columns={'Adj_Close': symbol})
        dff = dff.join(data_df, how='inner')
        dff = dff.astype(float)
    return dff


def plot_data(df,title = "Stock Prices", xlabel="Date", ylabel="Price"):
    '''Plot Prices'''
    ax = df.plot(title=title,fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def compute_daily_returns(df):
    daily_returns = df.copy()
    # daily_returns[1:] = (daily_returns[1:]/daily_returns[:-1].values)-1
    # daily_returns.ix[0,:] = 0
    daily_returns = (df/df.shift(1)) -1
    return daily_returns