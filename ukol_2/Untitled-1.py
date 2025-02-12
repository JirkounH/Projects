def precti_soubor():
    with open("emaily.txt", mode="r", encoding="UTF-8") as soubor:
        return soubor.readlines()
    
def projdi_vsechny_udaje(radky: list[str]):
    for radek in radky:
        if "end" in radek:
            break
        jmeno, domena = radek.split("@")
        

radky = precti_soubor ("emaily.txt")
