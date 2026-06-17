import pandas as pd

from analytics.performance import PerformanceAnalyzer


def create_performance_analyzer():
    returns = pd.Series(
        [
            0.01,
            -0.02,
            0.03,
            0.01,
            -0.01,
        ]
    )

    cumulative = (1 + returns).cumprod()

    return PerformanceAnalyzer(
        strategy_returns=returns,
        cumulative_returns=cumulative,
    )


def test_total_return():
    analyzer = create_performance_analyzer()

    total_return = analyzer.calculate_total_return()

    assert total_return > 0


def test_sharpe_ratio_returns_float():
    analyzer = create_performance_analyzer()

    sharpe = analyzer.calculate_sharpe_ratio()

    assert isinstance(sharpe, float)


def test_volatility_positive():
    analyzer = create_performance_analyzer()

    volatility = (
        analyzer.calculate_annualized_volatility()
    )

    assert volatility > 0


def test_max_drawdown():
    analyzer = create_performance_analyzer()

    drawdown, start, end = (
        analyzer.calculate_max_drawdown()
    )

    assert drawdown >= 0
    assert start is not None
    assert end is not None