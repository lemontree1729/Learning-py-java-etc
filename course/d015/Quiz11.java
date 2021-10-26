package d015;

public class Quiz11 {
    public static void main(String[] args) {
        int sum = 0;
        for (String arg : args) {
            sum += Integer.parseInt(arg);
        }
        System.out.println((double) sum / args.length);
    }
}
