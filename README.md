# SIEM Log Analyzer

Prosty system klasy SIEM (Security Information and Event Management) napisany w języku Python. Narzędzie służy do automatycznej analizy logów serwerowych pod kątem bezpieczeństwa, wykrywania ataków typu Brute-Force oraz automatycznego generowania reguł dla systemów Firewall.

## 🚀 Funkcje systemu
* **Parsowanie logów:** Automatyczne odczytywanie i czyszczenie surowych logów z pliku tekstowego.
* **Detekcja Brute-Force:** Liczenie nieudanych prób logowania per adres IP przy użyciu słowników Pythona.
* **Automatyczna Czarna Lista:** Flagowanie adresów IP przekraczających ustalony limit bezpieczeństwa (powyżej 2 nieudanych prób).
* **Rekomendacje Firewall:** Wypluwanie gotowych komunikatów o konieczności zablokowania wrogiego ruchu.

## 🛠️ Technologie
* **Język:** Python 3.x
* **Mechanizmy:** File I/O (Obsługa plików), Słowniki (Dictionaries), Pętle (Loops), Instrukcje warunkowe.

## 📈 Przykładowy Wynik Działania (Output)
== ZASTRZEŻONY SYSTEM ANALIZY LOGÓW (SIEM) ===

[i] Statystyki błędnych logowań per IP:
--> IP: 203.0.113.5 | Próby: 4

[🚨] GENEROWANIE REGUŁ FIREWALL (DO ZABLOKOWANIA):
[-] REKOMENDACJA: Zablokuj ruch z IP: 203.0.113.5 -> Powód: Atak Brute-Force
