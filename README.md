# Market Sentiment Analysis Tool

## Opis projektu
Aplikacja **Market Sentiment Analysis Tool** to zaawansowane narzędzie do analizy rynkowej kryptowalut, które integruje dane techniczne, historyczne oraz sentymenty z mediów społecznościowych (np. Reddit). Aplikacja pozwala użytkownikowi podejmować świadome decyzje inwestycyjne, generując rekomendacje za pomocą sztucznej inteligencji.

## Funkcjonalności

- **Pobieranie danych rynkowych**:
  - Wykorzystuje Binance API do pobierania cen otwarcia, zamknięcia, maksymalnych, minimalnych oraz wolumenów wybranego aktywa.
  - Obsługuje różne interwały czasowe (np. 1 minuta, 1 dzień, 1 tydzień).

- **Analiza techniczna**:
  - Implementacja wskaźników takich jak:
    - RSI (Relative Strength Index)
    - MACD (Moving Average Convergence Divergence)
    - ATR (Average True Range)
    - OBV (On-Balance Volume)
    - EMA (Exponential Moving Average)
    - Bollinger Bands
    - SMA (Simple Moving Average)

- **Analiza sentymentu**:
  - Pobieranie postów z subreddita `cryptocurrency`.
  - Analiza tekstu postów w celu określenia sentymentu (pozytywny, negatywny, neutralny).

- **Rekomendacje AI**:
  - Model AI wytrenowany przy użyciu Scikit-learn analizuje dane techniczne oraz sentymenty, aby wygenerować rekomendację:
    - **Kup**, **Sprzedaj** lub **Trzymaj**.

- **Interaktywne GUI**:
  - `Pre-GUI`: Formularz wejściowy, w którym użytkownik wprowadza dane aktywa, interwał czasu i słowo kluczowe.
  - `Główne GUI`: Wyświetla szczegółowe dane, interaktywny wykres i rekomendację AI.

- **Historia analiz**:
  - Wyniki każdej analizy są zapisywane w pliku `history.txt`.

## Technologie
- **Python**
- **Tkinter**: Budowa GUI
- **Matplotlib**: Wizualizacja danych
- **Scikit-learn**: Sztuczna inteligencja
- **Binance API**: Pobieranie danych rynkowych
- **NLTK**: Analiza sentymentu
- **Rich**: Formatowanie terminala

## Wymagania
1. Python 3.8+
2. Zainstalowane pakiety Python:
   Pakiety zawarte w projekcie:
   - matplotlib
   - scikit-learn
   - requests
   - binance
   - nltk
   - rich
   - tk
3. Konto na Binance z aktywnym kluczem API (opcjonalnie).

## Instrukcja instalacji

1. **Sklonuj repozytorium**:
   ```bash
   git clone https://github.com/your-username/market_sentiment.git
   ```

2. **Przejdź do katalogu projektu**:
   ```bash
   cd market_sentiment
   ```

3. **Zainstaluj wymagane biblioteki**:

4. **Skonfiguruj klucze API Binance**:
   - Otwórz plik `market_data.py` i wprowadź swoje klucze API:
     ```python
     API_KEY = 'your_api_key_here'
     API_SECRET = 'your_api_secret_here'
     ```

5. **Uruchom aplikację**:
   ```bash
   python main.py
   ```

## Jak korzystać z aplikacji

1. **Uruchomienie aplikacji**:
   Po uruchomieniu `main.py`, pojawi się okno GUI początkowego.

2. **Wprowadzenie danych wejściowych**:
   - Podaj symbol aktywa (np. `BTCUSDT`).
   - Wybierz interwał czasu (np. 1 dzień, 1 tydzień).
   - Wprowadź słowo kluczowe do analizy sentymentu (np. `Bitcoin`).

3. **Wyświetlenie wyników**:
   - Główne okno GUI wyświetli:
     - Szczegóły aktywa (cena otwarcia, zamknięcia, maksymalna, minimalna, zmienność).
     - Wyniki wskaźników technicznych.
     - Analizę sentymentu.
     - Wykres cenowy z wskaźnikami technicznymi.
     - Rekomendację AI.

4. **Historia analiz**:
   - Wyniki analiz są automatycznie zapisywane w pliku `history.txt`.

## Struktura projektu
```
market-sentiment-analysis/
├── analysis/
│   ├── indicators.py          # Obliczanie wskaźników technicznych
│   ├── sentiment.py           # Analiza sentymentu
├── data_fetch/
│   ├── market_data.py         # Pobieranie danych rynkowych
│   ├── reddit_data.py         # Pobieranie postów z Reddita
│   ├── history.py             # Zarządzanie historią analiz
├── visualization/
│   ├── plots.py               # Generowanie wykresów
├── ai_recommendation.py        # Model AI
├── main.py                     # Główny plik aplikacji
├── pre_gui.py                  # Formularz wejściowy GUI
├── utils/
│   ├── gui.py                 # Główne GUI
├── requirements.txt            # Lista wymaganych bibliotek
└── README.md                   # Opis projektu
```

## Przyszłe rozszerzenia
- Dodanie nowych wskaźników technicznych (np. Ichimoku Cloud).
- Obsługa większej liczby źródeł do analizy sentymentu (np. Twitter, Facebook).
- Implementacja systemu powiadomień dla użytkownika (np. email, SMS).

## Licencja
Projekt jest udostępniony na licencji MIT. Więcej informacji znajdziesz w pliku [LICENSE](LICENSE).

## Autor
**Twoje Imię i Nazwisko**
- GitHub: [Twój Profil](https://github.com/your-username)
- Email: your-email@example.com

---
