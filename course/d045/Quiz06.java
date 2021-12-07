package d045;

import java.util.Calendar;
import java.util.Scanner;

class TimeGuess {
    private long start, end;
    private Scanner sc = new Scanner(System.in);
    String name;

    TimeGuess() {
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print(name + " Start to Press <Enter>");
        sc.nextLine();
        start = getTime();
        System.out.println("    start time is " + (start % 60000) / 1000.0);
        System.out.print("Press <Enter> after 10 seconds");
        sc.nextLine();
        end = getTime();
        System.out.println("    end time is " + (end % 60000) / 1000.0);
    }

    private long getTime() {
        return Calendar.getInstance().getTimeInMillis();
    }

    double getResult() {
        return (end - start) / 1000.0;
    }
}

class Quiz06 {
    public static void main(String[] args) {
        TimeGuess people[] = new TimeGuess[3];
        for (int i = 0; i < people.length; i++)
            people[i] = new TimeGuess();
        System.out.print("result: ");
        int timer = 10, cnt = 0;
        double temp = Math.abs(timer - people[0].getResult());
        for (int i = 0; i < people.length; i++) {
            System.out.printf("[%s=%.3f]", people[i].name, people[i].getResult());
            if (Math.abs(people[i].getResult() - 10) < temp) {
                temp = Math.abs(people[i].getResult() - 10);
                cnt = i;
            }
        }
        System.out.println();
        System.out.println("winner is " + people[cnt].name + " with difference " + temp);
    }
}
