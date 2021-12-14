package d047;

import java.util.ArrayList;
import java.util.Scanner;

abstract class Shape {
    abstract void show();
}

class Line extends Shape {
    void show() {
        System.out.print("Line ");
    }
}

class Rect extends Shape {
    void show() {
        System.out.print("Rect ");
    }
}

class Circle extends Shape {
    void show() {
        System.out.print("Circle ");
    }
}

class Quiz10 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new ArrayList<Shape>();
        System.out.println("starting graphic editor beauty");
        boolean endcheck = true;
        while (endcheck) {
            System.out.print("put(1), remove(2), show(3), exit(4)>>");
            switch (sc.nextInt()) {
                case 1:
                    System.out.print("Line(1), Rect(2), Circle(3)>>");
                    Shape target = null;
                    switch (sc.nextInt()) {
                        case 1:
                            target = new Line();
                            break;
                        case 2:
                            target = new Rect();
                            break;
                        case 3:
                            target = new Circle();
                            break;
                    }
                    data.add(target);
                    break;
                case 2:
                    System.out.print("enter index>>");
                    int index = sc.nextInt();
                    if (index >= data.size() || index < 0)
                        System.out.println("remove failed");
                    else {
                        data.remove(index);
                        System.out.println("remove successed");
                    }
                    break;
                case 3:
                    data.forEach(Shape::show);
                    System.out.println();
                    break;
                case 4:
                    System.out.println("exiting program");
                    endcheck = false;
                    break;
            }
        }
        sc.close();
    }
}
