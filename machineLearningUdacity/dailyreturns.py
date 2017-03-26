import pandas as pd
import yahoo_finance
from matplotlib import pyplot as plt


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


def plot_data(df,title = "Stock Prices"):
    '''Plot Prices'''
    ax = df.plot(title=title,fonrsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
