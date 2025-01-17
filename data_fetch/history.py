import os
from rich.console import Console
from rich.table import Table

def save_analysis_to_history(data):
    """
    Zapisuje wyniki analizy do pliku history.txt.

    Args:
        data (dict): Dane analizy do zapisania (zawiera wszystkie wskaźniki i dodatkowe informacje).
    """
    try:
        with open("history.txt", "a") as file:
            file.write(f"Data: {data['date']}\n")
            file.write(f"Symbol: {data['symbol']}\n")
            file.write(f"RSI: {data['rsi']:.2f}\n")
            file.write(f"MACD: {data['macd']:.2f}, Linia sygnału: {data['signal']:.2f}\n")
            file.write(f"EMA (10-okresowa): {data['ema_10']:.2f}\n")
            file.write(f"Bollinger Bands (20-okresowe):\n")
            file.write(f"  Środkowa linia: {data['bb_middle']:.2f}\n")
            file.write(f"  Górna linia: {data['bb_upper']:.2f}\n")
            file.write(f"  Dolna linia: {data['bb_lower']:.2f}\n")
            file.write(f"Średni sentyment: {data['average_polarity']:.2f}\n")
            file.write(f"Liczba pozytywnych postów: {data['positive_posts']}\n")
            file.write(f"Liczba negatywnych postów: {data['negative_posts']}\n")
            file.write(f"Rekomendacja AI: {data['recommendation']}\n")
            file.write("=" * 50 + "\n")
    except Exception as e:
        print(f"Błąd podczas zapisywania historii: {e}")


def display_analysis_history():
    file_path = "history.txt"
    if not os.path.exists(file_path):
        print("Historia analiz jest pusta.")
        return

    console = Console()
    table = Table(title="Historia Analiz")

    # Dodaj kolumny
    table.add_column("Data", justify="left")
    table.add_column("Symbol", justify="left")
    table.add_column("RSI", justify="right")
    table.add_column("MACD", justify="right")
    table.add_column("Linia sygnału", justify="right")
    table.add_column("Pozytywne posty", justify="right")
    table.add_column("Negatywne posty", justify="right")
    table.add_column("Średni sentyment", justify="right")

    # Wczytaj dane z pliku
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]  # Pomijamy nagłówek
        for line in lines:
            row = line.strip().split(",")
            table.add_row(*row)

    console.print(table)