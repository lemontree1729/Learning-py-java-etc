package d015;

import java.util.Scanner;

class Quiz04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter any lower alphabet>>");
        String s = sc.next();
        char c = s.charAt(0);
        for (int i = (int) (c - 'a'); i >= 0; i--) {
            for (int j = i; j >= 0; j--) {
                System.out.print((char) (c - j));
            }
            System.out.println();
        }
        sc.close();
    }
}
