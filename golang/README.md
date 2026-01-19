# Go Implementation

## Demonstrations of HTTP retry logic with exponential backoff and jitter in Go.
---

### Running with Docker (No Go installation required)

#### Build the Docker image
```bash
cd golang
docker build -t backoff-demo .
```

#### Run the container
```bash
docker run backoff-demo
```

#### Customize the URL and parameters

To test with a different URL, modify `backoff.go` line 30:
```go
backoff("https://your-url-here.com", 1.0, 4, 0.25)
```

Then rebuild and run:
```bash
docker build -t backoff-demo .
docker run backoff-demo
```

### Parameters Explained

```go
backoff(url, baseDelay, maxRetries, jitter)
```

- **url**: The HTTP endpoint to request
- **baseDelay**: Initial delay in seconds (e.g., 1.0 = 1 second)
- **maxRetries**: Maximum number of retry attempts (e.g., 4)
- **jitter**: Random variance as a decimal (e.g., 0.25 = ±25%)

### How It Works

The retry delays grow exponentially:
- Attempt 1: ~1.0s (1 × 2^0 + jitter)
- Attempt 2: ~2.0s (1 × 2^1 + jitter)
- Attempt 3: ~4.0s (1 × 2^2 + jitter)
- Attempt 4: ~8.0s (1 × 2^3 + jitter)

Jitter adds randomness to prevent thundering herd problems.

---
