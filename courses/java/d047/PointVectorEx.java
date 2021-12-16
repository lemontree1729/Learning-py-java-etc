package d047;

import java.util.ArrayList;

class Point {
    int x, y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)", x, y);
    }
}

class PointVectorEx {
    public static void main(String[] args) {
        var a = new ArrayList<Point>();
        int n = 100, m = 100;
        for (int i = 0; i < n; i++)
            a.add(new Point((int) (Math.random() * m), (int) (Math.random() * m)));
        System.out.println(a);
    }
}
