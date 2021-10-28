package d015;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Quiz15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        System.out.print("enter two numbers>>");
        try {
            a = sc.nextInt();
            b = sc.nextInt();
            System.out.println(a + "x" + b + "=" + a * b);
        } catch (InputMismatchException e) {
            System.out.println("you entered wrong input!");
            sc.nextLine();
        }
        sc.close();
    }
}
