package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	// Zkontrolujeme, zda uživatel zadal argumenty
	if len(os.Args) < 2 {
		fmt.Println("Použití: pajton <název souboru .pajton>")
		os.Exit(1)
	}

	// Název souboru .pajton, který chceme spustit
	soubor := os.Args[1]

	// Získáme cestu ke spuštěnému Go programu (exe)
	exePath, err := os.Executable()
	if err != nil {
		fmt.Printf("Chyba při získávání cesty k programu: %v\n", err)
		os.Exit(1)
	}
	basePath := filepath.Dir(exePath) // Základní cesta k adresáři programu

	// Vytvoříme plnou cestu k Python skriptu (main.py) a souboru .pajton
	pythonScript := filepath.Join("C:/pajton/main.py")
	pajtonFile := filepath.Join(basePath, soubor)

	// Zkontrolujeme, zda Python skript existuje
	if _, err := os.Stat(pythonScript); os.IsNotExist(err) {
		fmt.Printf("Python skript nebyl nalezen: %s\n", pythonScript)
		os.Exit(1)
	}

	// Zkontrolujeme, zda .pajton soubor existuje
	if _, err := os.Stat(pajtonFile); os.IsNotExist(err) {
		fmt.Printf("Soubor .pajton nebyl nalezen: %s\n", pajtonFile)
		os.Exit(1)
	}

	// Spustíme Python skript s názvem souboru .pajton
	cmd := exec.Command("python", pythonScript, pajtonFile)
	cmd.Stdout = os.Stdout // Přesměrujeme výstup Pythonu na výstup Go programu
	cmd.Stderr = os.Stderr // Přesměrujeme chyby Pythonu na chyby Go programu

	// Spuštění příkazu
	err = cmd.Run()
	if err != nil {
		fmt.Printf("Chyba při spouštění Python skriptu: %v\n", err)
		os.Exit(1)
	}
}
