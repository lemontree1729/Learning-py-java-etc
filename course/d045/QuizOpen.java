package d045;

import java.util.Scanner;

class QuizOpen {
    static Scanner sc = new Scanner(System.in);

    static String readString() {
        StringBuffer sb = new StringBuffer();
        while (true) {
            String temp = sc.nextLine();
            if (temp.equals(";"))
                break;
            sb.append(temp);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        char[] data = readString().toUpperCase().toCharArray();
        int[] cnt = new int[26];
        for (char letter : data) {
            int index = letter - 'A';
            if (0 <= index && index < 26)
                cnt[index]++;
        }
        for (int i = 0; i < cnt.length; i++) {
            System.out.print((char) ('A' + i));
            for (int j = 0; j < cnt[i]; j++)
                System.out.print("-");
            System.out.println();
        }
    }
}
