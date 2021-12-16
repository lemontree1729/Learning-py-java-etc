package d047;

import java.util.HashMap;
import java.util.Scanner;

class Quiz07 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new HashMap<String, Float>();
        System.out.println("starting system.....");
        for (int i = 0; i < 5; i++) {
            System.out.print("enter name and GPA>>");
            var input = sc.nextLine().split(" ");
            data.put(input[0], Float.parseFloat(input[1]));
        }
        System.out.print("enter GPA to earn scolarship>>");
        var standard = sc.nextFloat();
        System.out.print("scolarship students: ");
        data.forEach((name, GPA) -> {
            if (GPA > standard)
                System.out.print(name + " ");
        });
        sc.close();
    }
}
