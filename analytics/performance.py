import numpy as np
import pandas as pd
from typing import Tuple

class PerformanceAnalyzer:
    """
    Calculates key performance metrics for trading strategies.
    
    Parameters:
    -----------
    strategy_returns : pd.Series
        Daily strategy returns
    cumulative_returns : pd.Series
        Cumulative strategy returns
    risk_free_rate : float, optional
        Risk-free rate for Sharpe ratio calculation (default 0.0)
    trading_days : int, optional
        Number of trading days per year (default 252)
    """
    
    def __init__(
        self,
        strategy_returns: pd.Series,
        cumulative_returns: pd.Series,
        risk_free_rate: float = 0.0,
        trading_days: int = 252
    ):
        self.strategy_returns = strategy_returns.dropna()
        self.cumulative_returns = cumulative_returns.dropna()
        self.risk_free_rate = risk_free_rate
        self.trading_days = trading_days
        
    def calculate_total_return(self) -> float:
        """
        Calculate total return over the entire period.
        
        Returns:
        --------
        float
            Total return as a decimal (e.g., 0.10 for 10%)
        """
        return self.cumulative_returns.iloc[-1]-1
    
    def calculate_annualized_return(self) -> float:
        """
        Calculate annualized return.
        
        Returns:
        --------
        float
            Annualized return as a decimal
        """
        days = len(self.strategy_returns)
        return (1 + self.calculate_total_return()) ** (self.trading_days / days) - 1
    
    def calculate_annualized_volatility(self) -> float:
        """
        Calculate annualized volatility.
        
        Returns:
        --------
        float
            Annualized volatility as a decimal
        """
        return self.strategy_returns.std() * np.sqrt(self.trading_days)
    
    def calculate_sharpe_ratio(self) -> float:
        """
        Calculate Sharpe ratio.
        
        Returns:
        --------
        float
            Sharpe ratio
        """
        excess_returns = self.strategy_returns - self.risk_free_rate / self.trading_days
        return (
            excess_returns.mean() / excess_returns.std() * np.sqrt(self.trading_days)
        )
    
    def calculate_max_drawdown(self) -> Tuple[float, pd.Timestamp, pd.Timestamp]:
        """
        Calculate maximum drawdown.
        
        Returns:
        --------
        Tuple[float, pd.Timestamp, pd.Timestamp]
            Maximum drawdown as decimal, start date, end date
        """
        cumulative_max = self.cumulative_returns.cummax()
        drawdown = (cumulative_max - self.cumulative_returns) / cumulative_max
        max_drawdown = drawdown.max()
        end_date = drawdown.idxmax()
        start_date = self.cumulative_returns[:end_date].idxmax()
        return max_drawdown, start_date, end_date
