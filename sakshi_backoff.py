import time, random, requests


def backoff(url, max_retries, base_delay, jitter, timeout):
    for i in range(max_retries):
        try:
            r = requests.get(url, timeout=timeout)

            if 200 <= r.status_code < 300:
                print("Success")
                print(r.text)
                return r.text

            raise Exception(f"HTTP error: {r.status_code}")

        except Exception as e:
            wait = base_delay * (2**i) + random.uniform(-jitter, jitter)
            wait = max(0, wait)

            print(f"Try {i + 1}")
            print(e)
            print(f"waiting {wait:.2f}s")
            time.sleep(wait)

    print("Request failed after max retries")


if __name__ == "__main__":
    backoff("https://mock.httpstatus.io/201", 3, 1.0, 0.25, 3.0)
