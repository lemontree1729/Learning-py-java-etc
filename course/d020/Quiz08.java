package d020;

import java.util.Scanner;

class PhoneBook {
    String name, tel;

    PhoneBook(String name, String tel) {
        this.name = name;
        this.tel = tel;
    }
}

class Quiz08 {
    static PhoneBook[] my;

    static void getPhoneNumber(String name) {
        if (my == null) {
            System.out.println(name + " is not in list");
        } else {
            if (name.equals("stop")) {
                System.exit(0);
            }
            boolean chk = true;
            for (PhoneBook book : my) {
                if (book.name.equals(name)) {
                    System.out.println(name + "'s phone number is " + book.tel);
                    chk = false;
                    break;
                }
            }
            if (chk) {
                System.out.println(name + " is not in list");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of people>>");
        my = new PhoneBook[sc.nextInt()];
        for (int i = 0; i < my.length; i++) {
            System.out.print("Name and Phone number>>");
            my[i] = new PhoneBook(sc.next(), sc.next());
        }
        while (true) {
            System.out.print("name for search>>");
            getPhoneNumber(sc.next());
        }
    }
}
