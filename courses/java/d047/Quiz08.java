package d047;

import java.util.HashMap;
import java.util.Scanner;

class Quiz08 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new HashMap<String, Integer>();
        System.out.println("** This is Point management program **");
        while (true) {
            System.out.print("enter name and point>>");
            var input = sc.nextLine().split(" ");
            if (input.length == 1 && input[0].equals("stop"))
                break;
            if (data.containsKey(input[0]))
                data.put(input[0], data.get(input[0]) + Integer.parseInt(input[1]));
            else
                data.put(input[0], Integer.parseInt(input[1]));
            data.forEach((name, point) -> System.out.printf("(%s,%d)", name, point));
            System.out.println();
        }
        sc.close();
    }
}
