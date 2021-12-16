package d050;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

class Quiz07 {
    public static void main(String[] args) {
        System.out.println("copy a.jpg to b.jpg");
        var fpath = "c:/temp/";
        var a = new File(fpath + "a.jpg");
        var b = new File(fpath + "b.jpg");
        try {
            var ain = new FileInputStream(a);
            var bout = new FileOutputStream(b);
            int data;
            long temp = 0L;
            while ((data = ain.read()) != -1) {
                bout.write(data);
                if (((b.length() - temp) * 10 / a.length()) > 0) {
                    temp = b.length() - 1;
                    System.out.print("*");
                }
            }
            ain.close();
            bout.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
