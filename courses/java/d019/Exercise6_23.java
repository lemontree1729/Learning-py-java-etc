package d019;

class Exercise6_23 {
    static int max(int[] arr) {
        if (arr == null || arr.length == 0) {
            arr = new int[1];
            arr[0] = -999999;
        }
        if (arr.length == 1) {
            return arr[0];
        } else {
            int result = arr[0];
            for (int i = 1; i < arr.length; i++) {
                if (result < arr[i]) {
                    result = arr[i];
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {
        int[] data = { 3, 2, 9, 4, 7 };
        System.out.println(java.util.Arrays.toString(data));
        System.out.println("max value: " + max(data));
        System.out.println("max value: " + max(null));
        System.out.println("max value: " + max(new int[] {}));
    }
}
