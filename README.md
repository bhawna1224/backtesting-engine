# Backtesting Engine

A modular, vectorized backtesting engine for quantitative trading strategies.

## Features
- Historical market data loading via yfinance
- Strategy interface with signal generation
- Portfolio simulation and position tracking
- Performance metrics calculation
- Visualization of results

## Setup
1. Clone the repository
2. Create and activate a virtual environment
3. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage
Run a simple moving average crossover strategy:
```bash
python main.py
```

## Architecture Overview
- `data/`: Handles market data loading and preprocessing
- `strategies/`: Contains strategy implementations
- `engine/`: Core backtesting logic
- `analytics/`: Performance metrics and visualization
- `tests/`: Unit tests

## Future Improvements
- Additional data providers
- More comprehensive performance metrics
- Walk-forward analysis
- Risk management features
