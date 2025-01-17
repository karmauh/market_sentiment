from data_fetch.market_data import get_historical_prices, get_market_data
from analysis.indicators import (
    calculate_sma, calculate_ema, calculate_rsi,
    calculate_macd, calculate_bollinger_bands,
    calculate_atr, calculate_obv
)
from data_fetch.reddit_data import get_reddit_posts
from analysis.sentiment import analyze_sentiment
from utils.pre_gui import pre_gui
from ai_recommendation import load_model_and_predict
from utils.gui import create_gui

# Główna funkcja programu
def main():

    def on_submit(symbol, interval, keyword):
        """
        Callback uruchamiany po wprowadzeniu danych w `pre_gui`.
        """
        try:
            # Pobranie danych rynkowych
            historical_prices = get_historical_prices(symbol, interval=interval, limit=30)
            market_data = get_market_data(symbol)

            if not historical_prices["close"] or not market_data:
                print("Nie udało się pobrać danych. Sprawdź symbol i spróbuj ponownie.")
                return

            # Szczegóły aktywa
            opening_price = historical_prices["close"][0]
            closing_price = historical_prices["close"][-1]
            max_price = max(historical_prices["high"])
            min_price = min(historical_prices["low"])
            volatility = max_price - min_price

            asset_details = {
                "Cena otwarcia": opening_price,
                "Cena zamknięcia": closing_price,
                "Cena maksymalna": max_price,
                "Cena minimalna": min_price,
                "Zmienność": volatility,
            }

            # Obliczanie wskaźników technicznych
            close_prices = historical_prices["close"]
            sma_5 = calculate_sma(close_prices, window=5)
            sma_30 = calculate_sma(close_prices, window=30)
            ema_10 = calculate_ema(close_prices, window=10)
            rsi = calculate_rsi(close_prices, window=14)
            macd, signal = calculate_macd(close_prices)
            bb_middle, bb_upper, bb_lower = calculate_bollinger_bands(close_prices, window=20)
            atr = calculate_atr(historical_prices["high"], historical_prices["low"], close_prices, window=14)
            obv = calculate_obv(close_prices, historical_prices["volume"])

            # Pobieranie postów z Reddita i analiza sentymentu
            subreddit = "cryptocurrency"
            posts = get_reddit_posts(subreddit, keyword, limit=10)
            average_polarity, positive_count, negative_count = analyze_sentiment(posts)

            # Dane analizy
            data = {
                "RSI (14-okresowy)": rsi,
                "MACD": macd,
                "Linia sygnału": signal,
                "ATR (14-okresowy)": atr,
                "OBV": obv,
                "EMA (10-okresowa)": ema_10[-1],
                "Bollinger Bands (środkowa)": bb_middle[-1],
                "Bollinger Bands (górna)": bb_upper[-1],
                "Bollinger Bands (dolna)": bb_lower[-1],
                "Średni sentyment": average_polarity,
                "Pozytywne posty": positive_count,
                "Negatywne posty": negative_count,
            }

            plot_data = {
                "prices": close_prices,
                "sma_5": sma_5,
                "sma_30": sma_30,
                "symbol": symbol,
                "ema_10": ema_10,
                "bb_middle": bb_middle,
                "bb_upper": bb_upper,
                "bb_lower": bb_lower,
            }

            # Generowanie rekomendacji
            features = [
                rsi,  # RSI (14-okresowy)
                macd,  # MACD
                signal,  # Linia sygnału
                ema_10[-1],  # EMA (10-okresowa)
                bb_middle[-1],  # Bollinger Bands (środkowa)
                bb_upper[-1],  # Bollinger Bands (górna)
                bb_lower[-1],  # Bollinger Bands (dolna)
                atr,  # ATR (14-okresowy)
                obv,  # OBV
                average_polarity,  # Średni sentyment
                positive_count  # Liczba pozytywnych postów
            ]

            recommendation = load_model_and_predict(features)

            # Wywołanie głównego GUI
            create_gui(data, recommendation, plot_data, asset_details)

        except ValueError as ve:
            print(f"Błąd: {ve}")
        except Exception as e:
            print("Wystąpił błąd podczas przetwarzania danych.")
            import traceback
            traceback.print_exc()

    # Uruchomienie początkowego GUI
    pre_gui(on_submit)


if __name__ == "__main__":
    main()
