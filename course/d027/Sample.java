package d027;

class SuperObject {
    void paint() {
        System.out.println(1);
        draw();
        System.out.println(2);
    }

    void draw() {
        System.out.println(3);
        draw();
        System.out.println(4);
        System.out.println("Super");
        System.out.println(5);
    }
}

class SubObject extends SuperObject {
    // @Override
    void paint() {
        System.out.println(6);
        super.draw();
        System.out.println(7);
    }

    // @Override
    void draw() {
        System.out.println(8);
        System.out.println("Sub");
        System.out.println(9);
    }
}

class Sample {
    public static void main(String[] args) {
        SuperObject a = new SubObject();
        a.paint();
        System.out.println("---------------");
        SubObject b = new SubObject();
        b.paint();
        // SuperObject c = new SuperObject(); -> prints 3 forever!
        // c.paint();

    }
}
