import matplotlib.pyplot as plt

def plot_price_chart(prices, sma_5, sma_30, symbol, ema_10=None, bb_middle=None, bb_upper=None, bb_lower=None):
    """
    Generuje wykres cen aktywa z dodatkowymi wskaźnikami i zwraca obiekt Figure dla Matplotlib.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(prices, label="Cena", color="blue")
    ax.plot(sma_5, label="SMA 5-okresowa", color="orange", linestyle="--")
    ax.plot(sma_30, label="SMA 30-okresowa", color="green", linestyle="--")

    if ema_10:
        ax.plot(ema_10, label="EMA 10-okresowa", color="red", linestyle=":")
    if bb_middle and bb_upper and bb_lower:
        ax.plot(bb_middle, label="BB Środkowa", color="purple")
        ax.plot(bb_upper, label="BB Górna", color="purple", linestyle="--")
        ax.plot(bb_lower, label="BB Dolna", color="purple", linestyle="--")

    ax.set_title(f"Wykres cen dla {symbol}")
    ax.set_xlabel("Czas")
    ax.set_ylabel("Cena (USDT)")
    ax.legend()
    return fig
