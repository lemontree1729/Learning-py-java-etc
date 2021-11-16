package d030;

class Oval2 implements Shape2 {
    private int x, y;

    Oval2(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void draw() {
        System.out.print(" Ellipse inscribed in " + x + "x" + y + "\n");
    }

    public double getArea() {
        return PI * (x / 2.0) * (y / 2.0);
    }
}

class Rect2 implements Shape2 {
    private int x, y;

    Rect2(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void draw() {
        System.out.print(" Rectanguler size of " + x + "x" + y + "\n");
    }

    public double getArea() {
        return (double) (x * y);
    }

}

public class Quiz14 {
    public static void main(String[] args) {
        Shape2[] list = new Shape2[3];
        list[0] = new Circle2(10);
        list[1] = new Oval2(20, 30);
        list[2] = new Rect2(10, 40);

        for (int i = 0; i < list.length; i++) {
            list[i].redraw();
        }
        for (int i = 0; i < list.length; i++) {
            System.out.println("Area is " + list[i].getArea());
        }
    }
}
