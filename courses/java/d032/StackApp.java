package d032;

import java.util.Scanner;

interface Stack {
    int length();

    int capacity();

    String pop();

    boolean push(String str);
}

public class StackApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("total stack capacity>> ");
        int n = sc.nextInt();
        StringStack ss = new StringStack(n);
        while (true) {
            System.out.print("enter string>>");
            String st = sc.next();
            if (st.equals("stop")) {
                break;
            }
            boolean result = ss.push(st);
            if (!result) {
                System.out.println("stack fulled");
            }
        }

        System.out.println("pop all strings in stack>>");
        int len = ss.length();
        for (int i = 0; i < len; i++) {
            System.out.println(ss.pop());
        }
        sc.close();
    }
}
