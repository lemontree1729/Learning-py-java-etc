package d050;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

class Quiz11 {
    public static void main(String[] args) {
        var fpath = "c:\\temp\\SATwords.txt";
        var wordFile = new File(fpath);
        var wordArray = new ArrayList<String>();
        Scanner sc;
        try {
            sc = new Scanner(wordFile);
            while (sc.hasNextLine()) {
                var temp = sc.nextLine().split(" ");
                if (temp.length == 1 && !temp[0].contains("#"))
                    wordArray.add(temp[0]);
            }
        } catch (IOException e) {
            System.out.println("reading " + fpath + " failed");
            e.printStackTrace();
        }
        System.out.println("reading " + fpath + " successful");
        sc = new Scanner(System.in);
        while (true) {
            System.out.print("word>>");
            var input = sc.nextLine();
            if (input.equals("stop"))
                break;
            for (var word : wordArray)
                if (word.startsWith(input))
                    System.out.println(word);
            System.out.println("--------------------");
        }
        System.out.println("system closed");
        sc.close();
    }
}
