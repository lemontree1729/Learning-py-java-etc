package d047;

import java.util.ArrayList;
import java.util.Scanner;

class Quiz04 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new ArrayList<Integer>();
        while (true) {
            System.out.print("enter precipitation(0 stops program)>>");
            data.add(sc.nextInt());
            if (data.get(data.size() - 1) == 0)
                break;
            data.forEach(i -> System.out.print(i + " "));
            System.out.println();
            System.out.println("average is: " + data.stream().mapToInt(Integer::intValue).average().getAsDouble());
        }
        sc.close();
    }
}
