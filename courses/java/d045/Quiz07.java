package d045;

import java.util.Scanner;
import java.util.StringTokenizer;

class WordWithSplit {
    Scanner sc = new Scanner(System.in);

    WordWithSplit() {
        while (true) {
            String text = sc.nextLine();
            if (text.equals("stop"))
                break;
            System.out.println(text.split(" ").length + " words");
        }
    }
}

class WordWithStringTokenizer {
    Scanner sc = new Scanner(System.in);

    WordWithStringTokenizer() {
        while (true) {
            String text = sc.nextLine();
            if (text.equals("stop"))
                break;
            StringTokenizer textToken = new StringTokenizer(text, " ");
            System.out.println(textToken.countTokens() + " words");
        }
    }
}

class Quiz07 {
    public static void main(String[] args) {
        WordWithSplit a = new WordWithSplit();
        WordWithStringTokenizer b = new WordWithStringTokenizer();
        System.out.println(a + " " + b);
    }
}
