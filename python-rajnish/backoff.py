import time
import math
import random
import requests


def backoff(url: str, base_delay: float, max_retries: int, jitter: float) -> None:

    for retry_count in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            print("Response status:", response.status_code)
            return

        except requests.RequestException as err:
            # Calculate wait time only after failure 
            wait_time = base_delay * math.pow(2, retry_count)
            wait_time += random.random() * jitter

            print(
                f"Error connecting ({err})... retrying in {wait_time:.2f} seconds"
            )
            time.sleep(wait_time)

    print("retry limit reached")


def main():
    print("Exponential backoff with jitter")

    backoff(
        url="https://googl.com",
        base_delay=1.0,
        max_retries=4,
        jitter=0.25,
    )

if __name__ == "__main__":
    main()
