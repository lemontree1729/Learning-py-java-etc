package d045;

class MyPoint {
    int x, y;

    MyPoint(int nx, int ny) {
        x = nx;
        y = ny;
    }

    public String toString() {
        return "Point(" + this.x + "," + this.y + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof MyPoint))
            return false;
        MyPoint other = (MyPoint) obj;
        if (this.x != other.x || this.y != other.y)
            return false;
        return true;
    }
}

class Quiz01 {
    public static void main(String[] args) {
        MyPoint p = new MyPoint(3, 50);
        MyPoint q = new MyPoint(4, 50);
        System.out.println(p);
        if (p.equals(q))
            System.out.println("same point");
        else
            System.out.println("different point");
    }
}
