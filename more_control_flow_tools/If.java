public class If {

    public static void main(String[] args) {
        System.out.print("Please enter an integer: ");

        java.util.Scanner scanner = new java.util.Scanner(System.in);
        int x = scanner.nextInt();

        if (x < 0) {
            x = 0;
            System.out.println("Negative changed to zero");
        } else if (x == 0) {
            System.out.println("Zero");
        } else if (x == 1) {
            System.out.println("Single");
        } else {
            System.out.println("More");
        }

    }
}
