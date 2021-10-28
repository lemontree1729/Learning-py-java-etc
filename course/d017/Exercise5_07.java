class Exercise5_07 {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("USAGE: java Exercise5_7 3120");
            System.exit(0);
        }
        int money = Integer.parseInt(args[0]);
        System.out.println("money=" + money);
        int[] coinUnit = { 500, 100, 50, 10 };
        int[] coin = { 5, 5, 5, 5 };
        for (int i = 0; i < coinUnit.length; i++) {
            int coinNum = 0;
            coinNum = money / coinUnit[i];
            if (coinNum > coin[i]) {
                coinNum = coin[i];
            }
            coin[i] -= coinNum;
            money -= coinNum * coinUnit[i];
            System.out.println(coinUnit[i] + "won: " + coinNum);
        }
        if (money > 0) {
            System.out.println("Not enough change");
            System.exit(0);
        }
        System.out.println("=left coins=");
        for (int i = 0; i < coinUnit.length; i++) {
            System.out.println(coinUnit[i] + "won: " + coin[i]);
        }
    }
}
