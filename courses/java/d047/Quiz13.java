package d047;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class Quiz13 {
    static ArrayList<String> turing = new ArrayList<String>();
    static HashMap<String, Integer> data = new HashMap<String, Integer>();

    public static int parse(String input) {
        if (data.containsKey(input))
            return data.get(input);
        return Integer.parseInt(input);
    }

    public static void run(String command) {
        var seq = command.split(" ");
        if (seq[0].equals("mov"))
            data.put(seq[1], parse(seq[2]));
        else if (seq[0].equals("add"))
            data.put(seq[1], parse(seq[1]) + parse(seq[2]));
        else if (seq[0].equals("sub"))
            data.put(seq[1], parse(seq[1]) - parse(seq[2]));
        else if (seq[0].equals("jn0")) {
            if (data.get(seq[1]) != 0) {
                for (int i = parse(seq[2]); i < turing.size(); i++)
                    run(turing.get(i));
            }
        } else if (seq[0].equals("res")) {
            System.out.println("[program reset]");
            reset();
        }
    }

    public static void showData() {
        data.forEach((str, num) -> System.out.printf("%S:%d  ", str, num));
        System.out.println();
    }

    public static void reset() {
        turing.clear();
        data.clear();
    }

    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        System.out.println("[Basic turing machine]");
        while (true) {
            System.out.print(">> ");
            var command = sc.nextLine();
            if (command.equals("end")) {
                System.out.println("[program ended]");
                break;
            }
            turing.add(command);
            run(command);
            showData();
        }
        sc.close();
    }
}
