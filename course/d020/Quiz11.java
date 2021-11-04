package d020;

import java.util.Scanner;

class Add {
    int a, b;

    void setValue(int a, int b) {
        this.a = a;
        this.b = b;
    }

    int calculate() {
        return a + b;
    }
}

class Sub {
    int a, b;

    void setValue(int a, int b) {
        this.a = a;
        this.b = b;
    }

    int calculate() {
        return a - b;
    }
}

class Mul {
    int a, b;

    void setValue(int a, int b) {
        this.a = a;
        this.b = b;
    }

    int calculate() {
        return a * b;
    }
}

class Div {
    int a, b;

    void setValue(int a, int b) {
        this.a = a;
        this.b = b;
    }

    int calculate() {
        return a / b;
    }
}

class Quiz11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter number1, number2 and operator>>");
        int a = sc.nextInt(), b = sc.nextInt();
        char op = sc.next().charAt(0);
        switch (op) {
        case '+':
            Add add = new Add();
            add.setValue(a, b);
            System.out.println(add.calculate());
            break;
        case '-':
            Sub sub = new Sub();
            sub.setValue(a, b);
            System.out.println(sub.calculate());
            break;
        case '*':
            Mul mul = new Mul();
            mul.setValue(a, b);
            System.out.println(mul.calculate());
            break;
        case '/':
            Div div = new Div();
            div.setValue(a, b);
            System.out.println(div.calculate());
            break;
        }
    }
}
