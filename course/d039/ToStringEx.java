package d039;

class Circle {
    int x, y;

    Circle(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}

class ToStringEx {
    public static void main(String[] args) {
        Circle a = new Circle(3, 7);
        System.out.println("point at: " + a);
    }
}
