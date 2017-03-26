import utilityfunctions as ut
import pandas as pd
from matplotlib import pyplot as plt


def test_run():
    start_date = '2009-01-01'
    end_date = '2012-12-31'

    dates = pd.date_range(start_date,end_date)
    symbols = ['SPY']

    df = ut.get_live_data(symbols,start_date,end_date,dates)

    #ut.plot_data(df)



    daily_returns = ut.compute_daily_returns(df)
    #print (daily_returns)

    #ut.plot_data(daily_returns,title="Daily Returns",ylabel = "Daily Returns")

    daily_returns.hist(bins=20)


    # Plotting mean and std on the historgram.
    mean = daily_returns['SPY'].mean()

    # print (mean)
    std = daily_returns['SPY'].std()
    # print (std)
    plt.axvline(mean,color='y',linestyle='dashed',linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

    plt.show()
    print(daily_returns.kurtosis())
if __name__ == '__main__':
    test_run()