import time
import random
from typing import Callable, Optional


class RetryError(Exception):
    """Raised when a task fails after all retry attempts are exhausted."""
    pass


def exponential_backoff(
    task: Callable[[], any],
    base_delay: float = 1.0,
    max_retries: int = 5,
    jitter: float = 0.1,
    should_retry: Optional[Callable[[Exception, int], bool]] = None
) -> any:
    """
    Retry a task using exponential backoff with optional jitter.

    Args:
        task: A callable task that may fail and raise exceptions.
        base_delay: Initial wait time before first retry (seconds).
        max_retries: Maximum number of retry attempts.
        jitter: Random extra delay to avoid synchronized retries.
        should_retry: Optional function to decide retry behavior.

    Returns:
        Result returned by the task if it succeeds.

    Raises:
        RetryError: When maximum retries are reached.
    """

    attempt = 0

    while attempt < max_retries:
        try:
            result = task()
            print(f"[SUCCESS] Task completed on attempt {attempt + 1}")
            return result

        except Exception as exc:
            attempt += 1

            # If retries exhausted, stop gracefully
            if attempt == max_retries:
                print(
                    f"[FINAL FAILURE] Maximum retries reached. "
                    f"Last error: {exc}"
                )
                break

            # Optional retry decision
            if should_retry and not should_retry(exc, attempt):
                print(f"[ABORT] Retry stopped at attempt {attempt}: {exc}")
                raise

            # Exponential backoff with jitter
            delay = base_delay * (2 ** (attempt - 1))
            delay += random.uniform(0, jitter)

            print(
                f"[RETRY] Attempt {attempt} failed: {exc}. "
                f"Retrying in {delay:.2f} seconds..."
            )
            time.sleep(delay)

    # Explicit failure after retries
    raise RetryError(f"Task failed after {max_retries} attempts")



def failure_simulation_task():
    """Fails consistently to simulate retry exhaustion."""
    raise ValueError("forced failure for testing")



def retryable_task():
    """Randomly fails to demonstrate exponential backoff."""
    if random.random() < 0.6:
        raise ValueError("short term failure")
    return "Task finished successfully!"


if __name__ == "__main__":
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

    print("\n=== Random failure demo ===")
    try:
        result = exponential_backoff(
            task=retryable_task,
            base_delay=0.5,
            max_retries=5,
            jitter=0.2
        )
        print(result)
    except RetryError as e:
        print(e)
