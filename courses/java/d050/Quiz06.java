package d050;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

class Quiz06 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var bpath = "c:/temp/";
        System.out.print("enter first file name>>");
        var fname1 = sc.nextLine();
        System.out.print("enter second file name>>");
        var fname2 = sc.nextLine();
        int temp;
        FileWriter fout;
        FileReader fin1, fin2;
        try {
            fout = new FileWriter(bpath + "appended.txt");
            fin1 = fname1.contains(":") ? new FileReader(fname1) : new FileReader(bpath + fname1);
            fin2 = fname2.contains(":") ? new FileReader(fname2) : new FileReader(bpath + fname2);
            while ((temp = fin1.read()) != -1)
                fout.write(temp);
            fin1.close();
            while ((temp = fin2.read()) != -1)
                fout.write(temp);
            fin2.close();
            fout.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(fname1 + " and " + fname2 + " merged at appended.txt");
        sc.close();
    }
}
