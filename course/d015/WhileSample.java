package d015;

import java.util.Scanner;

class WhileSample {
    public static void main(String[] args) {
        int count = 0;
        int sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("enter ints with end sign -1");
        int n = sc.nextInt();
        while (n != -1) {
            sum += n;
            count++;
            n = sc.nextInt();
        }
        if (count == 0) {
            System.out.println("Error: no number input");
        } else {
            System.out.print("number of int is " + count);
            System.out.println("average is " + (double) sum / count);
        }
        sc.close();
    }
}
