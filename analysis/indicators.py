import pandas as pd
import numpy as np

def calculate_sma(data, window):
    if len(data) < window:
        raise ValueError("Zbyt mało danych do obliczenia SMA.")

    df = pd.DataFrame(data, columns=["value"])
    df["SMA"] = df["value"].rolling(window=window).mean()
    return df["SMA"].tolist()


def calculate_rsi(prices, window=14):
    if len(prices) < window:
        raise ValueError("Zbyt mało danych do obliczenia RSI.")

    deltas = np.diff(prices)
    gains = np.maximum(deltas, 0)
    losses = np.abs(np.minimum(deltas, 0))

    avg_gain = np.mean(gains[:window])
    avg_loss = np.mean(losses[:window])

    if avg_loss == 0:
        return 100  # RSI = 100, jeśli brak strat

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    if len(prices) < long_window:
        raise ValueError("Zbyt mało danych do obliczenia MACD.")

    short_ema = np.convolve(prices, np.ones(short_window)/short_window, mode='valid')
    long_ema = np.convolve(prices, np.ones(long_window)/long_window, mode='valid')

    macd = short_ema[-len(long_ema):] - long_ema
    signal_line = np.convolve(macd, np.ones(signal_window)/signal_window, mode='valid')

    return macd[-1], signal_line[-1]


def calculate_ema(prices, window):
    ema = []
    k = 2 / (window + 1)  # Stała wygładzania
    for i, price in enumerate(prices):
        if i == 0:
            ema.append(price)  # Pierwsza EMA równa się pierwszej cenie
        else:
            ema.append(price * k + ema[-1] * (1 - k))
    return ema


def calculate_bollinger_bands(prices, window):
    middle_band = []
    upper_band = []
    lower_band = []

    for i in range(len(prices)):
        if i < window - 1:
            middle_band.append(np.nan)
            upper_band.append(np.nan)
            lower_band.append(np.nan)
        else:
            window_prices = prices[i - window + 1:i + 1]
            mean = np.mean(window_prices)
            std_dev = np.std(window_prices)

            middle_band.append(mean)
            upper_band.append(mean + 2 * std_dev)
            lower_band.append(mean - 2 * std_dev)

    return middle_band, upper_band, lower_band


def calculate_atr(high_prices, low_prices, close_prices, window=14):
    true_ranges = []
    for i in range(1, len(close_prices)):
        high_low = high_prices[i] - low_prices[i]
        high_close = abs(high_prices[i] - close_prices[i - 1])
        low_close = abs(low_prices[i] - close_prices[i - 1])
        true_range = max(high_low, high_close, low_close)
        true_ranges.append(true_range)

    atr = np.mean(true_ranges[-window:])  # Średnia z ostatnich 'window' wartości
    return atr


def calculate_obv(close_prices, volumes):
    obv = 0
    obv_values = [obv]

    for i in range(1, len(close_prices)):
        if close_prices[i] > close_prices[i - 1]:
            obv += volumes[i]
        elif close_prices[i] < close_prices[i - 1]:
            obv -= volumes[i]
        obv_values.append(obv)

    return obv_values[-1]  # Zwraca ostatnią wartość OBV