# Tesla Stock Price Prediction Dashboard

The original project was a Power BI dashboard for Tesla stock analysis. This repo keeps that BI framing, but adds a Python/Dash implementation so the logic is visible in code and runnable from GitHub.

## Analytics Included

- Closing-price trend.
- 20-day and 50-day moving averages.
- RSI momentum indicator.
- MACD and signal line.
- Date-range filtering for investor-style exploration.

## Files

- `src/indicators.py` - reusable technical-indicator calculations.
- `dash_app.py` - Dash dashboard.
- `data/tesla_stock_sample.csv` - safe sample time-series data.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python dash_app.py
```

## Portfolio Note

This is not investment advice. It is a finance analytics and visualization project showing how Power BI-style indicators can be reproduced in Python.
