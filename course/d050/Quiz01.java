package d050;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

class Quiz01 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        try {
            var fpath = "c:/temp/phone.txt";
            var fout = new FileWriter(fpath, true);
            while (true) {
                System.out.print("enter name and phone number>>");
                var input = sc.nextLine();
                if (input.equals("stop"))
                    break;
                fout.write(input + "\n");
            }
            fout.close();
            System.out.println("made file at " + fpath);
        } catch (IOException e) {
            e.printStackTrace();
        }
        sc.close();
    }
}
