package d045;

import java.util.Scanner;

class Quiz11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter text>>");
        StringBuffer text = new StringBuffer(sc.nextLine());
        while (true) {
            System.out.print("command>>");
            String[] command = sc.nextLine().split("!", -1);
            if (command.length == 1 && command[0].equals("stop")) {
                System.out.println("stop program");
                break;
            }
            int index = text.indexOf(command[0]);
            if (command.length != 2 || command[0].equals(""))
                System.out.println("wrong command!");
            else if (index == -1)
                System.out.println("cannot find!");
            else {
                text.replace(index, index + command[0].length(), command[1]);
                System.out.println(text);
            }
        }
        sc.close();
    }
}
