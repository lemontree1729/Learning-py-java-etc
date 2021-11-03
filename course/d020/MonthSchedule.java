package d020;

import java.util.Scanner;

class Day {
    private String work;

    public void set(String work) {
        this.work = work;
    }

    public String get() {
        return work;
    }

    public void show() {
        if (work == null)
            System.out.println("nothing");
        else
            System.out.println(work + " to do");
    }
}

class MonthSchedule {
    static Scanner sc = new Scanner(System.in);
    Day[] day;

    void input() {
        System.out.print("what to do?");
        sc.next();
    }

    public static void main(String[] args) {
        System.out.println("This month's schedule program");

    }
}
