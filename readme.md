
# Pajton - A Custom Python-like Language

**Pajton** is a meme language based on Python, created as a fun variation inspired by the "Zahorská" (Slovak) dialect. The language uses a humorous twist on Python's syntax to make coding more playful.

This repository contains both a Python interpreter and a Go program to run `.pajton` files. Choose either to execute your Pajton files based on your preference for Python or Go.

### Features:
- Translates specific words from the Zahorská dialect to Python syntax.
- Allows users to run `.pajton` files using either Python or Go.
- The Go program executes the Python interpreter internally, making it easy for users who prefer Go.

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
2. Ensure you have Python 3.x installed on your machine (for the Python interpreter).
3. Make sure you have Go installed (for the Go interpreter).
4. Save the `main.py` file (for Python) and the `main.go` file (for Go) in the same directory as your `.pajton` files.

---

## How to Use

You have two options for running `.pajton` files: using the **Python interpreter** or the **Go program**.

### 1. Using the Python Interpreter:
1. Write your code in a `.pajton` file.
2. To execute it with the Python interpreter, run the following command:

   ```bash
   python main.py <filename.pajton>
   ```

### 2. Using the Go Program:
1. Write your code in a `.pajton` file.
2. To execute it with the Go program, run the following command:

   ```bash
   pajton <filename.pajton> 
   ```

Where `<filename.pajton>` is the name of the `.pajton` file you want to run.

### Example:

#### `.pajton` File:

```pajton
more pozdrav():
    vypravaj("Ahoj, svet!")

pozdrav()

pocitaj_pocet = dlzka([1, 2, 3, 4])
vypravaj("Pocet prvkov v liste je: " + pocitaj_pocet)
```

#### Translated Python Code:

```python
def pozdrav():
    print("Ahoj, svet!")

pozdrav()

pocitaj_pocet = len([1, 2, 3, 4])
print("Pocet prvkov v liste je: " + pocitaj_pocet)
```

#### Command to Run (using Python interpreter):

```bash
python main.py example.pajton
```

#### Command to Run (using Go program):

```bash
pajton example.pajton
```

---

## Code Walkthrough

### 1. Python Interpreter (`pajton_interpreter.py`)

This script is responsible for translating `.pajton` files to Python code and executing them.

- **`preloz_pajton_kod(kod)`**: This function performs the translation from `.pajton` to Python by replacing specific keywords with Python equivalents.
- **`spust_pajton_soubor(soubor)`**: This function reads the `.pajton` file, translates it, and executes the resulting Python code.
- **`main()`**: Sets up argument parsing and handles the file execution process.

### 2. Go Program (`main.go`)

The Go program runs the Python interpreter internally to execute `.pajton` files. Here’s how it works:

- **`os.Args[1]`**: This fetches the `.pajton` filename passed as a command-line argument.
- **`os.Executable()`**: It finds the path to the Go executable and uses it to determine where the program is located.
- **`exec.Command("python", pythonScript, pajtonFile)`**: This runs the Python script (`main.py`) with the `.pajton` file as a parameter.

#### Go Program Breakdown:

```go
package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	// Check if the user provided arguments
	if len(os.Args) < 2 {
		fmt.Println("Usage: pajton <filename.pajton>")
		os.Exit(1)
	}

	// Get the filename of the .pajton file
	soubor := os.Args[1]

	// Get the path of the Go program (executable)
	exePath, err := os.Executable()
	if err != nil {
		fmt.Printf("Error getting executable path: %v\n", err)
		os.Exit(1)
	}
	basePath := filepath.Dir(exePath)

	// Define paths for the Python script and the .pajton file
	pythonScript := filepath.Join("C:/pajton/main.py")
	pajtonFile := filepath.Join(basePath, soubor)

	// Check if Python script exists
	if _, err := os.Stat(pythonScript); os.IsNotExist(err) {
		fmt.Printf("Python script not found: %s\n", pythonScript)
		os.Exit(1)
	}

	// Check if the .pajton file exists
	if _, err := os.Stat(pajtonFile); os.IsNotExist(err) {
		fmt.Printf("File .pajton not found: %s\n", pajtonFile)
		os.Exit(1)
	}

	// Run the Python script with the .pajton file as argument
	cmd := exec.Command("python", pythonScript, pajtonFile)
	cmd.Stdout = os.Stdout // Redirect stdout
	cmd.Stderr = os.Stderr // Redirect stderr

	// Run the command
	err = cmd.Run()
	if err != nil {
		fmt.Printf("Error running Python script: %v\n", err)
		os.Exit(1)
	}
}
```

### Key Steps:
1. **Argument Parsing**: The program expects the user to provide a `.pajton` file as an argument.
2. **Path Calculation**: It calculates the paths for both the Python interpreter and the `.pajton` file.
3. **File Existence Checks**: The Go program checks if both the Python script and the `.pajton` file exist.
4. **Command Execution**: The Python script is executed via the `exec` package with the `.pajton` file as its argument.

---

## Limitations and Notes

- **Syntax Support**: Currently, the Pajton interpreter supports a limited subset of Python features and only translates basic keywords.
- **Performance**: Running `.pajton` files requires an extra step of translation to Python, which may introduce slight performance overhead.
- **Humor**: Pajton is a meme language, not intended for serious production use. It’s a fun way to explore language translation and create humorous code.

---

Enjoy coding in Pajton! Feel free to contribute and improve this language further.
