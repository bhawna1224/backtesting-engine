import pandas as pd

class BacktestEngine:
    """
    Vectorized backtesting engine for evaluating trading strategies.
    """
    
    def __init__(
        self,
        price_data: pd.DataFrame,
        signals: pd.DataFrame,
        initial_capital: float=100000,
        commission_rate: float = 0.001
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
        self.commission_rate = commission_rate
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
        joined_data['benchmark_returns'] = joined_data['asset_returns']
        # Shift signals to avoid lookahead bias
        joined_data['positions'] = joined_data['signal'].shift(1)
        joined_data['trade_size'] = (joined_data['positions'].diff().abs().fillna(0))
        joined_data['transaction_cost'] = (joined_data['trade_size']* self.commission_rate)
        # Calculate strategy returns
        joined_data['strategy_returns'] = (
            joined_data['positions']
            * joined_data['asset_returns']
            - joined_data['transaction_cost']
        )
        # Calculate cumulative returns using compounded growth
        joined_data['cumulative_returns'] = (
            1 + joined_data['strategy_returns']
        ).cumprod()
        joined_data['benchmark_cumulative_returns'] = (
            1 + joined_data['benchmark_returns'].fillna(0)
        ).cumprod()
        # Calculate portfolio value starting from 1.0
        joined_data['portfolio_value'] = (
            self.initial_capital * (1 + joined_data['cumulative_returns'])
        )
        trade_log = self._generate_trade_log(
            joined_data
        )
        gross_profit = (
            trade_log.loc[
                trade_log["trade_return"] > 0,
                "trade_return"
            ].sum()
            if len(trade_log) > 0
            else 0
        )

        gross_loss = abs(
            trade_log.loc[
                trade_log["trade_return"] < 0,
                "trade_return"
            ].sum()
        ) if len(trade_log) > 0 else 0

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else float("inf")
        )
        trade_summary = {
            "total_trades": len(trade_log),
            "win_rate": (
                (trade_log["trade_return"] > 0).mean()
                if len(trade_log) > 0
                else 0
            ),
            "average_trade_return": (
                trade_log["trade_return"].mean()
                if len(trade_log) > 0
                else 0
            ),
            "average_holding_period": (
                trade_log["holding_period_days"].mean()
                if len(trade_log) > 0
                else 0
            ),
            "best_trade": trade_log["trade_return"].max()
            if len(trade_log) > 0 else 0,

            "worst_trade": trade_log["trade_return"].min()
            if len(trade_log) > 0 else 0,
            "profit_factor": profit_factor,
        }
        return {
            'returns': joined_data[
                [
                    'asset_returns',
                    'strategy_returns',
                    'benchmark_returns'
                ]
            ],
            'cumulative_returns': joined_data['cumulative_returns'],
            'benchmark_cumulative_returns': joined_data['benchmark_cumulative_returns'],
            'portfolio_value': joined_data['portfolio_value'],
            'trade_log': trade_log,
            'trade_summary': trade_summary,
        }
    def _generate_trade_log(self, joined_data: pd.DataFrame):
        trades = []

        in_trade = False
        entry_date = None
        entry_price = None

        for date, row in joined_data.iterrows():

            position = row["positions"]

            if not in_trade and position == 1:
                in_trade = True
                entry_date = date
                entry_price = row["Close"]

            elif in_trade and position == 0:

                exit_date = date
                exit_price = row["Close"]

                holding_period = (
                    exit_date - entry_date
                ).days

                trade_return = (
                    exit_price - entry_price
                ) / entry_price

                trades.append(
                    {
                        "entry_date": entry_date,
                        "exit_date": exit_date,
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "holding_period_days": holding_period,
                        "trade_return": trade_return,
                    }
                )

                in_trade = False

        return pd.DataFrame(trades)