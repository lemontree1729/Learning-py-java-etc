package d020;

import java.util.Scanner;

class Quiz12 {

    static void show(String[][] seat, String[] seatcol) {

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("system");
        while (true) {
            System.out.print(":1, :2, :3, :4");
            int menunum = sc.nextInt();
            String[][] chair = new String[3][10];
            for (int y = 0; y < chair.length; y++) {
                for (int x = 0; x < chair[0].length; x++) {
                    chair[y][x] = "---";
                }
            }
            switch (menunum) {
            case 1:
                System.out.print("select seat column S(1), A(2), B(3)>>");
                int seatcol = sc.nextInt() - 1;
                
                show(chair, {seatcol});
            }
        }
    }
}
