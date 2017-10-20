public class ExceptionHandlePlace {

    public static void main(String[] args) {
        try {
            fail();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    static void fail() {
        double d = 1 / 0;
    }
}
