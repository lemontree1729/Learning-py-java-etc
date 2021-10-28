package d015;

import java.util.Scanner;

public class Quiz06 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] units = { 50000, 10000, 1000, 500, 100, 50, 10, 1 };
        System.out.print("Enter the price>>");
        int price = sc.nextInt();
        for (int unit : units) {
            System.out.println(unit + " : " + price / unit);
            price %= unit;
        }
        sc.close();
    }
}
