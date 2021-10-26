package d015;

import java.util.Scanner;

public class Quiz14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String course[] = { "Java", "C++", "HTML5", "ComputerStructure", "Android" };
        int score[] = { 95, 88, 76, 62, 55 };
        boolean notPrinted;
        String name;
        while (true) {
            System.out.print("course name>>");
            notPrinted = true;
            name = sc.next();
            for (int i = 0; i < course.length; i++) {
                if (name.equals(course[i])) {
                    System.out.println(name + "'s score is " + score[i]);
                    notPrinted = false;
                    break;
                }
            }
            if (name.equals("stop")) {
                break;
            } else if (notPrinted) {
                System.out.println("not existed course");
            }
        }
        sc.close();
    }
}
