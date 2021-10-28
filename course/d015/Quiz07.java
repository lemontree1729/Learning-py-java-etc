package d015;

import java.lang.Math;

public class Quiz07 {
    public static void main(String[] args) {
        int ran, sum = 0;
        System.out.print("random numbers : ");
        for (int i = 0; i < 10; i++) {
            ran = (int) (Math.random() * 10 + 1);
            System.out.print(ran + " ");
            sum += ran;
        }
        System.out.println("\naverage : " + sum / 10.0);
    }
}
