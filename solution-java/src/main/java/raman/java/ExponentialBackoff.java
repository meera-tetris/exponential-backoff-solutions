package raman.java;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.concurrent.ThreadLocalRandom;

public class ExponentialBackoff {

    public static void hittingUrlWithJitter (String url, int maxSteps, long timeoutSeconds) {
        HttpClient httpClient = HttpClient.newHttpClient();
        HttpRequest httpRequest = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .timeout(Duration.ofSeconds(timeoutSeconds))
                .build();
        long baseDelay = 1000;

        for (int i = 1; i <= maxSteps; i++){
            long startTime = System.currentTimeMillis();

            try{
                System.out.println("Attempt :" + i );

                HttpResponse<Void> response = httpClient.send(httpRequest,HttpResponse.BodyHandlers.discarding());

                if (response.statusCode() == 200){
                    long timeTaken = System.currentTimeMillis() - startTime;
                    System.out.println("SUCCESS! "+ timeTaken + " ms taken");
                    return;
                } else {
                    System.out.println("Failed :" + response.statusCode());
                }

            }catch (Exception e){
                System.out.println("Failed to connect " + e.getMessage());
            }

            if (i == maxSteps){
                System.out.println("STOPPED. Max attempts reached");
                break;
            }

            long maxWaitTime = baseDelay * (1L << (i - 1));
            long jitterSleep = ThreadLocalRandom.current().nextLong(0, maxWaitTime);
            long totalWait = maxWaitTime + jitterSleep;
            System.out.println("Waiting "+ totalWait + "ms before next retry");

            try {
                Thread.sleep(jitterSleep);
            }catch (InterruptedException e){}

        }
    }

    public static void main(String[] args){
//        hittingUrlWithJitter("https://www.google.com",5);
        hittingUrlWithJitter("https://www.raman.com",3,3);
    }
}