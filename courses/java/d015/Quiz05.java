package d015;

import java.util.Scanner;

class Quiz05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter 10 positive integers>>");
        int[] num = new int[10];
        for (int i = 0; i < 10; i++) {
            num[i] = sc.nextInt();
        }
        System.out.print("multiples of 3 are ");
        for (int j : num) {
            if (j % 3 == 0) {
                System.out.print(j + " ");
            }
        }
        sc.close();
    }
}
