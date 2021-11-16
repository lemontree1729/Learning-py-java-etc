package d030;

abstract class Calculator {
    abstract int add(int a, int b);

    protected abstract int subtract(int a, int b);

    public abstract double average(int[] a);
}

class GoodCalc extends Calculator {
    protected int add(int b, int c) {
        return b + c;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public double average(int[] a) {
        double s = 0.0;
        for (int num : a) {
            s += num;
        }
        return s / a.length;
    }

    public static void main(String[] args) {
        GoodCalc a = new GoodCalc();
        int[] b = { 1, 2, 4 };
        String result = Integer.toString(a.add(1, 2)) + '\n' + Integer.toString(a.subtract(2, 3)) + '\n'
                + Double.toString(a.average(b));
        System.out.println(result);
    }
}
