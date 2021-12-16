package d050;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

class Quiz13 {
    static void showFileInfo(File file) {
        var type = file.isFile() ? "file" : "dir";
        System.out.printf("%-7s%-15s%s\n", type, file.length() + " byte", file.getName());
    }

    static void sortBySize(ArrayList<File> fileList) {
        var flow = true;
        while (flow) {
            flow = false;
            for (int i = 0; i < fileList.size() - 1; i++)
                if (fileList.get(i).length() < fileList.get(i + 1).length()) {
                    var temp = fileList.get(i);
                    fileList.set(i, fileList.get(i + 1));
                    fileList.set(i + 1, temp);
                    flow = true;
                }
        }
    }

    public static void main(String[] args) {
        System.out.println("***** file explorer *****");
        var file = new File("c:\\");
        var sc = new Scanner(System.in);
        while (true) {
            var fileList = new ArrayList<File>();
            var dirList = new ArrayList<File>();
            for (var anon : file.listFiles()) {
                if (anon.isFile())
                    fileList.add(anon);
                if (anon.isDirectory())
                    dirList.add(anon);
            }
            sortBySize(fileList);
            sortBySize(dirList);
            if (dirList.size() > 5) {
                for (int i = 0; i < 5; i++)
                    showFileInfo(dirList.get(i));
                System.out.println("...skipped " + (dirList.size() - 5) + " folders");
            } else
                for (int i = 0; i < fileList.size(); i++)
                    showFileInfo(fileList.get(i));
            if (fileList.size() > 5) {
                for (int i = 0; i < 5; i++)
                    showFileInfo(fileList.get(i));
                System.out.println("...skipped " + (fileList.size() - 5) + " files");
            } else
                for (int i = 0; i < fileList.size(); i++)
                    showFileInfo(fileList.get(i));
            System.out.print(">>");
            var input = sc.nextLine();
            if (input.equals("stop"))
                break;
            if (input.equals(".."))
                file = file.getParentFile();
            else
                file = new File(file, input);
        }
    }
}
