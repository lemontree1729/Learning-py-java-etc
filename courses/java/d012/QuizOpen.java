package d012;

import java.util.Scanner;

class QuizOpen {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1, n2, cnt;
        String per1, per2;
        String[] rpscase = {"rock", "paper", "scissors"};
        while (true) {
            System.out.print("first person : ");
            per1 = sc.next();
            System.out.print("second person : ");
            per2 = sc.next();
            n1 = 3;
            n2 = 0;
            cnt = 0;
            for (String rps : rpscase) {
                if (per1.equals(rps)) {
                    n1 = cnt;
                }
                if (per2.equals(rps)) {
                    n2 = cnt;
                }
                cnt++;
            }
            if (n1 == n2) {
                System.out.println("draw!");
            } else if (n1 == (n2 + 1) % 3) {
                System.out.println("first person wins!");
            } else if (n1 == (n2 - 1) % 3) {
                System.out.println("second person wins!");
            } else {
                System.out.println("program closed");
                break;
            }
        }
        sc.close();
    }
}