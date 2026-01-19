import requests, random, time

def request(url, max_retries, wait_time, jitter, timeout):
    retries = 0

    while retries < max_retries:
        try:
            requests.get(url, timeout=timeout).raise_for_status()
            print("request successful", flush=True)
            return

        except requests.exceptions.RequestException:
            delay = wait_time * (2 ** retries) + random.uniform(-jitter, jitter)
            delay = max(0, delay)

            print(f"retrying in {delay:.2f} seconds", flush=True)
            time.sleep(delay)
            retries += 1

    print("request failed after max retries", flush=True)

request("http://www.youtubddffe.com/", 4, 1, 0.5, 5)
#request("https://google.com", 4, 1, 0.5, 5)
