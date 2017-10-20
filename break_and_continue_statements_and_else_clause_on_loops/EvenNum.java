public class EvenNum {
    
    public static void main(String[] args) {
        for (int n = 2; n <= 10; n++) {
            if (n % 2 == 0) {
                System.out.println("Found an even number " + n);
                continue;
            }
            System.out.println("Found a number " + n);
        }
    }
}

