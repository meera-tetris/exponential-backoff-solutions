# Multi-stage build: compile in one container, run in a minimal container
FROM golang:1.23-alpine AS builder

WORKDIR /app

# Copy the Go source file
COPY backoff.go .

# Build a static binary
RUN go build -o backoff backoff.go

# Final stage: minimal runtime image
FROM alpine:latest

# Copy only the compiled binary from builder stage
COPY --from=builder /app/backoff /usr/local/bin/backoff

# Run the program
CMD ["backoff"]
