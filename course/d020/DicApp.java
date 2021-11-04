// Quiz10
package d020;

import java.util.Scanner;

class Dictionary {
    private static String[] kor = { "sarang", "agi", "don", "mirae", "huimang" };
    private static String[] eng = { "love", "baby", "money", "future", "hope" };

    static String kor2Eng(String word) {
        for (int i = 0; i < kor.length; i++) {
            if (word.equals(kor[i])) {
                return eng[i];
            }
        }
        return "";
    }
}

class DicApp {
    static Scanner sc = new Scanner(System.in);

    static void search() {
        System.out.print("kor word?");
        String word = sc.next();
        String result = Dictionary.kor2Eng(word);
        if (word.equals("stop")) {
            System.exit(0);
        }
        if (result.equals("")) {
            System.out.println(word + " is not in my dictionary");
        } else {
            System.out.println(word + " is " + result);
        }
    }

    public static void main(String[] args) {
        System.out.println("kor to eng program");

        while (true) {
            search();
        }
    }
}
