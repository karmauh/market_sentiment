import tkinter as tk
from tkinter import ttk


def pre_gui(on_submit_callback):
    # Tworzenie głównego okna
    root = tk.Tk()
    root.title("Konfiguracja aplikacji")
    root.geometry("600x400")

    # Funkcja obsługująca kliknięcie przycisku
    def handle_submit():
        symbol = symbol_entry.get().strip().upper()
        interval = interval_var.get()
        keyword = keyword_entry.get().strip()

        if not symbol or not interval or not keyword:
            error_label.config(text="Wszystkie pola muszą być wypełnione!")
            return

        # Zamknięcie okna i wywołanie funkcji przekazanej w argumencie
        root.destroy()
        on_submit_callback(symbol, interval, keyword)

    # Etykieta nagłówka
    header = tk.Label(root, text="Konfiguracja aplikacji", font=("Helvetica", 16, "bold"))
    header.pack(pady=10)

    # Pole symbolu aktywa
    tk.Label(root, text="Symbol aktywa (np. BTCUSDT):").pack(anchor=tk.W, padx=20)
    symbol_entry = tk.Entry(root, width=30)
    symbol_entry.pack(pady=5, padx=20)

    # Pole wyboru interwału czasu
    tk.Label(root, text="Interwał czasu:").pack(anchor=tk.W, padx=20)
    interval_var = tk.StringVar(value="1d")
    intervals = [("1 minuta", "1m"), ("5 minut", "5m"), ("15 minut", "15m"),
                 ("1 godzina", "1h"), ("1 dzień", "1d"), ("1 tydzień", "1w")]
    for text, value in intervals:
        ttk.Radiobutton(root, text=text, variable=interval_var, value=value).pack(anchor=tk.W, padx=30)

    # Pole słowa kluczowego
    tk.Label(root, text="Słowo kluczowe do analizy sentymentu:").pack(anchor=tk.W, padx=20)
    keyword_entry = tk.Entry(root, width=30)
    keyword_entry.pack(pady=5, padx=20)

    # Etykieta błędów
    error_label = tk.Label(root, text="", font=("Helvetica", 10), fg="red")
    error_label.pack(pady=10)

    # Przycisk potwierdzenia
    submit_button = ttk.Button(root, text="Zatwierdź", command=handle_submit)
    submit_button.pack(pady=20)

    # Uruchomienie GUI
    root.mainloop()
