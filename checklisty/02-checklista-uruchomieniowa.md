# Checklista uruchomieniowa

## Inteligentny kurnik — ESP32 / MicroPython

**Wydruk:** A4 · **Wersja dokumentu:** 1.0

### Dane uruchomienia

| Pole | Wartość |
|---|---|
| Lokalizacja / nazwa kurnika | |
| Data i godzina | |
| Osoba uruchamiająca | |
| Wersja firmware | |
| Wersja konfiguracji / kopia zapasowa | |
| Model ESP32 / rewizja płytki | |
| Model wentylatora / napędu drzwi | |
| Model czujnika NH₃ | |

### 1. Warunki rozpoczęcia

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | Checklista montażowa została zakończona, a niezgodności bezpieczeństwa zamknięte. |
| ☐ OK ☐ NOK ☐ N/D | Schemat i rzeczywista instalacja zostały porównane; piny i napięcia są potwierdzone dla tej płytki. |
| ☐ OK ☐ NOK ☐ N/D | Osłony są zamknięte; w pobliżu nie ma osób, ptaków ani przedmiotów narażonych na ruch napędu. |
| ☐ OK ☐ NOK ☐ N/D | Dostępny jest łatwy sposób odłączenia zasilania oraz osoba nadzorująca test. |
| ☐ OK ☐ NOK ☐ N/D | Progi bezpieczeństwa, godziny i wartości kalibracyjne są zapisane jako prowizoryczne lub zweryfikowane; nie traktuje się domyślnych jako zatwierdzonych. |

### 2. Pierwsze zasilenie — bez obciążeń wykonawczych

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | Zasilanie sterownika włączono zgodnie z procedurą; brak zapachu, nadmiernego nagrzewania, dymu i nietypowych dźwięków. |
| ☐ OK ☐ NOK ☐ N/D | ESP32 uruchamia się bez pętli restartów; zapisano komunikaty startowe. |
| ☐ OK ☐ NOK ☐ N/D | Napięcia zasilające sprawdzono w punktach przewidzianych projektem. |
| ☐ OK ☐ NOK ☐ N/D | Wyjścia wykonawcze pozostają w bezpiecznym stanie przy starcie i resecie. |
| ☐ OK ☐ NOK ☐ N/D | Wykonano kopię konfiguracji użytej przy uruchomieniu. |

### 3. Czujniki i odczyty

| Status | Kontrola | Odczyt / uwagi |
|---|---|---|
| ☐ OK ☐ NOK ☐ N/D | SHT31 wykryty; odczyt temperatury i wilgotności jest wiarygodny. | |
| ☐ OK ☐ NOK ☐ N/D | SCD41 wykryty; odczyt CO₂ jest dostępny po wymaganym czasie startu. | |
| ☐ OK ☐ NOK ☐ N/D | Czujnik NH₃ i jego tor analogowy odpowiadają dokumentacji konkretnego modelu. | |
| ☐ OK ☐ NOK ☐ N/D | Odczyt poziomu paszy jest stabilny i odpowiada znanemu stanowi zasobnika. | |
| ☐ OK ☐ NOK ☐ N/D | Wejście przepływu wody reaguje na impulsy; brak przepływu nie jest mylony z błędem czujnika. | |
| ☐ OK ☐ NOK ☐ N/D | Wartości porównano z przyrządem referencyjnym lub znanym stanem; zapisano różnice. | |
| ☐ OK ☐ NOK ☐ N/D | Błąd/odłączenie czujnika jest rozpoznawane i nie jest raportowane jako prawidłowy pomiar. | |

### 4. Testy wyjść i mechaniki

> Testy wykonuj pojedynczo, pod nadzorem i w warunkach zabezpieczających ludzi oraz ptaki. Nie obchodź zabezpieczeń napędu.

| Status | Kontrola | Wynik / uwagi |
|---|---|---|
| ☐ OK ☐ NOK ☐ N/D | Alarm lokalny działa i można go rozpoznać w miejscu obsługi. | |
| ☐ OK ☐ NOK ☐ N/D | Oświetlenie załącza się i wyłącza zgodnie z testowym poleceniem. | |
| ☐ OK ☐ NOK ☐ N/D | Wentylator uruchamia się i zatrzymuje zgodnie z projektem; kierunek przepływu jest prawidłowy. | |
| ☐ OK ☐ NOK ☐ N/D | Prąd rozruchowy i praca wentylatora nie powodują resetu sterownika ani zakłóceń czujników. | |
| ☐ OK ☐ NOK ☐ N/D | Drzwi wykonują kontrolowany ruch w jednym kierunku; zatrzymanie i krańcówka działają. | |
| ☐ OK ☐ NOK ☐ N/D | Drugi kierunek drzwi działa poprawnie; jednoczesne wysterowanie kierunków jest wykluczone. | |
| ☐ OK ☐ NOK ☐ N/D | Test zatrzymania/reakcji na przeszkodę wykonano zgodnie z bezpieczną procedurą producenta. | |
| ☐ OK ☐ NOK ☐ N/D | Po zaniku zasilania napęd nie wykonuje nieoczekiwanego ruchu; możliwa jest bezpieczna obsługa ręczna. | |

### 5. Sterowanie lokalne i łączność

| Status | Kontrola | Wynik / uwagi |
|---|---|---|
| ☐ OK ☐ NOK ☐ N/D | Lokalna wentylacja reaguje na testowy stan podwyższonego parametru zgodnie z konfiguracją. | |
| ☐ OK ☐ NOK ☐ N/D | Lokalna logika i alarm działają bez Home Assistant i bez MQTT. | |
| ☐ OK ☐ NOK ☐ N/D | Utrata Wi‑Fi/MQTT nie wyłącza lokalnej funkcji wentylacji ani innych krytycznych funkcji. | |
| ☐ OK ☐ NOK ☐ N/D | Po odzyskaniu łączności urządzenie wraca do raportowania bez niepożądanych poleceń wykonawczych. | |
| ☐ OK ☐ NOK ☐ N/D | Harmonogram drzwi i oświetlenia sprawdzono z uwzględnieniem czasu lokalnego. | |
| ☐ OK ☐ NOK ☐ N/D | Polecenia z HA/MQTT nie omijają lokalnych blokad i zabezpieczeń. | |

### 6. Kalibracja i okres obserwacji

| Status | Kontrola | Wartość / uwagi |
|---|---|---|
| ☐ OK ☐ NOK ☐ N/D | Zapisano wskazania referencyjne i warunki pomiaru (data, miejsce, przyrząd). | |
| ☐ OK ☐ NOK ☐ N/D | Offsety temperatury, wilgotności i CO₂ wprowadzono tylko na podstawie porównania z referencją. | |
| ☐ OK ☐ NOK ☐ N/D | Tor NH₃ skalibrowano zgodnie z modelem i dokumentacją producenta; nie użyto arbitralnego przelicznika jako wartości końcowej. | |
| ☐ OK ☐ NOK ☐ N/D | Progi wentylacji i alarmów zostały zweryfikowane dla konkretnego kurnika i obsady. | |
| ☐ OK ☐ NOK ☐ N/D | System obserwowano w pracy dziennej i nocnej; zapisano alarmy i anomalie. | |
| ☐ OK ☐ NOK ☐ N/D | Po okresie obserwacji ponownie sprawdzono stabilność czujników i mechaniki. | |

### Rejestr pomiarów

| Data / godzina | Temperatura | Wilgotność | CO₂ | NH₃ | Uwagi |
|---|---:|---:|---:|---:|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

### Niezgodności / działania korygujące

| Nr | Problem / działanie | Odpowiedzialny | Data zamknięcia |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Decyzja o przekazaniu do pracy

☐ Dopuszczono do pracy pod nadzorem  
☐ Nie dopuszczono — wymagane poprawki  
☐ Dopuszczono do normalnej pracy po zakończeniu obserwacji

Uwagi / ograniczenia: ______________________________________________________

Osoba uruchamiająca: __________________________  Podpis: ____________________

Osoba odpowiedzialna za instalację: _____________  Podpis: ____________________

Data: ____________________

> **Ważne:** przy niezaliczonym punkcie bezpieczeństwa lub niepewnym pomiarze nie uruchamiaj systemu w normalnej pracy. Nie wykonuj testów 230 V ani obejść zabezpieczeń bez wymaganych kwalifikacji.
