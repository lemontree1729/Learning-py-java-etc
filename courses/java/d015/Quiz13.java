package d015;

class Quiz13 {
    public static void main(String[] args) {
        int cnt;
        for (int i = 1; i < 100; i++) {
            int[] digits = { i / 10, i % 10 };
            cnt = 0;
            for (int digit : digits) {
                if (digit % 3 == 0 && digit != 0) {
                    cnt++;
                }
            }
            if (cnt != 0) {
                System.out.println(i + " clap " + cnt);
            }
        }
    }
}
