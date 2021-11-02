package d017;

class Exercise5_04 {
    public static void main(String[] args) {
        int[][] arr = { { 5, 5, 5, 5, 5 }, { 10, 10, 10, 10, 10 }, { 20, 20, 20, 20, 20 }, { 30, 30, 30, 30, 30 } };
        int total = 0;
        float average = 0;
        int cnt = 0;
        for (int[] col : arr) {
            cnt += col.length;
            for (int i : col) {
                total += i;
            }
        }
        average = total / (float) cnt;
        System.out.println("total=" + total);
        System.out.println("average=" + average);
    }
}
