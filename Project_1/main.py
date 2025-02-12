# Definice uzivatelu
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Definice textu
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Prihlaseni uzivatele
username = input("Zadejte uzivatelske jmeno: ")
password = input("Zadejte heslo: ")

if username in registered_users and registered_users[username] == password:
    print(f"Vitejte, {username}!")
    
    # Vyber textu
    print("Mame k dispozici 3 texty.")
    text_choice = input("Zadejte cislo textu (1-3): ")

    if text_choice.isdigit():
        text_choice = int(text_choice)
        if 1 <= text_choice <= 3:
            selected_text = TEXTS[text_choice - 1]
            words = selected_text.split()

            # Analyza textu
            total_words = len(words)
            capitalized_words = len([word for word in words if word.istitle()])
            uppercase_words = len([word for word in words if word.isupper() and word.isalpha()])
            lowercase_words = len([word for word in words if word.islower()])
            numeric_strings = [word for word in words if word.isdigit()]
            numeric_sum = sum(map(int, numeric_strings))

            # Vysledky analyzy
            print(f"\nAnalyza textu {text_choice}:")
            print(f"Pocet slov: {total_words}")
            print(f"Pocet slov zacinajicich velkym pismenem: {capitalized_words}")
            print(f"Pocet slov psanych velkymi pismeny: {uppercase_words}")
            print(f"Pocet slov psanych malymi pismeny: {lowercase_words}")
            print(f"Pocet cisel: {len(numeric_strings)}")
            print(f"Suma vsech cisel: {numeric_sum}")

            # Sloupcovy graf delky slov
            word_lengths = {}
            for word in words:
                length = len(word.strip(",."))
                if length > 0:
                    word_lengths[length] = word_lengths.get(length, 0) + 1

            print("\nSloupcovy graf cetnosti delky slov:")
            for length, count in sorted(word_lengths.items()):
                print(f"{length:2}| {'*' * count} {count}")

        else:
            print("Chyba: Zvolene cislo textu neni v rozsahu 1-3. Program se ukoncuje.")
    else:
        print("Chyba: Zadali jste neplatny vstup (neni to cislo). Program se ukoncuje.")
else:
    print("Neplatne prihlasovaci udaje. Program se ukoncuje.")
