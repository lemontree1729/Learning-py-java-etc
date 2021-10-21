public class Hello {

    public static int sum(int n, int m) {
        return n + m;
    }

    public static void main(String[] args) {
        int i = 20;
        int s = sum(i, 10);
        char a = '?';
        System.out.printf("%s%n%s%n%d%n", a, "Hello", s);
    }
}
