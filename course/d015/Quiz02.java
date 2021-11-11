package d015;

class Quiz02 {
    public static void main(String[] args) {
        int n[][] = { { 1 }, { 1, 2, 3 }, { 1 }, { 1, 2, 3, 4 }, { 1, 2 } };
        for (int col[] : n) {
            for (int num : col) {
                System.out.print(num + "  ");
            }
            System.out.println();
        }
    }
}
