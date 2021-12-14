package d050;

import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

class Quiz03 {
    public static void main(String[] args) {
        int temp;
        var fpath = "c:/windows/system.ini";
        try {
            var fread = new FileReader(fpath);
            while ((temp = fread.read()) != -1)
                System.out.print(Character.toUpperCase((char) temp));
            fread.close();
            System.out.println("print " + fpath + " with line numbers");
            var sc = new Scanner(new FileReader(fpath));
            var cnt = 0;
            while (sc.hasNextLine())
                System.out.printf("%5d: %s\n", ++cnt, sc.nextLine());
            sc.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
