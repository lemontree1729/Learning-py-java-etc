package d050;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

class Quiz12 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new ArrayList<String>();
        System.out.print("enter filepath>>");
        var fpath = sc.nextLine();
        try {
            var fsc = new Scanner(new File(fpath));
            while (fsc.hasNextLine())
                data.add(fsc.nextLine());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.exit(0);
        }
        while (true) {
            System.out.print("search>>");
            var temp = sc.nextLine();
            if (temp.equals("stop"))
                break;
            for (int i = 0; i < data.size(); i++)
                if (data.get(i).contains(temp))
                    System.out.println(i + ": " + data.get(i));
        }
        System.out.println("system closed");
        sc.close();
    }
}
