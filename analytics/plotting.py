import matplotlib.pyplot as plt
import pandas as pd
from typing import Optional

class BacktestPlotter:
    """
    Creates professional visualizations for backtest results.
    
    Parameters:
    -----------
    price_data : pd.DataFrame
        OHLCV price data with datetime index
    signals : pd.DataFrame
        DataFrame containing trading signals
    cumulative_returns : pd.Series
        Cumulative strategy returns
    """
    
    def __init__(
        self,
        price_data: pd.DataFrame,
        signals: pd.DataFrame,
        cumulative_returns: pd.Series
    ):
        self.price_data = price_data
        self.signals = signals
        self.cumulative_returns = cumulative_returns
        
    def plot_equity_curve(self, title: Optional[str] = "Equity Curve") -> None:
        """
        Plot cumulative returns over time.
        
        Parameters:
        -----------
        title : str, optional
            Plot title (default "Equity Curve")
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.cumulative_returns, label="Strategy Equity")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Cumulative Returns")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    def plot_price_with_signals(self, title: Optional[str] = "Price with Signals") -> None:
        """
        Plot price with buy/sell signals.
        
        Parameters:
        -----------
        title : str, optional
            Plot title (default "Price with Signals")
        """
        plt.figure(figsize=(12, 6))
        
        # Plot price
        plt.plot(self.price_data['Close'], label="Close Price", alpha=0.7)
        
        # Plot buy signals
        buy_signals = self.signals[self.signals['signal'].diff() == 1]
        plt.scatter(
            buy_signals.index,
            self.price_data.loc[buy_signals.index, 'Close'],
            marker='^',
            color='g',
            label="Buy Signal",
            alpha=1.0
        )
        
        # Plot sell signals
        sell_signals = self.signals[self.signals['signal'].diff() == -1]
        plt.scatter(
            sell_signals.index,
            self.price_data.loc[sell_signals.index, 'Close'],
            marker='v',
            color='r',
            label="Sell Signal",
            alpha=1.0
        )
        
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()
