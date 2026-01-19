Exponential Backoff Demo (Python + Docker)
This project shows a simple implementation of exponential backoff with jitter.
The script keeps retrying a request when it fails, waiting longer each time:

1s → 2s → 4s → 8s …


Jitter adds a small random delay so all retries don’t hit the server at the same time.

Project Structure
.
├── sakshi_backoff.py
├── requirements.txt
└── Dockerfile

Run locally (without Docker)

Create a virtual environment
python -m venv venv

Activate the virtual environment
venv\Scripts\Activate

Come inside folder
cd python_sakshi

Install dependencies:
pip install -r requirements.txt

Run the script:
python sakshi_backoff.py

Run with Docker
Build the image
docker build -t backoff-demo .

Run the container
docker run --rm backoff-demo

Code Settings
Inside sakshi_backoff.py, you can change:

backoff(
    "https://mock.httpstatus.io/500",  # URL
    3,                         # max retries
    1.0,                       # base delay
    0.25,                      # jitter
    3.0                        # timeout
)