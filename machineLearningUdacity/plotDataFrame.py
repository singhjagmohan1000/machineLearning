import os
import pandas as pd
from matplotlib import pyplot as plt



def symbol_to_path(symbol):

    return os.path.join("{}.csv".format(str(symbol)))


def get_data(symbols, dates):

    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:

        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=["SPY"])
    return df

def plot_data(df,title = "Stock Prices"):
    '''Plot Prices'''
    ax = df.plot(title=title,fonrsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    # Define a date range
    dates = pd.date_range('2016-01-01', '2016-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)
   # print (df.ix['2016-11-01': '2016-11-15',['GOOG','GLD']])

    plot_data(df)


if __name__ == "__main__":
    test_run()
