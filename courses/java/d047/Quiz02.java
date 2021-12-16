package d047;

import java.util.ArrayList;
import java.util.Scanner;

class Quiz02 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var li = new ArrayList<Character>();
        System.out.print("Enter 6 degrees(A/B/C/D/F possible)>>");
        while (li.size() < 6)
            sc.next().chars().forEach(i -> li.add((char) i));
        System.out.println(li.stream().mapToDouble(i -> Math.max('E' - i, 0)).average().getAsDouble());
        sc.close();
    }
}
