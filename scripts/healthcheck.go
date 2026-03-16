package main

import (
    "fmt"
    "net/http"
    "os"
)

// healthcheck.go lives in scripts to test Go parsing in mixed repo.
func main() {
    port := os.Getenv("PORT")
    if port == "" {
        port = "8081"
    }
    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "ok")
    })
    fmt.Printf("starting healthcheck server on %s (not really)\n", port)
}
