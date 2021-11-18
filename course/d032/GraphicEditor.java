package d032;

import java.util.Scanner;

class GraphicEditor {
    private String name;
    private Shape start = null, last = null;
    Scanner sc = new Scanner(System.in);

    GraphicEditor(String name) {
        this.name = name;
    }

    void run() {
        System.out.println("Starting" + name);
        int choice = 0;
        int num = 0;

        while (choice != 4) {
            System.out.print("1: insert, 2: delete, 3: show all, 4:exit : ");
            choice = sc.nextInt();
            switch (choice) {
            case 1:
                System.out.print("1: Line, 2: Rect, 3: Circle : ");
                num = sc.nextInt();
                if (num < 1 || num > 3) {
                    System.out.println("wrong input!");
                    break;
                }
                insert(num);
                break;
            case 2:
                System.out.println("enter index of shape : ");
                if (!delete(num)) {
                    System.out.println("cannot delete");
                }
                break;
            case 3:
                show();
                break;
            case 4:
                System.out.println("Exit " + name);
                break;
            }
        }
    }

    private void insert(int num) {
        Shape obj = null;
        switch (num) {
        case 1:
            obj = new Line();
            break;
        case 2:
            obj = new Rect();
            break;
        case 3:
            obj = new Circle();
            break;
        }
        if (start == null) {
            start = last = obj;
        } else {
            last.setNext(obj);
            last = obj;
        }
    }

    private boolean delete(int num) {
        Shape cur = start;
        Shape pre = start;
        if (start == null) {
            return false;
        }
        for (int i = 0; i < num; i++) {
            pre = cur;
            cur = cur.getNext();
            if (cur == null) {
                return false;
            }
        }
        if (start == last) {
            start = last = null;
            return true;
        }
        if (cur == start) {
            start = start.getNext();
        } else if (cur == last) {
            last = pre;
            last.setNext(null);
        } else {
            pre.setNext(cur.getNext());
        }
        return true;
    }

    private void show() {
        Shape t = start;
        while (t != null) {
            t.draw();
            t = t.getNext();
        }
    }

    public static void main(String[] args) {
        GraphicEditor ge = new GraphicEditor("beauty");
        ge.run();
    }
}
