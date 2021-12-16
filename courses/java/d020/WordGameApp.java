// chapter 4 open challenge quiz
package d020;

import java.util.Scanner;

class Player {
    String name;
    static Scanner sc = new Scanner(System.in);

    Player() {
        System.out.print("enter the players name>>");
        name = sc.next();
    }

    String getWordFromUser() {
        System.out.print(name + ">>");
        return sc.next(); // error accurs here on VS code.
        // guess there is some encoding problem but eclipse works fine
    }

    static boolean checkSuccess(String first, String last) {
        if (first.charAt(first.length() - 1) == last.charAt(0)) {
            return true;
        }
        System.out.print("Continue the game?(Y/N)");
        if (sc.next().equals("Y")) {
            return true;
        }
        return false;
    }
}

class WordGameApp {
    int playerNum;
    Scanner sc = new Scanner(System.in);

    WordGameApp() {
        System.out.println("starting word relay game!");
        System.out.print("enter the number of player>>");
        playerNum = sc.nextInt();
    }

    void run() {
        Player[] player = new Player[playerNum];
        for (int i = 0; i < playerNum; i++) {
            player[i] = new Player();
        }
        System.out.println("Starting word is father");
        String first = "father";
        int cnt = 0;
        while (true) {
            cnt = (cnt + 1) % playerNum;
            String last = player[cnt].getWordFromUser();
            if (!Player.checkSuccess(first, last)) {
                break;
            }
            first = last;
        }
        sc.close();
    }

    public static void main(String[] args) {
        WordGameApp hello = new WordGameApp();
        hello.run();
    }
}
