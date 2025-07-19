import argparse
import os
import sys

PREKLADY = {
    "vypravaj": "print",
    "pocitaj(": "len(",
    "dlzka": "len",
    "pokad": "if",
    "je": "==",
    "jinak:": "else:",
    "jinak": "else",
    "more": "def",
    "vrati": "return",
}

def preloz_pajton_kod(kod):
    radky = kod.split("\n")
    nove_radky = []

    for riadok in radky:
        upraveny = riadok
        for pajton, python in PREKLADY.items():
            if pajton in upraveny:
                upraveny = upraveny.replace(pajton, python)
        nove_radky.append(upraveny)

    return "\n".join(nove_radky)

def spust_pajton_soubor(soubor):
    try:
        with open(soubor, "r", encoding="utf-8") as f:
            pajton_kod = f.read()
        python_kod = preloz_pajton_kod(pajton_kod)


        exec(python_kod, {"__name__": "__main__"})
    except FileNotFoundError:
        print(f"Soubor {soubor} nebyl nalezen.")
    except SyntaxError as e:
        print(f"Chyba v syntaxi kódu: {e}")
    except Exception as e:
        print(f"Chyba při spuštění souboru: {e}")

def main():
    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    parser = argparse.ArgumentParser(description="Interpreter pro soubory .pajton.")
    parser.add_argument("soubor", help="Název souboru .pajton, který chcete spustit.")
    args = parser.parse_args()

    soubor_path = os.path.join(base_path, args.soubor)
    spust_pajton_soubor(soubor_path)

if __name__ == "__main__":
    main()
