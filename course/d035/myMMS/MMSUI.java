package d035.myMMS;

import java.util.Scanner;

public class MMSUI {
    public static void main(String[] args) {
        MMSData mydata = new MMSData();
        boolean stop = false;
        Scanner sc = new Scanner(System.in);
        int toggle = 0;
        do {
            System.out.println("=====member data=====");
            System.out.println("1. member register");
            System.out.println("2. member list");
            System.out.println("3. member update");
            System.out.println("4. member delete");
            System.out.println("5. member search");
            System.out.println("6. exit program");
            System.out.print("menu to go: ");
            toggle = MMSAction.checkInt(sc);
            switch (toggle) {
            case 1:
                MMSControl.register();
                break;
            case 2:
                MMSControl.show();
                break;
            case 3:
                MMSControl.update();
                break;
            case 4:
                MMSControl.delete();
                break;
            case 5:
                MMSControl.search();
                break;
            case 6:
                stop = true;
                System.out.println("program exit");
                break;
            default:
                System.out.println("wrong int(1~6)");
            }
        } while (!stop);
    }
}
