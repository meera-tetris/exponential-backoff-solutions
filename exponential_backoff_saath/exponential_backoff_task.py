import time
import random
from typing import Callable, Optional


class RetryError(Exception):
    """Raised when a task fails after all retry attempts are finished."""
    pass


def exponential_backoff(
    task: Callable[[], any],
    base_delay: float = 1.0,
    max_retries: int = 5,
    jitter: float = 0.1,
    should_retry: Optional[Callable[[Exception, int], bool]] = None
) -> any:
    attempt = 0
    last_exception = None  

    while attempt < max_retries:
        try:
            result = task()
            print(f"[SUCCESS] Task completed on attempt {attempt + 1}")
            return result
        except Exception as exc:
            last_exception = exc
            attempt += 1

            if should_retry and not should_retry(exc, attempt):
                raise

            delay = base_delay * (2 ** (attempt - 1))
            delay += random.uniform(0, jitter)

            print(
                f"[RETRY] Attempt {attempt} failed: {exc}. "
                f"Retrying in {delay:.2f} seconds..."
            )
            time.sleep(delay)

    print(
        f"[FINAL FAILURE] Maximum retries reached. "
        f"Last error: {last_exception}"
    )
    raise RetryError(f"Task failed after {max_retries} attempts")


# ------------------ Failure Simulation ------------------

def failure_simulation_task():
    raise RuntimeError("forced failure for testing")


print("=== Simulating maximum retry failure scenario ===")
try:
    exponential_backoff(
        task=failure_simulation_task,
        base_delay=0.5,
        max_retries=3,
        jitter=0.2
    )
except RetryError as e:
    print(e)
