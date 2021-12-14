package d050;

import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

class QuizOpen {
    public static void main(String[] args) {
        var fpath = "c:/temp/SATwords.txt";
        var data = new HashMap<String, String>();
        Scanner sc = null;
        try {
            sc = new Scanner(new FileReader(fpath));
        } catch (IOException e) {
            e.printStackTrace();
        }
        while (sc.hasNextLine()) {
            var temp = sc.nextLine();
            if (temp.contains("#"))
                continue;
            data.put(temp, sc.nextLine());
        }
        System.out.println("starting hangman game with 300 SAT words");
        var keys = data.keySet().toArray(new String[data.size()]);
        sc = new Scanner(System.in);
        while (true) {
            int cnt = 10;
            var origin = keys[(int) (Math.random() * keys.length)];
            var beep = new StringBuilder();
            for (int i = 0; i < origin.length(); i++)
                beep.append("-");
            while (cnt-- > 0) {
                System.out.print(beep + "\n>>");
                var input = sc.nextLine().charAt(0);
                for (int i = 0; i < origin.length(); i++) {
                    if (input == origin.charAt(i))
                        beep.setCharAt(i, input);
                }
                System.out.println(cnt + " chances left");
            }
            if (origin.equals(beep.toString()))
                System.out.println("you win!");
            else
                System.out.println("you lose!");
            System.out.printf("Answer was %s(%s)\n", origin, data.get(origin));
            System.out.println("Again(y/n)?");
            if (sc.nextLine().equals("n"))
                break;
        }
        sc.close();
    }
}
