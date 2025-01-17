import requests
from binance.client import Client

def get_market_data(symbol, params=None):
    symbol = symbol.upper()  # Symbol wielkimi literami
    if not symbol.endswith("USDT"):  # Doklejamy "USDT", jeśli nie znajduje się na końcu
        symbol += "USDT"

    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    try:
        # Pobranie danych z API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Sprawdź, czy odpowiedź zawiera kluczowe dane
        if "lastPrice" not in data or "volume" not in data:
            raise ValueError(f"Symbol {symbol} nie istnieje w API Binance.")

        return {
            "symbol": symbol,
            "price": float(data["lastPrice"]),
            "volume": float(data["volume"]),
            "change_24h": float(data["priceChangePercent"]),
            "high_price": float(data["highPrice"]),
            "low_price": float(data["lowPrice"]),
        }

    except requests.RequestException as e:
        print(f"Błąd HTTP: {e}")
        return None
    except ValueError as e:
        print(e)  # Drukuje dokładny błąd - np. brak danych dla symbolu
        return None


def get_historical_prices(symbol, interval="1d", limit=30):
    # Klucze API Binance
    API_KEY = ''
    API_SECRET = ''

    # Tworzenie klienta
    client = Client(API_KEY, API_SECRET)

    try:
        # Pobieranie danych historycznych
        klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)

        # Pobieramy ceny maksymalne, minimalne, zamknięcia i wolumeny
        high_prices = [float(entry[2]) for entry in klines]  # Cena maksymalna
        low_prices = [float(entry[3]) for entry in klines]  # Cena minimalna
        close_prices = [float(entry[4]) for entry in klines]  # Cena zamknięcia
        volumes = [float(entry[5]) for entry in klines]  # Wolumen

        return {
            "high": high_prices,
            "low": low_prices,
            "close": close_prices,
            "volume": volumes
        }
    except Exception as e:
        print(f"Błąd podczas pobierania danych: {e}")
        return {
            "high": [],
            "low": [],
            "close": [],
            "volume": []
        }
