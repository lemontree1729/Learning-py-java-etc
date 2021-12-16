package d027;

class Shape {
    Shape next;

    Shape() {
        next = null;
    }

    void draw() {
        System.out.println("Shape");
    }
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

class MethodOverridingEx {
    static void paint(Shape p) {
        p.draw();
    }

    public static void main(String[] args) {

        // override each draw methods
        paint(new Shape());
        paint(new Line());
        paint(new Rect());

        Shape start, temp, obj, a, t, hard;

        start = new Line();
        temp = start;
        obj = new Rect();
        temp.next = obj;
        temp = obj;
        obj = new Line();
        temp.next = obj;
        temp = obj;
        obj = new Circle();
        temp.next = obj;
        Shape p = start;
        while (p != null) {
            p.draw();
            p = p.next;
        }
        a = new Line();
        t = a;
        t = t.next = new Rect();
        t = t.next = new Line();
        t = t.next = new Circle();
        while (a != null) {
            a.draw(); // override draw method with same Shape class declare
                      // and different assigned class
            a = a.next;
        }
        hard = new Line();
        hard.next = new Rect();
        hard.next.next = new Line();
        hard.next.next.next = new Circle();
        while (hard != null) {
            hard.draw();
            hard = hard.next;
        }
    }
}
