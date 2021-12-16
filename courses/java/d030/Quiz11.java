package d030;

import java.util.Scanner;

abstract class Calc {
    static int a, b;

    static void setValue(int a, int b) {
        Calc.a = a;
        Calc.b = b;
    }

    abstract int calculate();
}

class Add extends Calc {
    int calculate() {
        return a + b;
    }
}

class Sub extends Calc {
    int calculate() {
        return a - b;
    }
}

class Mul extends Calc {
    int calculate() {
        return a * b;
    }
}

class Div extends Calc {
    int calculate() {
        return a / b;
    }
}

public class Quiz11 {
    public static void main(String[] args) {
        System.out.print("Enter two integers and operator>>");
        Scanner sc = new Scanner(System.in);
        Calc.setValue(sc.nextInt(), sc.nextInt());
        switch (sc.next().charAt(0)) {
        case '+':
            Add add = new Add();
            System.out.println(add.calculate());
            break;
        case '-':
            Sub sub = new Sub();
            System.out.println(sub.calculate());
            break;
        case '*':
            Mul mul = new Mul();
            System.out.println(mul.calculate());
            break;
        default:
            Div div = new Div();
            System.out.println(div.calculate());
            break;
        }
        sc.close();
    }
}
