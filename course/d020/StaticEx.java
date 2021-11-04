// Quiz09
package d020;

class ArrayUtil {
    static int[] concat(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        for (int i = 0; i < a.length; i++) {
            result[i] = a[i];
        }
        for (int i = 0; i < b.length; i++) {
            result[i + a.length] = b[i];
        }
        return result;
    }

    static void print(int[] a) {
        String toprint = "";
        if (!(a == null || a.length == 0)) {
            for (int i = 0; i < a.length; i++) {
                if (i == 0) {
                    toprint += a[0];
                } else {
                    toprint += ", " + a[i];
                }
            }
        }
        System.out.println("[" + toprint + "]");
    }
}

class StaticEx {
    public static void main(String[] args) {
        int[] array1 = { 1, 5, 7, 9 };
        int[] array2 = { 3, 6, -1, 100, 77 };
        int[] array3 = ArrayUtil.concat(array1, array2);
        ArrayUtil.print(array3);
    }
}
