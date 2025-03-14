import yfinance as yf
import json
from datetime import datetime

# Yahoo Finance Ticker für den Syntelligence Growth Fund
TICKER = "0P0001QOND.F"

# Daten abrufen (letzte 6 Monate)
fund = yf.Ticker(TICKER)
hist = fund.history(period="6mo")

# JSON-Format für TradingView
data = [{"time": date.strftime("%Y-%m-%d"), "value": row["Close"]} for date, row in hist.iterrows()]

# Speichert die Datei als JSON
with open("fund_data.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ Erfolgreich aktualisiert: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
