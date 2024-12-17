# Pajton - A Custom Python-like Language

**Pajton** is a meme language created as a fun variation of Python, inspired by the "Zahorská" (Slovak) dialect. It is not intended for serious use, but rather as a humorous take on Python's syntax, making the language more playful and entertaining.

### Features:
- Translates specific words from Slovak (Zahorská) dialect to Python syntax.
- Allows users to run `.pajton` files, which are interpreted as regular Python code after translation.

### How it works:
The interpreter reads the `.pajton` file, replaces specific keywords with the corresponding Python commands, and then executes the translated Python code.

### Common Translations:
- **vypravaj** → `print`
- **pocitaj(** → `len(`
- **dlzka** → `len`
- **pokad** → `if`
- **je** → `==`
- **jinak:** → `else:`
- **jinak** → `else`
- **more** → `def`
- **vrati** → `return`

---

## Installation

1. Clone or download the repository.
2. Ensure you have Python 3.x installed on your machine.
3. Save the interpreter script (`pajton_interpreter.py`) in the same directory as your `.pajton` files.
4. You can then run the `.pajton` files through the interpreter.

---

## How to Use

1. Write your code in `.pajton` files using the custom syntax.
2. To execute a `.pajton` file, run the interpreter using the command line.

### Command-line Usage:
```
python pajton_interpreter.py <filename.pajton>
```

Where `<filename.pajton>` is the name of the `.pajton` file you want to run. The file must be located in the same directory as the interpreter script.

---

## Example

### `.pajton` File:

```pajton
more pozdrav():
    vypravaj("Ahoj, svet!")

pozdrav()

pocitaj_pocet = dlzka([1, 2, 3, 4])
vypravaj("Pocet prvkov v liste je: " + pocitaj_pocet)
```

### Translated Python Code:

```python
def pozdrav():
    print("Ahoj, svet!")

pozdrav()

pocitaj_pocet = len([1, 2, 3, 4])
print("Pocet prvkov v liste je: " + pocitaj_pocet)
```

### Command to Run:
```bash
python pajton_interpreter.py example.pajton
```

---

## Code Walkthrough

The interpreter script (`pajton_interpreter.py`) includes the following key components:

### 1. **preloz_pajton_kod(kod)**

This function translates the custom `.pajton` code to standard Python syntax. It uses `str.replace()` to swap keywords like `vypravaj` with `print`, and `pokad` with `if`.

### 2. **spust_pajton_soubor(soubor)**

This function opens and reads the `.pajton` file, then processes the code through the `preloz_pajton_kod()` function. It attempts to execute the translated Python code, handling file errors and syntax issues.

### 3. **main()**

This function sets up command-line argument parsing with `argparse`, which allows users to specify the filename of the `.pajton` code they want to run. It uses the `spust_pajton_soubor()` function to execute the file.

---

## Example Script Breakdown

Here’s the Python code for the interpreter:

```python
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
```

---

## Limitations and Notes

- **Syntax**: The current version of Pajton only supports basic translations for some common Python keywords. More complex features of Python are not yet supported.
- **Performance**: Pajton code is first translated to Python, and then executed. This introduces an overhead compared to directly running Python code.
- **Humor**: Pajton is a meme and not intended for serious projects. It should be used for fun and as an educational tool to explore how interpreters and compilers work.

---

Enjoy coding in Pajton! If you encounter any issues or would like to add more features, feel free to contribute or send feedback.
