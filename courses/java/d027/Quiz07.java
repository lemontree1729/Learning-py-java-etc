package d027;

class Point3D extends Point {
    private int z;

    Point3D(int x, int y, int z) {
        super(x, y);
        this.z = z;
    }

    void move(int x, int y, int z) {
        super.move(x, y);
    }

    void moveUp() {
        z++;
    }

    void moveDown() {
        z--;
    }

    public String toString() {
        return String.format("(%d, %d, %d)", getX(), getY(), z);
    }

}

class Quiz07 {
    static void show(Point3D p) {
        System.out.println("point at " + p.toString());
    }

    public static void main(String[] args) {
        Point3D p = new Point3D(1, 2, 3);
        show(p);
        p.moveUp();
        show(p);
        p.moveDown();
        show(p);
        p.move(100, 200, 300);
        show(p);
    }
}
