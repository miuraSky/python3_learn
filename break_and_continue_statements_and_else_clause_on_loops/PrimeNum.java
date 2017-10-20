public class PrimeNum {
    
    public static void main(String[] args) {
        for (int n = 2; n <= 10; n++) {
            int x = 2;
            for (;x < n; x ++) {
                if (n % x == 0) {
                    System.out.println(n + " equals " + x + " * " + (n / x));
                    break;
                }
            }

            if (x == n) {
                System.out.println(x + " is a prime number.");
            }
        }
    }
}
