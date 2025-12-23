import time
import random
import requests


def backoff(url, max_retries, base_delay, jitter, timeout):
    try:
        requests.get(url, timeout=timeout)
    except:
        return
    for i in range(max_retries):
        try:
            print(f"try {i+1}")
            r = requests.get(url, timeout=timeout)
            if r.status_code == 200:
                return r.text
        except:
            pass

        wait = base_delay * (2**i)
        wait += random.uniform(-jitter, jitter)

        if wait < 0:
            wait = 0

        print(f"waiting {wait:.2f}s")
        time.sleep(wait)


if __name__ == "__main__":
    backoff("https://httpstat.us/503", 5, 1.0, 0.25, 3.0)
# https://httpstat.us/503
