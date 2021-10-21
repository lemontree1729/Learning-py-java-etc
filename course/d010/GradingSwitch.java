import java.util.Scanner;

public class GradingSwitch {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter your score(0~100) : ");
        int score = sc.nextInt();
        char grade = ' ';
        if (score > 100 || score < 0) {
            System.out.println("Wrong score");
        } else {
            switch (score / 10) {
            case 10:
            case 9:
                grade = 'A';
            case 8:
                grade = 'B';
            default:
                grade = 'F';
            }
            System.out.println("your score is " + grade);
        }
        sc.close();
    }
}
