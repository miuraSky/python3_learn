public class RetFib {

    public static void main(String[] args) {
        System.out.println(retFib(2000));
    }

    static java.util.ArrayList retFib(int n) {
        java.util.ArrayList<Integer> list = new java.util.ArrayList<>();

        int a = 1, b = 2;
        while (a <= n) {
            list.add(a);
            int c = a + b;
            a = b;
            b = c;
        }

        return list;
    }
}
