"""
Exponential Backoff with Jitter Implementation

"""

import time
import math
import random
import requests
from typing import Optional


def backoff(
    url: str,
    base_delay: float,
    max_retries: int,
    jitter: float,
    timeout: float = 5.0,
) -> Optional[int]:
    """
    Retries an HTTP GET request with exponential backoff and jitter.

    This function attempts to make an HTTP GET request to the specified URL.
    If the request fails, it waits for an exponentially increasing amount of time
    (with added jitter) before retrying. The wait time doubles with each retry attempt.

    Returns:
        The HTTP status code if the request succeeds, None if all retries are exhausted.

    Example:
        >>> backoff("https://api.example.com", base_delay=1.0, max_retries=4, jitter=0.25)
        Error connecting (Connection timeout)... retrying in 1.15 seconds
        Response status: 200
        200
    """
    for retry_count in range(max_retries):
        try:
            # Attempt the HTTP GET request
            response = requests.get(url, timeout=timeout)
            
            # Raise an exception for HTTP error status codes (4xx, 5xx)
            response.raise_for_status()

            print(f"Response status: {response.status_code}")
            return response.status_code

        except requests.RequestException as err:
           
            wait_time = base_delay * math.pow(2, retry_count)
            
            # Add random jitter to prevent synchronized retries from multiple clients
            # This helps avoid the "thundering herd" problem
            wait_time += random.random() * jitter

            # Check if this was the last retry attempt
            if retry_count == max_retries - 1:
                print(
                    f"Error connecting ({err})... retry limit reached after "
                    f"{max_retries} attempts"
                )
            else:
                print(
                    f"Error connecting ({err})... retrying in {wait_time:.2f} seconds "
                    f"(attempt {retry_count + 1}/{max_retries})"
                )
                time.sleep(wait_time)

    print("All retry attempts exhausted. Request failed.")
    return None


def main() -> None:
    """
    Main entry point for the exponential backoff demonstration.

    """
    print("Exponential backoff with jitter")

    result = backoff(
        url="https://googl.com",
        base_delay=1.0,  
        max_retries=4,   
        jitter=0.25,     
    )

    if result is None:
        print("\nFailed to connect after all retry attempts.")
    else:
        print(f"\nSuccessfully connected with status code: {result}")


if __name__ == "__main__":
    main()
