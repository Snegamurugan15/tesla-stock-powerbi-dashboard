# Tesla Stock Power BI Dashboard

This project analyzes Tesla stock-price movement using a Power BI report and a Python/Dash implementation. The original dashboard focuses on trading volume, open/high/low/close price behavior, monthly trends, conditional formatting, and interactive stock-market visuals.

## Analytics Included

- Power BI dashboard with Tesla stock visuals and conditional formatting.
- PDF export of the Power BI dashboard for quick viewing.
- Closing-price trend.
- 20-day and 50-day moving averages.
- RSI momentum indicator.
- MACD and signal line.
- Date-range filtering for investor-style exploration.

## Files

- `src/indicators.py` - reusable technical-indicator calculations.
- `dash_app.py` - Dash dashboard.
- `data/tesla_stock_sample.csv` - safe sample time-series data.
- `powerbi/tesla-stock-dashboard.pbix` - original Power BI Desktop report.
- `reports/tesla-stock-powerbi-report.pdf` - exported report snapshot.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python dash_app.py
```

## Portfolio Note

This is not investment advice. It is a finance analytics and visualization project showing how Power BI-style indicators can be reproduced in Python.
