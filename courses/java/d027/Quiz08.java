package d027;

class PositivePoint extends Point {
    PositivePoint() {
        super(0, 0);
    }

    PositivePoint(int x, int y) {
        super(x, y);
        if (x < 0 || y < 0) {
            super.move(0, 0);
        }
    }

    protected void move(int x, int y) {
        if (x >= 0 && y >= 0) {
            super.move(x, y);
        }
    }

    public String toString() {
        return String.format("(%d, %d)", getX(), getY());
    }
}

public class Quiz08 {
    static void show(PositivePoint p) {
        System.out.println("point at " + p.toString());
    }

    public static void main(String[] args) {
        PositivePoint p = new PositivePoint();
        p.move(10, 10);
        show(p);
        p.move(-5, 5);
        show(p);
        PositivePoint p2 = new PositivePoint(-10, -10);
        show(p2);
    }
}
