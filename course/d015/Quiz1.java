package d015;

public class Quiz1 {
    public static void whileTest(int n) {
        int sum = 0, i = 0;
        while (i < 100) {
            sum += i;
            i += 2;
        }
        System.out.println(sum);
    }

    public static void forTest(int n) {
        int sum = 0;
        for (int i = 0; i < 100; i += 2) {
            sum += i;
        }
        System.out.println(sum);

    }

    public static void doWhileTest(int n) {
        int sum = 0, i = 0;
        do {
            sum += i;
            i += 2;
        } while (i < 100);
        System.out.println(sum);

    }

    public static void main(String[] args) {
        int n = 100;
        whileTest(n);
        forTest(n);
        doWhileTest(n);
    }
}
