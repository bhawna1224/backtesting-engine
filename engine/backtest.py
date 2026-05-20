import pandas as pd

class BacktestEngine:
    """
    Vectorized backtesting engine for evaluating trading strategies.
    """
    
    def __init__(
        self,
        price_data: pd.DataFrame,
        signals: pd.DataFrame,
        initial_capital: float=100000
    ):
        """
        Initialize backtest with price data and signals.
        
        Parameters:
        -----------
        price_data : pd.DataFrame
            OHLCV price data with datetime index
        signals : pd.DataFrame
            DataFrame containing trading signals
        initial_capital : float
            Starting capital for backtest
        """
        self.price_data = price_data
        self.signals = signals
        self.initial_capital = initial_capital
        
    def run_backtest(self) -> dict:
        """
        Execute vectorized backtest.
        
        Returns:
        --------
        dict
            Dictionary containing:
            - 'returns' DataFrame with daily returns
            - 'cumulative_returns' Series
            - 'portfolio_value' Series
        """
        # Convert both DataFrames to have consistent single-level datetime index
        price_data = self.price_data.copy()
        signals = self.signals.copy()
        
        # Convert MultiIndex columns to single level if present
        if isinstance(price_data.columns, pd.MultiIndex):
            price_data.columns = price_data.columns.get_level_values(0)
        if isinstance(signals.columns, pd.MultiIndex):
            signals.columns = signals.columns.get_level_values(0)
            
        # Ensure datetime index
        price_data.index = pd.to_datetime(price_data.index)
        signals.index = pd.to_datetime(signals.index)
        
        # Join price data with signals
        joined_data = price_data.join(signals, how='inner').dropna()
        
        # Calculate asset returns
        joined_data['asset_returns'] = joined_data['Close'].pct_change()
        
        # Shift signals to avoid lookahead bias
        joined_data['positions'] = joined_data['signal'].shift(1)
        
        # Calculate strategy returns
        joined_data['strategy_returns'] = (joined_data['positions'] * 
                                         joined_data['asset_returns'])
        
        # Calculate cumulative returns
        joined_data['cumulative_returns'] = (
            1 + joined_data['strategy_returns']).cumprod() - 1
        
        # Calculate portfolio value
        joined_data['portfolio_value'] = (
            self.initial_capital * (1 + joined_data['strategy_returns']).cumprod())
        
        return {
            'returns': joined_data[['asset_returns', 'strategy_returns']],
            'cumulative_returns': joined_data['cumulative_returns'],
            'portfolio_value': joined_data['portfolio_value']
        }
