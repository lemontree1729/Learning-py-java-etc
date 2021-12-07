package d045;

import java.util.Scanner;

class Quiz09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String data[] = { "rock", "scissors", "paper" };
        int bob, computer;
        while (true) {
            System.out.print("bob[rock(1), scissors(2), paper(3), exit(4)]>>");
            bob = sc.nextInt();
            if (bob == 4)
                break;
            computer = (int) (Math.random() * 3);
            System.out.printf("bob(%s) : computer(%s)\n", data[bob], data[computer]);
            if (bob == computer)
                System.out.println("you draw");
            else if ((bob - computer + 3) % 3 == 2)
                System.out.println("you win!");
            else
                System.out.println("you lose!");
        }
        sc.close();
    }
}
