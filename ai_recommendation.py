from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle  # Do zapisu modelu

def train_model():
    """
    Trenuje model Random Forest na przygotowanych danych.
    """
    # Dane (X) i etykiety (y) zdefiniowane wcześniej
    X = np.array([
        [30, 0.5, 0.4, 100, 95, 105, 0.6, 5, 2, 14.5, 50000],
        [70, -0.3, -0.4, 102, 100, 110, -0.4, 3, 7, 12.5, 45000],
        [50, 0.1, 0.1, 101, 98, 106, 0.0, 4, 4, 12.3, 52000],
        [25, 0.8, 0.7, 90, 85, 95, 0.8, 8, 1, 10.5, 38000],
        [60, 0.0, -0.1, 105, 100, 110, 0.3, 6, 3, 11.5, 48000],
        [40, -0.5, -0.6, 95, 90, 100, -0.7, 2, 6, 13.5, 42000]
    ])
    y = np.array([2, 0, 1, 2, 1, 0])

    # Skalowanie danych
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Podział na zbiór treningowy i testowy
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Trening modelu Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Ocena modelu
    accuracy = model.score(X_test, y_test)
    print(f"Dokładność modelu: {accuracy:.2f}")

    # Zapis modelu i skalera do plików
    with open("model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)
    with open("scaler.pkl", "wb") as scaler_file:
        pickle.dump(scaler, scaler_file)

# Wywołanie funkcji treningowej (tylko raz, później korzystamy z zapisanego modelu)
if __name__ == "__main__":
    train_model()


def load_model_and_predict(features):

    # Mapowanie etykiet na klasy
    labels = {0: "Sprzedaj", 1: "Trzymaj", 2: "Kup"}

    # Ładowanie modelu i skalera
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

    # Skalowanie danych wejściowych
    features_scaled = scaler.transform([features])

    # Generowanie predykcji
    prediction = model.predict(features_scaled)[0]
    return labels[prediction]
