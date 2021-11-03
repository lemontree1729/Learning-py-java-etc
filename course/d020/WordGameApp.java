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
        String a = sc.next(); // error accurs here on VS code. guess it is because of encoding problem but
                              // eclipse works fine
        System.out.println(a);
        return a;
    }

    static boolean checkSuccess(String firstWord, String lastWord) {
        char lastChar = firstWord.charAt(firstWord.length() - 1);
        char firstChar = lastWord.charAt(0);

        for (char a : firstWord.toCharArray()) {
            System.out.println((Character.toString(a)));
            System.out.println((int) a);
        }
        System.out.println("and");
        for (char a : lastWord.toCharArray()) {
            System.out.println((Character.toString(a)));
            System.out.println((int) a);
        }
        if (lastChar == firstChar) {
            return true;
        }
        System.out.print("Continue the game?(Y/N)");
        String yorn = sc.next();
        if (yorn.charAt(0) == 'Y') {
            return true;
        }
        return false;
    }
}

class WordGameApp {
    static int playerNum;

    WordGameApp() {
        System.out.println("starting word relay game!");
        System.out.print("enter the number of player>>");
        Scanner sc = new Scanner(System.in);
        playerNum = sc.nextInt();
    }

    static void run() {
        Player[] player = new Player[playerNum];
        for (int i = 0; i < playerNum; i++) {
            player[i] = new Player();
        }
        System.out.println("Starting word is 아버지");
        String first = "아버지";
        int cnt = 0;
        while (true) {
            cnt = (cnt + 1) % playerNum;
            String last = player[cnt].getWordFromUser();
            System.out.println(last);
            if (!Player.checkSuccess(first, last)) {
                break;
            }
            first = last;
        }
    }

    public static void main(String[] args) {
        WordGameApp hello = new WordGameApp();
        hello.run();
    }
}
