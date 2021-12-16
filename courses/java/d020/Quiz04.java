package d020;

class Rectangle {
    int x, y, width, height;

    Rectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    int square() {
        return width * height;
    }

    void show() {
        System.out.printf("size of %dx%d located at (%d,%d)\n", width, height, x, y);
    }

    boolean contains(Rectangle r) {
        if (x < r.x && x + width > r.x + r.width && y < r.y && y + height > r.y + r.height) {
            return true;
        }
        return false;
    }
}

class Quiz04 {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(2, 2, 8, 7);
        Rectangle s = new Rectangle(5, 5, 6, 6);
        Rectangle t = new Rectangle(1, 1, 10, 10);
        r.show();
        System.out.println("area of s is " + s.square());
        if (t.contains(r))
            System.out.println("t contains r.");
        if (t.contains(s))
            System.out.println("t contains s.");
    }
}
