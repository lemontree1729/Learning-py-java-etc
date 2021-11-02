package d020;

import java.util.Scanner;

class Player {
    String name;
    static Scanner sc = new Scanner(System.in);

    Player() {
        System.out.print("enter the players name>>");
        Scanner hello = new Scanner(System.in);
        name = sc.next();
    }

    String getWordFromUser() {
        System.out.print(name + ">>");
        return sc.next();
    }

    static boolean checkSuccess(String firstWord, String lastWord) {
        char lastChar = firstWord.charAt(firstWord.length() - 1);
        char firstChar = lastWord.charAt(0);
        System.out.println(firstChar);
        System.out.println((int) firstChar);
        System.out.println(lastChar);
        System.out.println((int) lastChar);
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
