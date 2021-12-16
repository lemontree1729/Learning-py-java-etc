package d032;

abstract class Shape {
    private Shape before;
    private Shape next;

    Shape() {
        before = null;
        next = null;
    }

    void setNext(Shape obj) {
        next = obj;
    }

    void setBefore(Shape obj) {
        before = obj;
    }

    Shape getNext() {
        return next;
    }

    Shape getBefore() {
        return before;
    }

    abstract void draw();
}

class Line extends Shape {
    @Override
    public void draw() {
        System.out.print("1");
    }
}

class Rect extends Shape {
    @Override
    public void draw() {
        System.out.print("2");
    }
}

class Circle extends Shape {
    @Override
    public void draw() {
        System.out.print("3");
    }
}