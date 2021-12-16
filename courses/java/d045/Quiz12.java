package d045;

import java.util.Scanner;

class Person {
    String name;
    Scanner sc = new Scanner(System.in);

    Person(String name) {
        this.name = name;
    }

    boolean getResult() {
        System.out.print("[" + name + "]:<Enter>");
        sc.nextLine();
        int num[] = new int[3];
        System.out.print("  ");
        for (int i = 0; i < num.length; i++) {
            num[i] = (int) (Math.random() * 3);
            System.out.print("  " + num[i]);
        }
        for (int i = 0; i < num.length; i++) {
            if (i > 0 && num[i - 1] != num[i])
                return false;
        }
        return true;
    }
}

class Quiz12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("number of people joining gamble game>>");
        Person[] players = new Person[sc.nextInt()];
        for (int i = 0; i < players.length; i++) {
            System.out.print("person" + (i + 1) + " name>>");
            players[i] = new Person(sc.nextLine());
        }
        boolean flow = true;
        while (flow) {
            for (Person player : players) {
                if (player.getResult()) {
                    System.out.println("    " + player.name + " wins!");
                    flow = false;
                    break;
                } else
                    System.out.println("    that was close!");
            }
        }
        sc.close();
    }
}
