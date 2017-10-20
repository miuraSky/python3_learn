import java.util.LinkedList;
import java.util.Arrays;

public class For {
    
    public static void main(String[] args) {
        // Measure some strings
        String[] words = new String[] {"cat", "window", "defenstrate"}; 

        for (String s : words) {
            System.out.println(s + " " + s.length());
        }

        /* 1. Iterator接口支持List循环的时候remove, 但没有add
         * 2. 为了Insert还要用LinkedList
         * 3. 还要注意浅copy引起的问题
         */
        LinkedList<String> wordsList = new LinkedList<String>(Arrays.asList(words));
        for (String s : words) {
            if (s.length() > 6) {
                wordsList.add(0, "Java的这种操作太难了 @@");
            }
        }

        // java的数组不能改变,只能new新的
        words = new String[wordsList.size()];
        // LinkedList.toArray()返回的是Object[], 不能强转成String[]
        wordsList.toArray(words);
        
        System.out.println(Arrays.asList(words));

    }

}
