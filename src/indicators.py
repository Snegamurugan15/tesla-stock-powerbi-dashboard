import pandas as pd


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ma20"] = out["close"].rolling(20, min_periods=1).mean()
    out["ma50"] = out["close"].rolling(50, min_periods=1).mean()
    delta = out["close"].diff().fillna(0)
    gain = delta.clip(lower=0).rolling(14, min_periods=1).mean()
    loss = (-delta.clip(upper=0)).rolling(14, min_periods=1).mean().replace(0, 0.01)
    out["rsi"] = 100 - (100 / (1 + gain / loss))
    out["ema12"] = out["close"].ewm(span=12, adjust=False).mean()
    out["ema26"] = out["close"].ewm(span=26, adjust=False).mean()
    out["macd"] = out["ema12"] - out["ema26"]
    out["signal"] = out["macd"].ewm(span=9, adjust=False).mean()
    return out
