import pandas as pd

from strategies.moving_average_crossover import (
    MovingAverageCrossoverStrategy,
)


def test_generate_signals():
    dates = pd.date_range("2024-01-01", periods=100)

    data = pd.DataFrame(
        {
            "Close": range(100)
        },
        index=dates,
    )

    strategy = MovingAverageCrossoverStrategy(
        data=data,
        short_window=5,
        long_window=20,
    )

    signals = strategy.generate_signals()

    assert "signal" in signals.columns
    assert "short_ma" in signals.columns
    assert "long_ma" in signals.columns

    assert set(signals["signal"].dropna().unique()).issubset(
        {0, 1}
    )


def test_signal_dataframe_not_empty():
    dates = pd.date_range("2024-01-01", periods=100)

    data = pd.DataFrame(
        {
            "Close": range(100)
        },
        index=dates,
    )

    strategy = MovingAverageCrossoverStrategy(
        data=data,
        short_window=5,
        long_window=20,
    )

    signals = strategy.generate_signals()

    assert not signals.empty