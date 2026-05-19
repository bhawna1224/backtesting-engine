from data.data_loader import MarketDataLoader
from strategies.moving_average_crossover import MovingAverageCrossoverStrategy
from engine.backtest import BacktestEngine
import pandas as pd

def main():
    """
    Main function to test the vectorized backtesting engine.
    Downloads AAPL data, runs MA crossover strategy, and prints results.
    """
    # Step 1: Download historical data
    print("Downloading AAPL historical data...")
    data_loader = MarketDataLoader(
        ticker="AAPL",
        start_date="2020-01-01",
        end_date="2024-01-01"
    )
    price_data = data_loader.fetch_data()
    
    # Ensure single-level datetime index
    price_data.index = pd.to_datetime(price_data.index)
    
    # Step 2: Initialize strategy
    print("\nInitializing Moving Average Crossover Strategy...")
    strategy = MovingAverageCrossoverStrategy(
        data=price_data,
        short_window=20,
        long_window=50
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
        initial_capital=100000
    )
    results = backtest.run_backtest()
    
    # Step 5: Print results
    print("\n=== Results ===")
    print("\nFirst 10 signals:")
    print(signals.head(10))
    
    print("\nFirst 10 returns:")
    print(results['returns'].head(10))
    
    print(f"\nFinal cumulative return: {results['cumulative_returns'][-1]:.2%}")
    print(f"Final portfolio value: ${results['portfolio_value'][-1]:,.2f}")

if __name__ == "__main__":
    main()
