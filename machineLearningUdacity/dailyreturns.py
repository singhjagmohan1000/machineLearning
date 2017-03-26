import pandas as pd
import yahoo_finance
from matplotlib import pyplot as plt
import utilityfunctions as ut


def test_run():
    start_date = '2012-07-01'
    end_date = '2012-07-31'
    dates = pd.date_range(start_date,end_date)

    symbols=['SPY', 'XOM']
    df = ut.get_live_data(symbols,start_date,end_date,dates)
    #ut.plot_data(df)
    daily_returns = ut.compute_daily_returns(df)
    #ut.plot_data(df)
    ut.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

if __name__ == '__main__':
    test_run()