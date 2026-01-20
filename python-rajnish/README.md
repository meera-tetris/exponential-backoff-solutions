# Exponential Backoff with Jitter - Python Implementation

This Python implementation demonstrates an exponential backoff retry strategy with jitter for HTTP requests.

## What is Exponential Backoff?

Exponential backoff is a retry strategy where the wait time between retry attempts increases exponentially. This helps reduce load on a server that might be temporarily unavailable.

**Formula:** `wait_time = base_delay * 2^retry_count + random_jitter`

### Example Timeline:

- **Attempt 1:** Immediate (no wait)
- **Attempt 2:** Wait ~1 second (base_delay \* 2^0)
- **Attempt 3:** Wait ~2 seconds (base_delay \* 2^1)
- **Attempt 4:** Wait ~4 seconds (base_delay \* 2^2)

## What is Jitter?

Jitter adds randomness to the wait time to prevent multiple clients from retrying simultaneously (avoiding the "thundering herd" problem).

## Running with Docker

### Build the Docker image:

**Option 1: Build from the `python-rajnish` directory (recommended)**

```bash
cd python-rajnish
docker build -t exponential-backoff-python .
```

**Option 2: Build from the parent directory**

```bash
docker build -t exponential-backoff-python -f python-rajnish/Dockerfile python-rajnish
```

### Run the container:

```bash
docker run exponential-backoff-python
```

## Running Locally

### Prerequisites:

- Python 3.7 or higher
- pip (Python package manager)

### Installation:

```bash
pip install -r requirements.txt
```

### Execution:

```bash
python backoff.py
```

## Customization

You can modify the parameters in `main()` function:

- `url`: The URL to connect to
- `base_delay`: Initial delay in seconds (default: 1.0)
- `max_retries`: Maximum number of retry attempts (default: 4)
- `jitter`: Maximum random jitter in seconds (default: 0.25)
- `timeout`: Request timeout in seconds (default: 5.0)

## How It Works

1. The function attempts to make an HTTP GET request to the specified URL
2. If the request fails (network error, timeout, or HTTP error status), it calculates the wait time using exponential backoff
3. Random jitter is added to the wait time
4. The function waits for the calculated time before retrying
5. This process repeats until either:
   - The request succeeds (returns status code)
   - All retry attempts are exhausted (returns None)
