import pandas as pd
import yahoo_finance
from matplotlib import pyplot as plt
import utilityfunctions as ut


def test_run():

    dates = pd.date_range('2012-07-01','2012-07-31')

    symbols=['SPY', 'XOM']
    df = ut.get_live_data(symbols,dates)
    ut.plot_data(df)
    daily_returns = ut.compute_daily_returns(df)
    ut.plot_data(df)
    ut.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

if __name__ == '__main__':
    test_run()