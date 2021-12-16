package d045;

class Circle {
    int x, y, r;

    Circle(int x, int y, int r) {
        this.x = x;
        this.y = y;
        this.r = r;
    }

    public String toString() {
        return String.format("Circle(%d,%d), radius:%d", x, y, r);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Circle))
            return false;
        Circle other = (Circle) obj;
        if (this.x != other.x || this.y != other.y)
            return false;
        return true;
    }
}

class Quiz02 {
    public static void main(String[] args) {
        Circle a = new Circle(2, 3, 5);
        Circle b = new Circle(2, 3, 30);
        System.out.println("circle a: " + a);
        System.out.println("circle b: " + b);
        if (a.equals(b))
            System.out.println("same circle");
        else
            System.out.println("different circle");
    }
}
