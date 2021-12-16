package d015;

import java.util.Scanner;

class Quiz03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter the number>>");
        int star = sc.nextInt();
        for (int i = star; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        sc.close();
    }
}
