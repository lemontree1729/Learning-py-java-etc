package d032;

class Exercise7_23 {
    static double sumArea(Shape1[] arr) {
        double total = 0;
        for (Shape1 a : arr)
            total += a.calcArea();
        return total;
    }

    public static void main(String[] args) {
        Shape1[] arr = { new Circle1(5.0), new Rectangle1(3, 4), new Circle1(1) };
        System.out.println("Sum of area: " + sumArea(arr));
    }
}
