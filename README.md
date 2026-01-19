# Java Exponential Backoff with Jitter (Dockerized)

##  Overview

This project demonstrates how to implement HTTP retry logic in Java using:

- Exponential Backoff
- Jitter (randomized delay)
- Java HttpClient (Java 11+)
- Docker (to run without Java installed)

The goal is to safely retry failed HTTP calls without overloading servers
(thundering herd problem).

---

##  Why Exponential Backoff?

When a server goes down and comes back up, many clients retry at the same time.
This can overload the server again.

### Problems without backoff:
- Immediate retries
- Fixed retry intervals

### Solution:
- Exponential backoff increases wait time after each failure
- Jitter adds randomness so retries don’t happen simultaneously

---

##  Key Concepts Used

### 1️ Exponential Backoff

Retry delay increases exponentially:

| Attempt | Delay Formula |
|------|---------------|
| 1 | baseDelay × 2⁰ |
| 2 | baseDelay × 2¹ |
| 3 | baseDelay × 2² |
| 4 | baseDelay × 2³ |

This protects downstream services from overload.

---

### 2️ Jitter (Randomized Delay)

Jitter prevents all clients from retrying at the same moment.

```java
long jitterSleep =
    ThreadLocalRandom.current().nextLong(0, maxWaitTime);
