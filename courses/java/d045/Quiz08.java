package d045;

import java.util.Scanner;

class Quiz08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter any string");
        String text = sc.nextLine();
        for (int i = 1; i <= text.length(); i++)
            System.out.println(text.substring(i, text.length()) + text.substring(0, i));
        sc.close();
    }
}
