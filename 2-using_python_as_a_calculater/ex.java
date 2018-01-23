import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Ex {

    public static void main(String[] args) {
        boolean theWorldIsFlat = true;
        if (theWorldIsFlat) {
            System.out.println("Be careful not to fall off!");
        }

        // Strings in JAVA
        String word = "Python";
        System.out.println(word.charAt(0));
        System.out.println(word.charAt(word.length() - 1));

        System.out.println(word.substring(0, 2));
        System.out.println(word.substring(2, 5));
        System.out.println(word.substring(0, 5));
        System.out.println(word.substring(word.length() - 2, word.length())); 
        System.out.println("word length: " + word.length());
        // ERROR: String index out of range:-4
        // System.out.println(word.substring(word.length() - 2, 0)); 
       
        // strings is a object  
        
        // Lists in JAVA
        List<Integer> squares = Arrays.asList(1, 4, 9, 16, 25);
        System.out.println(squares);
        System.out.println(squares.get(0));
        System.out.println(squares.get(squares.size() - 1));
        System.out.println(Arrays.asList(Arrays.copyOfRange(squares.toArray(), squares.size() - 3, squares.size())));

        List<Integer> squaresCopy = Arrays.asList((Integer[])Arrays.copyOfRange(squares.toArray(), 0, squares.size()));
        System.out.println(squaresCopy);

        List<Integer> squaresConcat = new ArrayList<>(Arrays.asList((Integer[])squares.toArray())); // Arrays.ArrayList的add居然还有坑
        squaresConcat.addAll(Arrays.asList(36, 49, 64, 81, 100));
        System.out.println(squaresConcat);

        List<Integer> cubes = new ArrayList<>(Arrays.asList(1, 8, 27, 65, 125));
        System.out.println(cubes);
        cubes.set(3, 64);
        System.out.println(cubes);
        cubes.add(216);
        cubes.add((int)Math.pow(7, 3));
        System.out.println(cubes);

        List<Character> letters = new ArrayList<>(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f', 'g'));
        System.out.println(letters);

        // 官方的标准库不支持区域替换
         
        // Fibonacci 数列
        int a = 0, b = 1; 
        while (b < 1000) {
            System.out.print(b + ",");
            int c = a + b;
            a = b;
            b = c;
        }

        System.out.println();
    }
}
