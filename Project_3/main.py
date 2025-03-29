"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jiri Hubacek
email: hubacek108@gmail.com
"""

import sys
import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def validate_args(args):
    if len(args) != 3:
        print("Chyba: musíš zadat dva argumenty: <URL> <výstupní_soubor.csv>")
        sys.exit(1)
    if not args[1].startswith("https://www.volby.cz/pls/ps2017nss/ps32"):
        print("Chyba: první argument musí být odkaz na stránku územního celku (např. ps32...)")
        sys.exit(1)
    if not args[2].endswith(".csv"):
        print("Chyba: druhý argument musí být název výstupního souboru s příponou .csv")
        sys.exit(1)
    return args[1], args[2]

def get_obec_links(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("table", class_="table")
    links = []
    for row in table.find_all("tr")[2:]:
        tds = row.find_all("td")
        if len(tds) >= 2:
            code = tds[0].text.strip()
            name = tds[1].text.strip()
            a_tag = tds[0].find("a")
            if a_tag and "href" in a_tag.attrs:
                link = urljoin(url, a_tag["href"])
                links.append((code, name, link))
    return links

def scrape_obec(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

    tables = soup.find_all("table", class_="table")
    if not tables or len(tables) < 2:
        raise ValueError(f"Nelze najít potřebné tabulky na stránce {url}")
    
    # První tabulka: statistiky
    summary_table = tables[0]
    tds = summary_table.find_all("td")
    try:
        registered = int(tds[3].text.replace('\xa0', '').replace(' ', ''))
        envelopes = int(tds[4].text.replace('\xa0', '').replace(' ', ''))
        valid = int(tds[7].text.replace('\xa0', '').replace(' ', ''))
    except (IndexError, ValueError):
        raise ValueError(f"Chyba při zpracování počtů voličů na stránce {url}")

    # Všechny další tabulky: výsledky stran
    parties = {}
    result_tables = tables[1:]
    for table in result_tables:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                party = cols[1].text.strip()
                votes = int(cols[2].text.replace('\xa0', '').replace(' ', ''))
                parties[party] = votes

    return registered, envelopes, valid, parties

def main():
    url, output_file = validate_args(sys.argv)
    obce = get_obec_links(url)

    print(f"Nalezeno obcí: {len(obce)}")

    all_party_names = set()
    data_rows = []

    for code, name, link in obce:
        try:
            registered, envelopes, valid, parties = scrape_obec(link)
            all_party_names.update(parties.keys())
            row = {
                "code": code,
                "location": name,
                "registered": registered,
                "envelopes": envelopes,
                "valid": valid,
                **parties
            }
            data_rows.append(row)
            print(f"Načteno: {code} - {name}")
        except Exception as e:
            print(f"Chyba při zpracování obce {name} ({code}): {e}")

    sorted_parties = sorted(all_party_names)
    fieldnames = ["code", "location", "registered", "envelopes", "valid"] + sorted_parties

    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for row in data_rows:
            for party in sorted_parties:
                row.setdefault(party, 0)
            writer.writerow(row)

    print(f"Hotovo. Výsledky uloženy do: {output_file}")

if __name__ == "__main__":
    main()
