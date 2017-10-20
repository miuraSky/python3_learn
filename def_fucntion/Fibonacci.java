public class Fibonacci {

    public static void main(String[] args) {
        fibonacci(2000);
    }

    static void fibonacci(int n) {
        if (n <= 0) {
            System.out.println("Illegal paramter: n <=0");
            return;
        }

        int a = 1, b = 2;
        while (a <= n) {
            System.out.print(a + " ");
            int c = a + b;
            a = b;
            b = c;
        }

        System.out.println();
    }
}
