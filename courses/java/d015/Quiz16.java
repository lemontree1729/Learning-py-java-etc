package d015;

import java.util.Scanner;
import java.lang.Math;

class Quiz16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = { "rock", "scissors", "paper" };
        String user;
        int comp;
        System.out.println("Starting rock scissors paper game!");
        while (true) {
            System.out.print("rock scissors paper!>>");
            user = sc.next();
            comp = (int) (Math.random() * 3);
            if (user.equals("stop")) {
                System.out.println("Game stopped");
                break;
            } else {
                System.out.print("user: " + user + ", computer: " + str[comp] + ", ");
                if (user.equals(str[comp])) {
                    System.out.println("you draws!");
                } else if (user.equals(str[(comp + 1) % 3])) {
                    System.out.println("you lose!");
                } else if (user.equals(str[(comp + 2) % 3])) {
                    System.out.println("you wins!");
                } else {
                    System.out.println("wrong input!");
                }
            }
        }
        sc.close();
    }
}
