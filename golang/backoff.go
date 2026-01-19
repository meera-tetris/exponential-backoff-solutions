package main

import (
	"fmt"
	"math"
	"math/rand/v2"
	"net/http"
	"time"
)

// backoff retries HTTP GET requests with exponential backoff and jitter until success or max retries reached.
func backoff(url string, baseDelay float64, maxRetries int, jitter float64) {
	for retryCount := 0; retryCount < maxRetries; retryCount++ {
		waitTime := baseDelay*math.Pow(2, float64(retryCount)) + rand.Float64()*jitter
		response, err := http.Get(url)
		if err == nil {
			defer response.Body.Close()
			fmt.Println("Response status: ", response.Status)
			return
		}
		fmt.Printf("Error connecting... retrying in %f seconds\n", waitTime)
		time.Sleep(time.Duration(waitTime * float64(time.Second)))
	}
	fmt.Println("retry limit reached")
}

func main() {
	fmt.Println("hello world")

	backoff("https://meerasundar.abcd", 1.0, 4, 0.25)
	//backoff("https://google.com", 1.0, 4, 0.25)
}
