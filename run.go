package main

import (
    "fmt"
    "os"
    "os/exec"
)

func main() {
    // Get the current working directory
    currentDirectory, err := os.Getwd()
    if err != nil {
        fmt.Println(err)
        return
    }

    // Look for main.go in the current directory
    mainFile := fmt.Sprintf("%s/main.py", currentDirectory)

    // Check if main.go exists
    if _, err := os.Stat(mainFile); os.IsNotExist(err) {
        fmt.Println("main.go not found in the current directory.")
        return
    }

    // Run main.py in the command line
    cmd := exec.Command("python", mainFile)
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    if err := cmd.Run(); err != nil {
        fmt.Println(err)
        return
    }
}