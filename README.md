Backtesting Engine
==================

A modular vectorized backtesting engine for evaluating quantitative trading strategies on historical market data.

This project was built to explore systematic trading, portfolio analytics, and quantitative research workflows while following clean software engineering practices.

Features
--------

### Data Management

*   Historical market data retrieval using Yahoo Finance
    
*   OHLCV price data support
    
*   Configurable ticker and date range selection
    

### Strategy Framework

*   Abstract strategy interface
    
*   Plug-and-play strategy architecture
    
*   Moving Average Crossover Strategy implementation
    

### Backtesting Engine

*   Vectorized backtesting using Pandas
    
*   Lookahead bias prevention via signal shifting
    
*   Position management
    
*   Portfolio equity tracking
    
*   Transaction cost modeling
    

### Performance Analytics

*   Total Return
    
*   Annualized Return
    
*   Annualized Volatility
    
*   Sharpe Ratio
    
*   Maximum Drawdown
    
*   Benchmark Comparison
    

### Trade Analytics

*   Trade logging
    
*   Win Rate
    
*   Average Trade Return
    
*   Average Holding Period
    
*   Best Trade
    
*   Worst Trade
    
*   Profit Factor
    

### Visualization

*   Equity Curve
    
*   Strategy vs Benchmark Comparison
    
*   Price Chart with Buy/Sell Signals
    

### Testing

*   Pytest-based test suite
    
*   Strategy tests
    
*   Backtest engine tests
    
*   Performance analytics tests
    

Project Structure
-----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   backtesting-engine/  │  ├── analytics/  │   ├── performance.py  │   └── plotting.py  │  ├── data/  │   └── data_loader.py  │  ├── engine/  │   └── backtest.py  │  ├── strategies/  │   ├── base_strategy.py  │   └── moving_average_crossover.py  │  ├── tests/  │   ├── test_strategy.py  │   ├── test_backtest.py  │   └── test_performance.py  │  ├── main.py  ├── requirements.txt  └── README.md   `

Architecture
------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Historical Data         │         ▼   Strategy Layer         │         ▼   Signal Generation         │         ▼   Backtesting Engine         │         ▼   Portfolio Accounting         │         ▼   Performance Analytics         │         ▼   Visualization   `

Implemented Strategy
--------------------

### Moving Average Crossover

Long position when:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Short Moving Average > Long Moving Average   `

Flat position when:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Short Moving Average <= Long Moving Average   `

Current default parameters:

*   Short Window: 20 Days
    
*   Long Window: 50 Days
    

Example Run
-----------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python main.py \    --ticker AAPL \    --start 2020-01-01 \    --end 2024-01-01 \    --capital 100000 \    --short_window 20 \    --long_window 50   `

Example Results
---------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   === Strategy ===  Total Return: 65.56%  Annualized Return: 14.21%  Sharpe Ratio: 0.72  Max Drawdown: 29.80%  === Buy & Hold Benchmark ===  Total Return: 183.71%  Annualized Return: 31.64%  Sharpe Ratio: 1.03  === Trade Summary ===  Total Trades: 10  Win Rate: 60.00%  Average Trade Return: 8.27%  Average Holding Period: 80.1 days  Best Trade: 61.93%  Worst Trade: -10.49%  Profit Factor: 4.93   `

Running Tests
-------------

Execute the complete test suite:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pytest   `

Current test coverage includes:

*   Strategy generation
    
*   Backtest execution
    
*   Performance metric calculations
    
*   Portfolio value tracking
    
*   Benchmark generation
    

Key Concepts Implemented
------------------------

*   Vectorized Backtesting
    
*   Lookahead Bias Prevention
    
*   Portfolio Return Compounding
    
*   Transaction Cost Modeling
    
*   Risk-Adjusted Performance Measurement
    
*   Drawdown Analysis
    
*   Benchmark Comparison
    
*   Trade-Level Analytics
    

Future Improvements
-------------------

### Phase 2: Event-Driven Backtesting Engine

Planned architecture:

*   MarketEvent
    
*   SignalEvent
    
*   OrderEvent
    
*   FillEvent
    
*   Portfolio
    
*   ExecutionHandler
    
*   Event Queue
    

### Additional Features

*   Multiple Asset Support
    
*   Position Sizing Models
    
*   Portfolio Rebalancing
    
*   Slippage Modeling
    
*   Advanced Risk Metrics
    
*   Walk-Forward Analysis
    
*   Factor-Based Strategies
    

Technologies Used
-----------------

*   Python
    
*   Pandas
    
*   NumPy
    
*   Matplotlib
    
*   yFinance
    
*   Pytest
    

Motivation
----------

The goal of this project is to build a realistic quantitative research environment that emphasizes:

*   Correct backtesting methodology
    
*   Reproducible research
    
*   Modular architecture
    
*   Performance analysis
    
*   Software engineering best practices
    

Rather than focusing on prediction, the project focuses on evaluating trading strategies rigorously and transparently.