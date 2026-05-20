import pandas as pd
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

from src.indicators import add_indicators


df = add_indicators(pd.read_csv("data/tesla_stock_sample.csv", parse_dates=["date"]))
app = Dash(__name__)
app.title = "Tesla Stock Analytics"

app.layout = html.Div(
    style={"fontFamily": "Segoe UI, sans-serif", "margin": "32px", "maxWidth": "1180px"},
    children=[
        html.H1("Tesla Stock Analytics Dashboard"),
        html.P("Dash rebuild of the original Power BI concept with MACD, RSI, moving averages, and volume."),
        dcc.DatePickerRange(
            id="dates",
            min_date_allowed=df["date"].min(),
            max_date_allowed=df["date"].max(),
            start_date=df["date"].min(),
            end_date=df["date"].max(),
        ),
        dcc.Graph(id="price-chart"),
        dcc.Graph(id="momentum-chart"),
    ],
)


@app.callback(
    Output("price-chart", "figure"),
    Output("momentum-chart", "figure"),
    Input("dates", "start_date"),
    Input("dates", "end_date"),
)
def update(start_date, end_date):
    view = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    price = go.Figure()
    price.add_trace(go.Scatter(x=view["date"], y=view["close"], name="Close"))
    price.add_trace(go.Scatter(x=view["date"], y=view["ma20"], name="MA20"))
    price.add_trace(go.Scatter(x=view["date"], y=view["ma50"], name="MA50"))
    price.update_layout(title="Price Trend", yaxis_title="USD")
    momentum = go.Figure()
    momentum.add_trace(go.Scatter(x=view["date"], y=view["rsi"], name="RSI"))
    momentum.add_trace(go.Scatter(x=view["date"], y=view["macd"], name="MACD"))
    momentum.add_trace(go.Scatter(x=view["date"], y=view["signal"], name="Signal"))
    momentum.update_layout(title="Momentum Indicators")
    return price, momentum


if __name__ == "__main__":
    app.run(debug=True)
