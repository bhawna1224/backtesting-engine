from data.data_loader import MarketDataLoader
from strategies.moving_average_crossover import MovingAverageCrossoverStrategy
from engine.backtest import BacktestEngine
from analytics.performance import PerformanceAnalyzer
from analytics.plotting import BacktestPlotter
import pandas as pd
import argparse

def main():
    """
    Main function to test the vectorized backtesting engine.
    Downloads AAPL data, runs MA crossover strategy, and prints results.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run backtest with Moving Average Crossover Strategy")
    parser.add_argument('--ticker', type=str, default='AAPL', help='Stock ticker symbol')
    parser.add_argument('--start', type=str, default='2020-01-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', type=str, default='2024-01-01', help='End date (YYYY-MM-DD)')
    parser.add_argument('--capital', type=float, default=100000, help='Initial capital')
    parser.add_argument('--short_window', type=int, default=20, help='Short MA window')
    parser.add_argument('--long_window', type=int, default=50, help='Long MA window')
    args = parser.parse_args()

    # Step 1: Download historical data
    print(f"Downloading {args.ticker} historical data from {args.start} to {args.end}...")
    data_loader = MarketDataLoader(
        ticker=args.ticker,
        start_date=args.start,
        end_date=args.end
    )
    price_data = data_loader.fetch_data()
    
    # Convert MultiIndex to single-level datetime index
    if isinstance(price_data.index, pd.MultiIndex):
        price_data.index = price_data.index.get_level_values(0)
    price_data.index = pd.to_datetime(price_data.index)
    
    # Step 2: Initialize strategy
    print("\nInitializing Moving Average Crossover Strategy...")
    strategy = MovingAverageCrossoverStrategy(
        data=price_data,
        short_window=args.short_window,
        long_window=args.long_window
    )
    
    # Step 3: Generate signals
    print("\nGenerating trading signals...")
    signals = strategy.generate_signals()
    
    # Ensure signals has same index as price data
    signals.index = pd.to_datetime(signals.index)
    
    # Step 4: Run backtest
    print("\nRunning backtest...")
    backtest = BacktestEngine(
        price_data=price_data,
        signals=signals,
        initial_capital=args.capital
    )
    results = backtest.run_backtest()
    
    # Step 5: Performance analysis
    print("\n=== Performance Analysis ===")
    analyzer = PerformanceAnalyzer(
        strategy_returns=results['returns']['strategy_returns'],
        cumulative_returns=results['cumulative_returns']
    )
    benchmark_analyzer = PerformanceAnalyzer(
        results['returns']['benchmark_returns'],
        results['benchmark_cumulative_returns']
    )
    total_return = analyzer.calculate_total_return()
    annual_return = analyzer.calculate_annualized_return()
    sharpe_ratio = analyzer.calculate_sharpe_ratio()
    max_drawdown, drawdown_start, drawdown_end = analyzer.calculate_max_drawdown()
    print("\n=== Strategy ===")
    print(f"\nTotal Return: {total_return:.2%}")
    print(f"Annualized Return: {annual_return:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown:.2%} ({drawdown_start} to {drawdown_end})")
    print("\n=== Buy & Hold Benchmark ===")
    print(f"Total Return: {benchmark_analyzer.calculate_total_return():.2%}")
    print(f"Annualized Return: {benchmark_analyzer.calculate_annualized_return():.2%}")
    print(f"Sharpe Ratio: {benchmark_analyzer.calculate_sharpe_ratio():.2f}")
    print("\n=== Trade Summary ===")

    summary = results["trade_summary"]

    print(
        f"Total Trades: "
        f"{summary['total_trades']}"
    )

    print(
        f"Win Rate: "
        f"{summary['win_rate']:.2%}"
    )

    print(
        f"Average Trade Return: "
        f"{summary['average_trade_return']:.2%}"
    )

    print(
        f"Average Holding Period: "
        f"{summary['average_holding_period']:.1f} days"
    )
    print("\n=== First Trades ===")
    print(results["trade_log"].head())
    print(
        f"Best Trade: "
        f"{summary['best_trade']:.2%}"
    )

    print(
        f"Worst Trade: "
        f"{summary['worst_trade']:.2%}"
    )
    print(
        f"Profit Factor: "
        f"{summary['profit_factor']:.2f}"
    )
    # Step 6: Visualization
    print("\nGenerating visualizations...")
    plotter = BacktestPlotter(price_data, signals, results['cumulative_returns'], results['benchmark_cumulative_returns'])
    plotter.plot_equity_curve(title=f"{args.ticker} Strategy Equity Curve")
    plotter.plot_price_with_signals(title=f"{args.ticker} Price with Signals")

if __name__ == "__main__":
    main()
