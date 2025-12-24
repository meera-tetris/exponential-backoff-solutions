import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.concurrent.ThreadLocalRandom;

public class ExponentialBackoffWithJitter {

    private final int maxTries;
    private final long baseDelayMillis;
    private final long maxDelayMillis;

    public ExponentialBackoffWithJitter(int maxTries, long baseDelayMillis, long maxDelayMillis) {
        this.maxTries = maxTries;
        this.baseDelayMillis = baseDelayMillis;
        this.maxDelayMillis = maxDelayMillis;
    }

    public void callWithRetry(String urlStr) throws Exception {
        int attempt = 0;

        while (true) {
            try {
                int statusCode = makeHttpCall(urlStr);
                System.out.println("Success! HTTP Status: " + statusCode);
                return;
            } catch (Exception ex) {
                attempt++;

                if (attempt > maxTries) {
                    System.out.println("Max retries reached. Giving up.");
                    throw ex;
                }

                long delay = calculateJitterDelay(attempt);
                System.out.println("Retry " + attempt + " after " + delay + " ms due to: " + ex.getMessage());

                Thread.sleep(delay);
            }
        }
    }

    private int makeHttpCall(String urlStr) throws Exception {
        URL url = URI.create(urlStr).toURL();
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        connection.setRequestMethod("GET");
        connection.setConnectTimeout(3000);
        connection.setReadTimeout(3000);

        int statusCode = connection.getResponseCode();

        if (statusCode < 200 || statusCode >= 300) {
            throw new RuntimeException("Non-success response: " + statusCode);
        }

        return statusCode;
    }

    private long calculateJitterDelay(int attempt) {
        long exponentialDelay = baseDelayMillis * (1L << (attempt - 1));
        long cappedDelay = Math.min(exponentialDelay, maxDelayMillis);

        return ThreadLocalRandom.current().nextLong(0, cappedDelay + 1);
    }
}
