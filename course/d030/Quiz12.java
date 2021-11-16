package d030;

import java.util.Scanner;

abstract class Shape {
    private Shape next;

    Shape() {
        next = null;
    }

    void setNext(Shape obj) {
        next = obj;
    }

    Shape getNext() {
        return next;
    }

    abstract void draw();
}

class Line extends Shape {
    void draw() {
        System.out.println("Line");
    }
}

class Rect extends Shape {
    void draw() {
        System.out.println("Rect");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Circle");
    }
}

class GraphicEditor {
    Shape origin = null;
    Shape target = null;
    Scanner sc = new Scanner(System.in);
    boolean raiseStop = false;
    int cnt = 0;

    void run() {
        System.out.println("Starting graphic editor beauty.");
        while (!raiseStop) {
            System.out.print("1:insert, 2:delete, 3:show, 4:exit>>");
            switch (sc.nextInt()) {
            case 1:
                insert();
                break;
            case 2:
                delete();
                break;
            case 3:
                show();
                break;
            case 4:
                exit();
                break;
            }
        }
        sc.close();
    }

    void insert() {
        cnt++;
        System.out.print("1:Line, 2:Rect, 3:Circle>>");
        Shape temp = null;
        switch (sc.nextInt()) {
        case 1:
            temp = new Line();
            break;
        case 2:
            temp = new Rect();
            break;
        case 3:
            temp = new Circle();
            break;
        }
        if (origin == null) {
            origin = temp;
            target = temp;
        } else {
            target.setNext(temp);
            target = target.getNext();
        }
    }

    void delete() {
        System.out.print("index of deleting shape>>");
        int index = sc.nextInt();
        if (index > cnt) {
            System.out.println("Cannot delete");
        } else {
            Shape a = origin;
            if (index == 1) {
                origin = origin.getNext();
            } else {
                for (int i = 0; i < index - 2; i++) {
                    a = a.getNext();
                }
                a.setNext(a.getNext().getNext());
            }
        }
    }

    void show() {
        Shape b = origin;
        while (b != null) {
            b.draw();
            b = b.getNext();
        }
    }

    void exit() {
        System.out.println("beauty Exited");
        raiseStop = true;
    }
}

public class Quiz12 {
    public static void main(String[] args) {
        GraphicEditor beauty = new GraphicEditor();
        beauty.run();
    }
}
