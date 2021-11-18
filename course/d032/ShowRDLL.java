package d032;

import java.util.Scanner;

class ShowRDLL {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        RDLL list = new RDLL();
        int choice = 0;
        while (choice != 5) {
            System.out.print("1: push, 2: pop, 3: rotate_left, 4: rotate_right,"
                    + "\n5: delete, 6: getValue, 7: show, 8: exit >> ");
            choice = sc.nextInt();
            switch (choice) {
            case 1:
                System.out.print("1: Line, 2: Rect, 3: Circle >> ");
                list.push(sc.nextInt());
                list.show();
                break;
            case 2:
                list.pop();
                list.show();
                break;
            case 3:
                System.out.print("Enter number to rotate left >> ");
                list.rotate_left(sc.nextInt());
                list.show();
                break;
            case 4:
                System.out.print("Enter number to rotate right >> ");
                list.rotate_right(sc.nextInt());
                list.show();
                break;
            case 5:
                System.out.print("Enter index to delete >> ");
                list.delete(sc.nextInt());
                list.show();
                break;
            case 6:
                System.out.print("Enter index to get value >> ");
                list.getValue(sc.nextInt());
                list.show();
                break;
            case 7:
                list.show();
                break;
            case 8:
                System.out.println("Exit the program");
                break;
            }
        }
        sc.close();
    }
}
