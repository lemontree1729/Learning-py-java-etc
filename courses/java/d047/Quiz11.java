package d047;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class Nation {
    String country, capital;

    Nation(String country, String capital) {
        this.country = country;
        this.capital = capital;
    }

    boolean contains(String capital) {
        if (this.capital.equals(capital))
            return true;
        return false;
    }

    public String getCountry() {
        return country;
    }
}

class Quiz11 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new ArrayList<Nation>();
        System.out.println("**** game start ****");
        var gameflow = true;
        while (gameflow) {
            System.out.print("input(1), quiz(2), exit(3)>>");
            switch (Integer.parseInt(sc.nextLine())) {
                case 1:
                    System.out.println(data.size() + " input exist");
                    while (true) {
                        System.out.print("enter country and capital" + (data.size() + 1) + ">>");
                        var temp = sc.nextLine().split(" ");
                        if (temp.length == 1 && temp[0].equals("stop"))
                            break;
                        for (var nation : data) {
                            if (nation.contains(temp[0])) {
                                System.out.println("nation already exist");
                                continue;
                            }
                        }
                        data.add(new Nation(temp[0], temp[1]));
                    }
                    break;
                case 2:
                    while (true) {
                        int ran = (int) (Math.random() * data.size());
                        System.out.print(data.get(ran).getCountry() + "'s capital?");
                        var answer = sc.nextLine();
                        if (answer.equals("stop"))
                            break;
                        if (data.get(ran).contains(answer))
                            System.out.println("correct!");
                        else
                            System.out.println("wrong!");
                    }
                    break;
                case 3:
                    System.out.println("exit the game");
                    gameflow = false;
                    break;
            }
        }
        gameflow = true;
        var newdata = new HashMap<String, String>();
        System.out.println("**** game start ****");
        System.out.print("input(1), quiz(2), exit(3)>>");
        while (gameflow) {
            switch (Integer.parseInt(sc.nextLine())) {
                case 1:
                    System.out.println(newdata.size() + " input exist");
                    while (true) {
                        System.out.print("enter country and capital" + (newdata.size() + 1));
                        var temp = sc.nextLine().split(" ");
                        if (temp.length == 1 && temp[0].equals("stop"))
                            break;
                        if (newdata.containsKey(temp[0])) {
                            System.out.println("nation already exist");
                            continue;
                        }
                        newdata.put(temp[0], temp[1]);
                    }
                    break;
                case 2:
                    while (true) {
                        var iter = newdata.keySet().iterator();
                        while (iter.hasNext()) {
                            var next = iter.next();
                            System.out.print(next + "'s capital?");
                            var answer = sc.nextLine();
                            if (answer.equals("stop"))
                                break;
                            if (newdata.get(next).equals(answer))
                                System.out.println("correct!");
                            else
                                System.out.println("wrong!");
                        }
                        if (iter.hasNext())
                            break;
                    }
                    break;
                case 3:
                    System.out.println("exit the game");
                    gameflow = false;
                    break;
            }
        }

        sc.close();
    }
}
