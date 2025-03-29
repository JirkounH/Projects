# Výsledky voleb - Scraper

Tento nástroj slouží ke stažení výsledků voleb do Poslanecké sněmovny z webu volby.cz a jejich uložení do CSV souboru.

## Popis

- Stáhne výsledky hlasování za všechny obce v daném okrese/kraji.
- Výstupní soubor obsahuje:
  - Kód obce
  - Název obce
  - Počet voličů
  - Vydané obálky
  - Platné hlasy
  - Hlasy pro jednotlivé politické strany

CSV soubor je připraven pro otevření v Microsoft Excel (kódování UTF-8 s BOM, oddělovač `;`).

## Instalace

Doporučeno spouštět ve virtuálním prostředí.

1. Stáhni soubor `main.py` a `requirements.txt`.
2. Nainstaluj potřebné knihovny:

