public class Circle { // define class name
    // declare member variables(instance variable and class variable)
    int radius; // instance variable radius and name
    String name;
    static int cnt = 0; // class variable cnt
    // static variables and functions can even use without new instance
    // because it will be made when class is made

    public Circle() { // first constructor
    }

    public Circle(int radius) { // second constructor with parameter radius(or local variable of constuctor)
        // also known as method overloading
        this.radius = radius; // use this(reference instance itself) to distinguish instance variable radius
                              // with local variable radius
    }

    public double getArea() { // instance method of Circle
        return 3.14 * radius * radius;
    }

    public static void main(String[] args) {
        System.out.println(Circle.cnt);
        // System.out.println(pizza.cnt);
        // --> makes error because instance can't access to class variable
        Circle pizza = new Circle(); // make Circle class instance pizza with first constructor
        pizza.radius = 10;
        pizza.name = "Java pizza";
        System.out.println(pizza.name + "@ radius: " + pizza.radius + ", area: " + pizza.getArea());
        Circle donut = new Circle(2); // make Circle class instance donut with second constructor
        donut.name = "Java donut";
        System.out.println(donut.name + "@ radius: " + donut.radius + ", area: " + donut.getArea());
    }
}
