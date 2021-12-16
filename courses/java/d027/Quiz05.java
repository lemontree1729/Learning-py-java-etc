package d027;

class Point {
    private int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    protected void move(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class ColorPoint extends Point {
    private String color;

    ColorPoint() {
        super(0, 0);
        color = "BLACK";
    }

    ColorPoint(int x, int y, String color) {
        super(x, y);
        this.color = color;
    }

    void setXY(int x, int y) {
        move(x, y);
    }

    void setColor(String color) {
        this.color = color;
    }

    public String toString() {
        return color + " color at (" + getX() + ", " + getY() + ") point";
    }

}

public class Quiz05 {
    public static void main(String[] args) {
        ColorPoint zeroPoint = new ColorPoint();
        System.out.println(zeroPoint.toString());
        ColorPoint cp = new ColorPoint(5, 5, "YELLOW");
        cp.setXY(10, 20);
        cp.setColor("RED");
        System.out.println(cp.toString());
    }
}
