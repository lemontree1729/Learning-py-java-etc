package d050;

import java.io.File;

class Quiz09 {
    public static void main(String[] args) {
        var fpath = "c:\\temp\\mytemp";
        var temp = new File(fpath);
        System.out.println("deleting all txt files in " + fpath);
        var filelist = temp.listFiles();
        var cnt = 0;
        for (int i = 0; i < filelist.length; i++) {
            if (filelist[i].getName().contains(".txt")) {
                System.out.println("deleting " + filelist[i].getAbsoluteFile());
                filelist[i].delete();
                cnt++;
            }
        }
        System.out.println("deleted file number: " + cnt);
    }
}
