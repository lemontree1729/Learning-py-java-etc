package d032;

abstract class Shape1 {
    Point p;

    Shape1() {
        this(new Point(0, 0));
    }

    Shape1(Point p) {
        this.p = p;
    }

    abstract double calcArea();

    Point getPosition() {
        return p;
    }

    void setPosition(Point p) {
        this.p = p;
    }
}

class Point {
    int x;
    int y;

    Point() {
        this(0, 0);
    }

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "[" + x + ", " + y + "]";
    }
}

class Circle1 extends Shape1 {
    double r;

    Circle1(double r) {
        super();
        this.r = r;
    }

    double calcArea() {
        return Math.PI * r * r;
    }
}

class Rectangle1 extends Shape1 {
    double width;
    double height;

    Rectangle1(double w, double h) {
        super();
        width = w;
        height = h;
    }

    double calcArea() {
        return width * height;
    }

    boolean isSquare() {
        if (width == height)
            return true;
        return false;
    }
}

class Exercise7_22 {

}
