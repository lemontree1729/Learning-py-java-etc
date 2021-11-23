package d035.myMMS;

import java.util.Scanner;

class MMSAction {
    static int checkInt(Scanner sc) {
        Integer next = MMSControl.parseInt(sc.next());
        int cnt = 0;
        while (next == null) {
            if (cnt < 3)
                System.out.print("you should enter int: ");
            else
                System.out.print("INPUT--->!!INT!!<---: ");
            next = MMSControl.parseInt(sc.next());
            cnt++;
        }
        return next;
    }

    static void register() {

    }

    static void show() {

    }

    static void update() {

    }

    static void delete() {

    }

    static void search() {

    }
}
