package d047;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class QuizOpen {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var dict = new HashMap<String, String>();
        dict.put("painting", "mural");
        dict.put("eye", "oculus");
        dict.put("society", "association");
        dict.put("old", "decrepit");
        dict.put("hard", "ardouus");
        dict.put("spend", "allocate");
        dict.put("hire", "appoint");
        dict.put("exist", "prevail");
        dict.put("orbit", "trajectory");
        dict.put("dictionary", "glossary");
        dict.put("make", "manufacture");
        dict.put("delete", "annul");
        dict.put("touch", "caress");
        var gameflow = true;

        System.out.println("** this is english synonym test program **");
        while (gameflow) {
            System.out.print("test(1), insert(2), exit(3)>>");
            switch (Integer.parseInt(sc.nextLine())) {
                case 1:
                    System.out.println("enter -1 if you want to exit...");
                    System.out.println(dict.size() + " number of words exist");
                    var iter = dict.keySet().iterator();
                    while (true) {
                        var example = new ArrayList<String>();
                        while (example.size() < 4) {
                            if (!iter.hasNext())
                                iter = dict.keySet().iterator();
                            example.add(iter.next());
                        }
                        var answer = (int) (Math.random() * 4 + 1);
                        System.out.println(example.get(answer - 1) + "?");
                        for (int i = 0; i < example.size(); i++)
                            System.out.printf("(%d)%s ", i + 1, dict.get(example.get(i)));
                        System.out.print(">>");
                        int input;
                        try {
                            input = Integer.parseInt(sc.nextLine());
                        } catch (NumberFormatException e) {
                            System.out.println("wrong input!");
                            continue;
                        }
                        if (input == -1)
                            break;
                        if (input == answer)
                            System.out.println("correct!");
                        else
                            System.out.println("wrong!");
                    }
                    System.out.println();
                    break;
                case 2:
                    System.out.println("enter stop to stop insert...");
                    while (true) {
                        System.out.print("enter 2 english synonyms>>");
                        var input = sc.nextLine().split(" ");
                        if (input.length == 1 && input[0].equals("stop"))
                            break;
                        dict.put(input[0], input[1]);
                    }
                    break;
                case 3:
                    System.out.println("program cloesd");
                    gameflow = false;
                    break;
            }
        }
        sc.close();
    }
}
