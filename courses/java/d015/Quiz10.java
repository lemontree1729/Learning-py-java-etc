package d015;

import java.util.Random;

class Quiz10 {
    public static void main(String[] args) {
        Random r = new Random();
        int[][] li = new int[4][4];
        int col, row, cnt = 0;
        while (cnt < 10) {
            col = r.nextInt(4);
            row = r.nextInt(4);
            if (li[row][col] == 0) {
                li[row][col] = r.nextInt(1, 11);
                cnt++;
            }
        }
        for (int[] cols : li) {
            for (int num : cols) {
                System.out.print(num + "\t");
            }
            System.out.println();
        }
    }
}
