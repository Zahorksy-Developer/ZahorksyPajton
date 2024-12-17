import argparse
import os
import sys

def preloz_pajton_kod(kod):
    # Převody záhorské syntaxe na Python
    kod = kod.replace("vypravaj", "print")
    kod = kod.replace("pocitaj(", "(")
    kod = kod.replace("dlzka", "len")
    kod = kod.replace("pokad", "if")
    kod = kod.replace("je", "==")
    kod = kod.replace("jinak:", "else:")
    kod = kod.replace("jinak", "else")
    kod = kod.replace("more", "def")
    kod = kod.replace("vrati", "return")
    return kod

def spust_pajton_soubor(soubor):
    try:
        with open(soubor, "r", encoding="utf-8") as f:
            pajton_kod = f.read()
        python_kod = preloz_pajton_kod(pajton_kod)
        exec(python_kod)
    except FileNotFoundError:
        print(f"Soubor {soubor} nebyl nalezen.")
    except SyntaxError as e:
        print(f"Chyba v syntaxi kódu: {e}")
    except Exception as e:
        print(f"Chyba při spuštění souboru: {e}")

def main():
    # Zjistíme cestu ke spuštěnému programu
    base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Nastavení argumentů pro soubor
    parser = argparse.ArgumentParser(description="Interpreter pro soubory .pajton.")
    parser.add_argument(
        "soubor",
        help="Název souboru .pajton, který chcete spustit (musí být ve stejné složce jako tento program)",
    )
    args = parser.parse_args()

    # Spojíme základní cestu s názvem souboru
    soubor_path = os.path.join(base_path, args.soubor)

    # Spustíme soubor
    spust_pajton_soubor(soubor_path)

if __name__ == "__main__":
    main()
