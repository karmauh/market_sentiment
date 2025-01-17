import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from visualization.plots import plot_price_chart


def create_gui(data, recommendation, plot_data=None, asset_details=None):
    """
    Tworzy główne GUI do wyświetlania danych analizy, rekomendacji oraz wykresu.

    Args:
        data (dict): Dane analizy technicznej.
        recommendation (str): Rekomendacja AI.
        plot_data (dict): Dane do wykresu.
        asset_details (dict): Szczegóły aktywa.
    """
    # Tworzenie głównego okna
    root = tk.Tk()
    root.title("Rekomendacja AI")
    root.geometry("1200x900")  # Powiększone okno

    # Dodanie możliwości scrollowania
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar_main = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_main.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar_main.pack(side=tk.RIGHT, fill=tk.Y)

    # Nagłówek
    header = tk.Label(scrollable_frame, text="Dane analizy", font=("Helvetica", 16, "bold"))
    header.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Ramka dla tabeli
    table_frame = tk.Frame(scrollable_frame)
    table_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Tabela z danymi
    tree = ttk.Treeview(table_frame, columns=("Wskaźnik", "Wartość"), show="headings", height=15)
    tree.heading("Wskaźnik", text="Wskaźnik")
    tree.heading("Wartość", text="Wartość")
    tree.column("Wskaźnik", anchor=tk.W, width=500)
    tree.column("Wartość", anchor=tk.E, width=300)

    # Scrollbar dla tabeli
    scrollbar_table = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_table.set)

    scrollbar_table.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Dodanie szczegółów aktywa do tabeli
    if asset_details:
        for key, value in asset_details.items():
            tree.insert("", "end", values=(key, f"{value:.2f}"))

    # Dodanie danych analizy technicznej do tabeli
    for key, value in data.items():
        if isinstance(value, int):  # Jeśli to liczba całkowita, np. pozytywne/negatywne posty
            tree.insert("", "end", values=(key, value))
        elif isinstance(value, float):  # Jeśli to liczba zmiennoprzecinkowa (np. wskaźniki jak RSI)
            tree.insert("", "end", values=(key, f"{value:.2f}"))
        else:  # Dla innego typu danych (jako tekst)
            tree.insert("", "end", values=(key, str(value)))

    # Rekomendacja AI
    recommendation_label = tk.Label(
        scrollable_frame, text=f"Rekomendacja: {recommendation}", font=("Helvetica", 14, "bold"), fg="blue"
    )
    recommendation_label.grid(row=2, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Wykres w GUI
    if plot_data:
        fig = plot_price_chart(
            prices=plot_data["prices"],
            sma_5=plot_data["sma_5"],
            sma_30=plot_data["sma_30"],
            symbol=plot_data["symbol"],
            ema_10=plot_data["ema_10"],
            bb_middle=plot_data["bb_middle"],
            bb_upper=plot_data["bb_upper"],
            bb_lower=plot_data["bb_lower"],
        )

        figure_canvas = FigureCanvasTkAgg(fig, scrollable_frame)
        figure_canvas.draw()
        canvas_widget = figure_canvas.get_tk_widget()
        canvas_widget.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Przycisk zamknięcia aplikacji
    close_button = ttk.Button(scrollable_frame, text="Zamknij", command=root.destroy)
    close_button.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

    # Wymuszenie skalowania elementów wewnątrz okna
    for i in range(2):
        scrollable_frame.grid_columnconfigure(i, weight=1)

    # Uruchomienie GUI
    root.mainloop()
