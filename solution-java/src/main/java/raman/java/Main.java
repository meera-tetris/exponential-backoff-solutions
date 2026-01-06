package raman.java;

public class Main {

    public static void main(String[] args) {

        //ExponentialBackoff.hittingUrlWithJitter("https://mock.httpstatus.io/201",5,4);
	ExponentialBackoff.hittingUrlWithJitter("https://www.google.com", 5, 4);

    }
}
