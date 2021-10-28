import java.util.Scanner;

class Exercise5_13 {
    public static void main(String[] args) {
        String[] words = { "television", "computer", "mouse", "phone" };
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < words.length; i++) {
            char[] question = words[i].toCharArray();
            for (int j = 0; j < question.length; j++) {
                int ran = (int) (Math.random() * question.length);
                char temp = question[j];
                question[j] = question[ran];
                question[ran] = temp;
            }
            System.out.printf("Q%d. %s's anwer>>", i + 1, new String(question));
            String answer = sc.nextLine();
            if (words[i].equals(answer.trim())) {
                System.out.println("correct!\n");
            } else {
                System.out.println("wrong!\n");
            }
        }
        sc.close();
    }
}
