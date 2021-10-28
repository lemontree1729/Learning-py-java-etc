class Exercise5_06 {
    public static void main(String[] args) {
        int[] coinUnit = { 500, 100, 50, 10 };
        int money = 2680;
        System.out.println("money=" + money);
        for (int i = 0; i < coinUnit.length; i++) {
            System.out.print(coinUnit[i] + "won: " + money / coinUnit[i]);
            System.out.println();
            money %= coinUnit[i];
        }
    }
}
