package d012;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Quiz04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("ENTER ANYTHING WRONG TO QUIT!");
        int a, b, c, a1, b1, c1, middle1, first, middle2;
        while (true) {
            try {
                System.out.print("enter the three numbers : ");
                a = sc.nextInt();
                b = sc.nextInt();
                c = sc.nextInt();
                // case 1
                a1 = a > b ? a : b;
                b1 = b > c ? b : c;
                c1 = c > a ? c : a;
                if (a1 > b1) {
                    middle1 = b1;
                } else if (a1 < b1) {
                    middle1 = a1;
                } else {
                    middle1 = c1;
                }
                System.out.println("your middle number is : " + middle1);
                // case 2
                first = a > b ? a : b;
                middle2 = c > first ? first : (first == a ? (c > b ? c : b) : (c > a ? c : a));
                System.out.println("your middle number is : " + middle2);
            } catch (InputMismatchException ime) {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}
