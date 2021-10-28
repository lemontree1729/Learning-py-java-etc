package d015;

import java.util.Random;

public class Quiz09 {
    public static void main(String[] args) {
        Random r = new Random();
        int[][] li = new int[4][4];
        for (int[] col : li) {
            for (int num : col) {
                num = r.nextInt(1, 11);
                System.out.print(num + "\t");
            }
            System.out.println();
        }
    }
}
