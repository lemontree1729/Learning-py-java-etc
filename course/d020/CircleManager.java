// Quiz05 and Quiz 06
package d020;

import java.util.Scanner;

class Circle {
    private double x, y;
    int radius;

    Circle(double x, double y, int radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    void show() {
        System.out.printf("(%.1f,%.1f)%d\n", x, y, radius);
    }
}

class CircleManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Circle[] c = new Circle[3];
        for (int i = 0; i < c.length; i++) {
            System.out.print("x, y, radius >>");
            double x = sc.nextDouble();
            double y = sc.nextDouble();
            int radius = sc.nextInt();
            c[i] = new Circle(x, y, radius);
        }
        int maxarea = 0;
        int index = 0;
        for (int i = 0; i < c.length; i++) {
            if (c[i].radius * c[i].radius > maxarea) {
                maxarea = c[i].radius * c[i].radius;
                index = i;
            }
            c[i].show();
        }
        c[index].show();
        sc.close();
    }
}
