package d030;

import java.util.Scanner;

abstract class Converter {
    abstract protected double convert(double src);

    abstract protected String getSrcString();

    abstract protected String getDestString();

    protected double ratio;

    void run() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Convert " + getSrcString() + " to " + getDestString());
        System.out.print("Enter " + getSrcString() + ">> ");
        double val = sc.nextDouble();
        double res = convert(val);
        System.out.println("result: " + res + getDestString());
        sc.close();
    }
}

class Won2Dollar extends Converter {
    Won2Dollar(double ratio) {
        this.ratio = 1 / ratio;
    }

    protected double convert(double src) {
        return src * ratio;
    }

    protected String getSrcString() {
        return "won";
    }

    protected String getDestString() {
        return "dollar";
    }
}

class Quiz03 {
    public static void main(String[] args) {
        Won2Dollar toDollar = new Won2Dollar(1200);
        toDollar.run();
    }
}