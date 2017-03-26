import os
import pandas as pd
from matplotlib import pyplot as plt
import yahoo_finance


def symbol_to_path(symbol):
    return os.path.join("{}.csv".format(str(symbol)))

def plot_data(df,title = "Strock Prices"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def get_live_data(symbols_list, date):
    dff = pd.DataFrame(index=date)
    for symbol in symbols_list:
        data_list = yahoo_finance.Share(symbol).get_historical("2016-02-01", "2017-09-23")
        data_df = pd.DataFrame(data_list, columns=['Date', 'Adj_Close'])
        data_df['Date'] = pd.to_datetime(data_df['Date'])
        data_df = data_df.set_index(data_df['Date'])
        data_df = pd.DataFrame(data_df, columns=['Adj_Close'])
        data_df = data_df.rename(columns={'Adj_Close': symbol})
        dff = dff.join(data_df, how='inner')
        dff = dff.astype(float)
    return dff



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




def test_run():

    dates = pd.date_range('2016-01-01','2017-02-28')

    symbols=['GOOG', 'IBM', 'GLD']
    df = get_data(symbols,dates)
    #plot_data(df)
    print (df.mean())
    print (df.median())
    print (df.std())

def test_rolling_mean():
    dates = pd.date_range('2016-01-01','2017-02-28')
    symbols = ['SPY']
    df = get_data(symbols,dates)

    ax = df['SPY'].plot(title= "SPY Rolling mean", label= 'SPY')

    rm_SPY = df['SPY'].rolling(window=20).mean()

    rm_SPY.plot(label='Rolling Mean', ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")

    plt.show()

if __name__ == "__main__":
    test_rolling_mean()