package d050;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

class Quiz05 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var bpath = "c:/temp/";
        System.out.print("enter first file name>>");
        var fname1 = sc.nextLine();
        System.out.print("enter second file name>>");
        var fname2 = sc.nextLine();
        System.out.println("comparing " + fname1 + " and " + fname2);
        int temp1, temp2;
        FileInputStream fread1, fread2;
        boolean isSame = true;
        try {
            fread1 = fname1.contains(":") ? new FileInputStream(fname1) : new FileInputStream(bpath + fname1);
            fread2 = fname2.contains(":") ? new FileInputStream(fname2) : new FileInputStream(bpath + fname2);
            while (true) {
                temp1 = fread1.read();
                temp2 = fread2.read();
                if (temp1 != temp2) {
                    isSame = false;
                    break;
                }
                if (temp1 == -1)
                    break;
            }
            fread1.close();
            fread2.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (isSame)
            System.out.println("file is same");
        else
            System.out.println("file is different");
        sc.close();
    }
}
