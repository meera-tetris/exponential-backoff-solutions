# Python Implementation

## Demonstrations of HTTP retry logic with exponential backoff and jitter in Python.

---

### Running with Docker (No Python installation required)

#### Build the Docker image

```bash
docker build -t exponential-backoff .
```

#### Run the container

```bash
docker run exponential-backoff
```

#### Customize the URL and parameters

To test with a different URL, modify `main.py` line 23:

```python
request("https://your-url-here.com", 4, 1, 0.5, 5)
```

Then rebuild and run:

```bash
docker build -t exponential-backoff .
docker run exponential-backoff
```

### Parameters Explained

```python
request(url, max_retries, wait_time, jitter, timeout)
```

- **url**: The HTTP endpoint to request
- **max_retries**: Maximum number of retry attempts (e.g., 4)
- **wait_time**: Initial delay in seconds (e.g., 1 = 1 second)
- **jitter**: Random variance in seconds (e.g., 0.5 = ±0.5 seconds)
- **timeout**: Request timeout in seconds (e.g., 5)

### How It Works

The retry delays grow exponentially:

- Attempt 1: ~1.0s (1 × 2^0 ± jitter)
- Attempt 2: ~2.0s (1 × 2^1 ± jitter)
- Attempt 3: ~4.0s (1 × 2^2 ± jitter)
- Attempt 4: ~8.0s (1 × 2^3 ± jitter)

Jitter adds randomness to prevent thundering herd problems.

---
