# backtesting_core

This project serves several purposes:

1. create an automated pipeline for trading strategies development and optimisation with webapp-like interface (thank you streamlit)
2. easily deploy the strategy to automatic trading (either local or webserver), seamless visualisation of the strategy with high level of analytics
3. create a flexible framework to add machine learning tools (scikit learn and/or tensorflow) and historical data for not only price data but economic indicators and

Work with a notion that each strategy is a portfolio, however since converntional strategy looks at returns, it is a combination of trading strategies should give you a portfolio of results. 

Ideall the strategy should incorporate some sort of proxy for tick data. I understand that developing strategies with tick data is computationally expensive, however there should be a tool to implement tick data simulation...

Ideally this project should be the same framework for strategy and portfolio management

All instruments are equal, whether it is a CFD or binary broker

so first brokers to add are:

binary.com
ig.com
binance.com

