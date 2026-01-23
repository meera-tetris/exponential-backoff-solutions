saath/exponential-backoff-v2
Exponential Backoff Demo (Python)

This project demonstrates task retry logic using exponential backoff with optional jitter in Python. The mechanism retries a task multiple times when it fails, increasing the delay exponentially after each failure. A random jitter is added to avoid synchronized retries. The project also handles scenarios where the task fails even after the maximum number of retries, raising a RetryError.

Running with Docker (No Python installation required)

You can run the project using Docker without needing Python installed locally.

Build the Docker image:

cd exponential-backoff-solutions-saathvika
docker build -t exponential-backoff-demo .


Run the container:

docker run --rm exponential-backoff-demo

Customize the Task

To test with your own task, modify exponential_backoff_task.py:

def my_task():
    # Your task that may fail
    pass

result = exponential_backoff(
    task=my_task,
    base_delay=1.0,
    max_retries=5,
    jitter=0.2
)


Then rebuild and run the Docker container:

docker build -t exponential-backoff-demo .
docker run --rm exponential-backoff-demo

Parameters Explained
exponential_backoff(task, base_delay, max_retries, jitter, should_retry)


task: A callable function that may fail

base_delay: Initial delay in seconds before the first retry

max_retries: Maximum number of retry attempts

jitter: Random extra delay added to avoid synchronized retries

should_retry (optional): A function to decide whether to retry based on the exception and attempt number

How It Works

The retry delays grow exponentially with each attempt:

Attempt 1: base_delay × 2^0 + jitter

Attempt 2: base_delay × 2^1 + jitter

Attempt 3: base_delay × 2^2 + jitter

… and so on, until max_retries is reached.

If the task fails after all attempts, a RetryError is raised to indicate that the operation did not complete successfully.



