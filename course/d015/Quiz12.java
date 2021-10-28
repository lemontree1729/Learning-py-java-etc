package d015;

public class Quiz12 {
    public static void main(String[] args) {
        int sum = 0;
        for (String arg : args) {
            try {
                sum += Integer.parseInt(arg);
            } catch (NumberFormatException e) {
            }
        }
        System.out.println(sum);
    }

}
