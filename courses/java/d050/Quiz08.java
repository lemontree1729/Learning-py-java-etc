package d050;

import java.io.File;

class Quiz08 {
    public static void main(String[] args) {
        var c = new File("c:/");
        var size = 0L;
        var name = "";
        for (var file : c.listFiles()) {
            if (file.length() > size) {
                size = file.length();
                name = file.getName();
            }
        }
        System.out.println("biggest file is " + name + " and size is " + size + " byte");
    }
}
