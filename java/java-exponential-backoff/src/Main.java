public class Main {
    public static void main(String[] args) throws Exception {

        ExponentialBackoffWithJitter backOff = new ExponentialBackoffWithJitter(5, 1000, 16000);

//        backOff.callWithRetry("https://www.google.com");

        backOff.callWithRetry("https://invalid-url-test-123.com");

    }
}