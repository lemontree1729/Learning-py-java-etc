package d050;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

class Quiz10 {
    public static void main(String[] args) {
        var data = new File("c:\\temp\\phone.txt");
        var dict = new HashMap<String, String>();
        Scanner sc;
        try {
            sc = new Scanner(data);
            while (sc.hasNextLine()) {
                var temp = sc.nextLine().split(" ");
                dict.put(temp[0], temp[1]);
            }
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(dict.size() + " phone number added");
        sc = new Scanner(System.in);
        while (true) {
            System.out.print("name>>");
            var name = sc.nextLine();
            if (name.equals("stop"))
                break;
            if (dict.containsKey(name))
                System.out.println(dict.get(name));
            else
                System.out.println("no name such as " + name);
        }
        sc.close();
    }
}
