import pandas as pd
from .base_strategy import BaseStrategy

class MovingAverageCrossoverStrategy(BaseStrategy):
    """
    Moving Average Crossover Strategy.
    Generates signals when short MA crosses above/below long MA.
    """
    
    def __init__(self, data: pd.DataFrame, short_window: int=20, long_window: int=50):
        """
        Initialize strategy with price data and window lengths.
        
        Parameters:
        -----------
        data : pd.DataFrame
            DataFrame containing OHLCV price data
        short_window : int
            Window size for short moving average
        long_window : int
            Window size for long moving average
        """
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
        
    def generate_signals(self) -> pd.DataFrame:
        """
        Generate trading signals based on MA crossover logic.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame containing:
            - 'signal' (1=long, 0=flat)
            - 'short_ma', 'long_ma' columns
            - Indexed by datetime
        """
        signals = pd.DataFrame(index=self.data.index)
        signals['short_ma'] = self.data['Close'].rolling(window=self.short_window).mean()
        signals['long_ma'] = self.data['Close'].rolling(window=self.long_window).mean()
        
        # Generate signals (1 when short MA > long MA, else 0)
        signals['signal'] = 0
        signals.loc[signals['short_ma'] > signals['long_ma'], 'signal'] = 1
        
        return signals.dropna()
