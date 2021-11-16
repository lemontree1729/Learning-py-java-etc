package d030;

interface Shape2 {
    final double PI = 3.14;

    void draw();

    double getArea();

    default public void redraw() {
        System.out.print("--- redraw!");
        draw();
    }
}

class Circle2 implements Shape2 {
    private int radius = 0;

    Circle2(int radius) {
        this.radius = radius;
    }

    public void draw() {
        System.out.print("Circle radius is " + radius + "\n");
    }

    public double getArea() {
        return PI * radius * radius;
    }
}

public class Quiz13 {
    public static void main(String[] args) {
        Shape2 donut = new Circle2(10);
        donut.redraw();
        System.out.println("Area is " + donut.getArea());
    }
}
