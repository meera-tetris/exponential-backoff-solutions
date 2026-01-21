# Exponential Backoff Solutions

This repository demonstrates **Exponential Backoff with Jitter** using a Java HTTP example.

---

## Java – HTTP Exponential Backoff with Jitter

### Behaviour
- Successful call → no retry
- Failed / invalid URL → retry enabled
- Exponential delay (2ⁿ)
- Delay randomized using jitter
- Graceful exit after maximum retries

---

## Folder Structure

java/ 
    exponential-backoff/ 
        ExponentialBackoffWithJitter.java 
        Main.java

---

## Run Locally

```bash
javac java/exponential-backoff/*.java
java -cp java/exponential-backoff Main
```

## Run Using Docker

```bash
docker build -t exponential-backoff-java .
docker run --rm exponential-backoff-java
```



