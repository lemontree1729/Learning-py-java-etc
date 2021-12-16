package d015;

import java.util.Random;
import java.util.Scanner;

class QuizOpen {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        int ans, k, start, end, cnt;
        String yorn;
        while (true) {
            k = r.nextInt(100);
            start = 0;
            end = 99;
            cnt = 1;
            System.out.println("Game starts!");
            while (true) {
                System.out.println(start + "~" + end);
                System.out.print(cnt + ">>");
                ans = sc.nextInt();
                if (k > ans) {
                    System.out.println("Higher!");
                    start = ans;
                } else if (k < ans) {
                    System.out.println("Lower!");
                    end = ans;
                } else {
                    System.out.println("Correct!");
                    break;
                }
                cnt++;
            }
            System.out.print("Restart?(Y/N)>>");
            yorn = sc.next();
            if (yorn.equals("N")) {
                break;
            }
        }
        sc.close();
    }
}
