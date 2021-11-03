// Quiz07
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
    int date;

    MonthSchedule(int num) {
        day = new Day[num];
        for (int i = 0; i < num; i++) {
            day[i] = new Day();
        }
    }

    void input() {
        System.out.print("what do you work for this day?");
        day[date].set(sc.next());
    }

    void view() {
        String result;
        if (day[date].get() == null) {
            result = "nothing";
        } else {
            result = day[date].get();
        }
        System.out.println("Day" + (date + 1) + " to do: " + result);
    }

    void finish() {
        System.out.println("Program closed");
        System.exit(0);
    }

    void run() {
        System.out.println("This month's schedule program");
        while (true) {
            System.out.print("What to do?(input: 1, view: 2, finish: 3)");
            int judge = sc.nextInt();
            if (judge == 3) {
                finish();
            } else {
                System.out.print("date(1~" + day.length + ")?");
                date = sc.nextInt() - 1;
                if (judge == 1) {
                    input();
                } else {
                    view();
                }
            }
        }
    }

    public static void main(String[] args) {
        MonthSchedule april = new MonthSchedule(30);
        april.run();
    }
}
