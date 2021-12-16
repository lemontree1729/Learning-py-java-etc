package d020;

import java.util.Scanner;

class Grade {
    int math, science, english;

    Grade(int math, int science, int english) {
        this.math = math;
        this.science = science;
        this.english = english;
    }

    int average() {
        return (math + science + english) / 3;
    }
}

class Quiz02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("enter math, science, english score each>>");
        int math = sc.nextInt();
        int science = sc.nextInt();
        int english = sc.nextInt();
        Grade me = new Grade(math, science, english);
        System.out.println("average is>>" + me.average());

        sc.close();
    }
}
