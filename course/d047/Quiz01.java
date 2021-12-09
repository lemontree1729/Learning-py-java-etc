package d047;

import java.util.Collections;
import java.util.Scanner;
import java.util.Vector;

class Quiz01 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var v = new Vector<Integer>();
        System.out.print("int(enter -1 to stop)>>");
        while (true) {
            var temp = sc.nextInt();
            if (temp == -1)
                break;
            v.add(temp);
        }
        Collections.sort(v);
        System.out.println("sorted vector: " + v);
        System.out.println("max number: " + Collections.max(v));
        sc.close();
    }
}
