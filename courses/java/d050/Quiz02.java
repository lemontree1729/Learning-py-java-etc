package d050;

import java.io.FileReader;
import java.io.IOException;

class Quiz02 {
    public static void main(String[] args) {
        var fpath = "c:/temp/phone.txt";
        System.out.println("printing " + fpath);
        try {
            var fin = new FileReader(fpath);
            int temp = 0;
            while ((temp = fin.read()) != -1) {
                System.out.print((char) temp);
            }
            fin.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
