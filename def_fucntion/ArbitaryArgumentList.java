public class ArbitaryArgumentList {

    public static void main(String[] args) {
        System.out.println(concat("/", "earch", "mars", "venus", "谷军宇"));
        System.out.println(concat(",", "earch", "mars", "venus", "谷军宇"));
    }

    static String concat(String sep, String... args)  {
        java.util.StringJoiner sj = new java.util.StringJoiner(sep);
        for (String arg : args) {
            sj.add(arg);
        }

        return sj.toString();
    }
}
