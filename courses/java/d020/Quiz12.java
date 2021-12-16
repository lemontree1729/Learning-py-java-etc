package d020;

import java.util.Scanner;

class Seat {
    String seatname;
    String[] stat;

    Seat(int n, String seatname) {
        this.seatname = seatname;
        stat = new String[n];
        for (int i = 0; i < n; i++) {
            stat[i] = "---";
        }
    }

    void set(int n, String name) {
        stat[n] = name;
    }

    void show() {
        System.out.print(seatname + ">>");
        for (String name : stat)
            System.out.print(" " + name);
        System.out.println();
    }
}

class SeatSystem {
    Scanner sc = new Scanner(System.in);
    Seat[] totalseat = new Seat[3];

    SeatSystem() {
        System.out.println("system start");
        totalseat[0] = new Seat(10, "S");
        totalseat[1] = new Seat(10, "A");
        totalseat[2] = new Seat(10, "B");
        run();
    }

    void run() {
        while (true) {
            System.out.print("reservation:1, search:2, cancel:3, end:4>>");
            int menunum = sc.nextInt();
            switch (menunum) {
            case 1:
                reserv();
                break;
            case 2:
                search();
                break;
            case 3:
                cancel();
                break;
            case 4:
                end();
                break;
            }
        }
    }

    void reserv() {
        System.out.print("select seat column S(1), A(2), B(3)>>");
        int seatcol = sc.nextInt() - 1;
        totalseat[seatcol].show();
        System.out.print("name>>");
        String name = sc.next();
        System.out.print("num>>");
        int num = sc.nextInt();
        totalseat[seatcol].set(num, name);
    }

    void search() {
        for (Seat seat : totalseat) {
            seat.show();
        }
        System.out.println("<<search ended>>");
    }

    void cancel() {
        System.out.print("select seat column S(1), A(2), B(3)>>");
        int seatcol = sc.nextInt() - 1;
        Seat target = totalseat[seatcol];
        target.show();
        System.out.print("name>>");
        String name = sc.next();
        for (int i = 0; i < 10; i++) {
            if (name.equals(target.stat[i])) {
                target.set(i, "---");
                break;
            }
        }
    }

    void end() {
        System.out.println("<<end the program>>");
        System.exit(0);
    }
}

class Quiz12 {
    public static void main(String[] args) {
        new SeatSystem();
    }
}
