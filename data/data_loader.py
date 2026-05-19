import yfinance as yf
import pandas as pd
from typing import Optional


class MarketDataLoader:
    """
    Loads historical market data using yfinance.
    
    Parameters:
    -----------
    ticker : str
        The ticker symbol to download data for.
    start_date : str
        Start date in format 'YYYY-MM-DD'.
    end_date : str
        End date in format 'YYYY-MM-DD'.
    interval : str
        Data interval ('1d', '1wk', '1mo', etc.).
    """
    
    def __init__(
        self, 
        ticker: str, 
        start_date: str, 
        end_date: str, 
        interval: str = '1d'
    ):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        
    def fetch_data(self) -> pd.DataFrame:
        """
        Download OHLCV data from yfinance.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame containing OHLCV data with DatetimeIndex
        """
        df = yf.download(
            tickers=self.ticker,
            start=self.start_date,
            end=self.end_date,
            interval=self.interval,
            progress=False
        )
        return df.sort_index()
