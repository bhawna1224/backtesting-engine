import pandas as pd

from engine.backtest import BacktestEngine


def create_test_data():
    dates = pd.date_range("2024-01-01", periods=10)

    prices = pd.DataFrame(
        {
            "Close": [
                100,
                101,
                102,
                103,
                104,
                105,
                106,
                107,
                108,
                109,
            ]
        },
        index=dates,
    )

    signals = pd.DataFrame(
        {
            "signal": [0, 0, 1, 1, 1, 1, 1, 0, 0, 0]
        },
        index=dates,
    )

    return prices, signals


def test_backtest_runs():
    prices, signals = create_test_data()

    engine = BacktestEngine(
        price_data=prices,
        signals=signals,
        initial_capital=100000,
    )

    results = engine.run_backtest()

    assert "returns" in results
    assert "cumulative_returns" in results
    assert "portfolio_value" in results


def test_portfolio_value_positive():
    prices, signals = create_test_data()

    engine = BacktestEngine(
        price_data=prices,
        signals=signals,
        initial_capital=100000,
    )

    results = engine.run_backtest()

    assert (
        results["portfolio_value"].iloc[-1]
        > 0
    )


def test_benchmark_exists():
    prices, signals = create_test_data()

    engine = BacktestEngine(
        price_data=prices,
        signals=signals,
        initial_capital=100000,
    )

    results = engine.run_backtest()

    assert "benchmark_cumulative_returns" in results