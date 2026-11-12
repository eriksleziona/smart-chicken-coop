# Checklista montażowa

## Inteligentny kurnik — ESP32 / MicroPython

**Wydruk:** A4 · **Wersja dokumentu:** 1.0

### Dane instalacji

| Pole | Wartość |
|---|---|
| Lokalizacja / nazwa kurnika | |
| Data montażu | |
| Osoba wykonująca montaż | |
| Osoba odpowiedzialna za instalację elektryczną | |
| Wersja firmware / konfiguracji | |

### 1. Przygotowanie i bezpieczeństwo

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | Dostępne są aktualne schematy, instrukcje urządzeń i zatwierdzony plan instalacji. |
| ☐ OK ☐ NOK ☐ N/D | Zasilanie jest odłączone i zabezpieczone przed przypadkowym załączeniem na czas montażu. |
| ☐ OK ☐ NOK ☐ N/D | Instalację 230 V wykonuje osoba z wymaganymi kwalifikacjami, zgodnie z lokalnymi przepisami. |
| ☐ OK ☐ NOK ☐ N/D | Obwody sieciowe i niskonapięciowe są rozdzielone zgodnie z projektem oraz wymaganiami obudowy i urządzeń. |
| ☐ OK ☐ NOK ☐ N/D | Nie ma odsłoniętych przewodów ani niezabezpieczonych połączeń; nie użyto płytki stykowej w obwodach sieciowych. |
| ☐ OK ☐ NOK ☐ N/D | Obudowa i przepusty przewodów są odpowiednie do przewidywanego zapylenia, wilgoci i warunków środowiskowych. |
| ☐ OK ☐ NOK ☐ N/D | Wyłącznik, zabezpieczenia i uziemienie/ochrona przeciwporażeniowa zostały dobrane i sprawdzone przez osobę odpowiedzialną. |

### 2. Miejsce i elementy mechaniczne

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | Miejsce montażu sterownika jest suche, osłonięte i dostępne do serwisu. |
| ☐ OK ☐ NOK ☐ N/D | Wentylator, wloty i wyloty odpowiadają zatwierdzonemu układowi; strumień powietrza nie powoduje przeciągu bezpośrednio na ptaki. |
| ☐ OK ☐ NOK ☐ N/D | Drzwi i napęd poruszają się swobodnie w całym zakresie, bez zacięć i punktów przycięcia. |
| ☐ OK ☐ NOK ☐ N/D | Ograniczniki i krańcówki drzwi są zamocowane, dostępne do regulacji i zabezpieczone przed przypadkowym przestawieniem. |
| ☐ OK ☐ NOK ☐ N/D | Przewidziano bezpieczne, ręczne uwolnienie lub obsługę drzwi po zaniku zasilania, zgodnie z projektem. |
| ☐ OK ☐ NOK ☐ N/D | Kable są chronione przed wilgocią, gryzoniami, ptakami, ruchem drzwi i uszkodzeniami mechanicznymi. |

### 3. Czujniki i prowadzenie przewodów

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | SHT31 i SCD41 są zamontowane w reprezentatywnym miejscu, z dala od bezpośredniego nawiewu i źródeł ciepła. |
| ☐ OK ☐ NOK ☐ N/D | Model czujnika NH₃ i jego wymagany układ kondycjonowania/kalibracji są potwierdzone dokumentacją producenta. |
| ☐ OK ☐ NOK ☐ N/D | Czujniki są dostępne do kontroli i nie są zasłonięte przez karmniki, poidła ani elementy konstrukcji. |
| ☐ OK ☐ NOK ☐ N/D | Przewody sygnałowe prowadzone są zgodnie z projektem, z ograniczeniem zakłóceń od silników, przekaźników i przewodów zasilających. |
| ☐ OK ☐ NOK ☐ N/D | Poziomy napięć, polaryzacja, podciąganie wejść i wspólne/izolowane odniesienia masy są zgodne ze schematami urządzeń. |
| ☐ OK ☐ NOK ☐ N/D | Oznaczenia przewodów i zacisków odpowiadają schematowi i mapie pinów zastosowanej wersji sprzętu. |

### 4. Sterownik i elementy wykonawcze

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | Zastosowana płytka ESP32 i jej wariant pinów są zgodne z dokumentacją konfiguracji. |
| ☐ OK ☐ NOK ☐ N/D | Wejścia analogowe ESP32 nie przekraczają dopuszczalnych napięć; sygnały mają wymagane kondycjonowanie. |
| ☐ OK ☐ NOK ☐ N/D | Sterowniki przekaźników/MOSFET i zasilacze są dobrane do obciążeń, prądów rozruchowych i warunków pracy. |
| ☐ OK ☐ NOK ☐ N/D | Sterowanie silnikiem drzwi ma sprzętowe zabezpieczenia wymagane przez projekt; oba kierunki nie mogą być aktywne jednocześnie. |
| ☐ OK ☐ NOK ☐ N/D | Wentylator i oświetlenie mają właściwe zabezpieczenia oraz nie obciążają bezpośrednio GPIO ESP32. |
| ☐ OK ☐ NOK ☐ N/D | Buzzer/alarm i lokalny sposób sygnalizacji są zamontowane i widoczne/słyszalne w miejscu obsługi. |

### 5. Dokumentacja powykonawcza

| Status | Kontrola |
|---|---|
| ☐ OK ☐ NOK ☐ N/D | Zapisano rzeczywistą mapę pinów, numery urządzeń i wersje modułów. |
| ☐ OK ☐ NOK ☐ N/D | Zaznaczono na planie lokalizację sterownika, czujników, wentylatora, napędu i zabezpieczeń. |
| ☐ OK ☐ NOK ☐ N/D | Zapisano odstępstwa od projektu i przekazano je osobie odpowiedzialnej przed uruchomieniem. |
| ☐ OK ☐ NOK ☐ N/D | Obudowa jest zamknięta, a wszystkie przepusty i osłony są poprawnie założone. |

### Niezgodności / uwagi

| Nr | Opis niezgodności lub wykonanej korekty | Osoba / data zamknięcia |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

### Zatwierdzenie montażu

**Montaż zakończony:** ☐ Tak ☐ Nie  
**Dopuszczono do kontrolowanego uruchomienia:** ☐ Tak ☐ Nie  

Imię i nazwisko: ______________________________  
Podpis: _______________________________________  
Data: _________________________________________

> **Ważne:** „NOK” w punkcie dotyczącym bezpieczeństwa oznacza wstrzymanie uruchomienia do czasu usunięcia problemu i ponownej kontroli.
