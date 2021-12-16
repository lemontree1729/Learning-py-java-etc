package d047;

import java.util.HashMap;
import java.util.Scanner;

class Quiz03 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var nations = new HashMap<String, Integer>();
        System.out.println("enter country and population.(example: Korea 5000");
        while (true) {
            System.out.print("country, population>>");
            var temp = sc.nextLine().split(" ");
            if (temp.length == 1 && temp[0].equals("stop"))
                break;
            if (temp.length == 2)
                nations.put(temp[0], Integer.valueOf(temp[1]));
        }
        while (true) {
            System.out.print("enter country to search population>>");
            var temp = sc.next();
            if (temp.equals("stop"))
                break;
            if (!nations.containsKey(temp))
                System.out.println("there is no " + temp + " in dictionary");
            else
                System.out.println("population of " + temp + " is " + nations.get(temp));
        }
        sc.close();
    }
}
