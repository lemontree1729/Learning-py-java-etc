package d015;

import java.util.Scanner;
import java.util.Random;

public class Quiz08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("number of int : ");
        Random r = new Random();
        int rannum;
        int n = sc.nextInt();
        int[] li = new int[n];
        while (li[n - 1] == 0) {
            rannum = r.nextInt(1, 101);
            for (int i = 0; i < n; i++) {
                if (rannum == li[i]) {
                    break;
                } else if (li[i] == 0) {
                    li[i] = rannum;
                    break;
                }
            }
        }
        for (int j : li) {
            System.out.print(j + " ");
        }
        sc.close();
    }
}
