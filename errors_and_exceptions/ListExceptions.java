import java.util.List;
import java.util.Arrays;

class B extends Exception {}
class C extends B {}
class D extends C {}

public class ListExceptions {

    public static void main(String[] args) {
        List<Class> list = Arrays.asList(B.class, C.class, D.class);

        for (Class clz : list) {
            try {
                Object exObj;
                try {
                    exObj = clz.newInstance();
                } catch (InstantiationException | IllegalAccessException ex) {
                    System.out.println("InstantiationException");
                    break;
                }

                if (exObj instanceof B) {
                    throw (B) exObj;
                }

                if (exObj instanceof C) {
                    throw (C) exObj;
                }

                if (exObj instanceof D) {
                    throw (D) exObj;
                }
            } catch (D e) {
                System.out.println('D');
            } catch (C e) {
                System.out.println('C');
            } catch (B e) {
                System.out.println('B');
            }
        }
    }
}



