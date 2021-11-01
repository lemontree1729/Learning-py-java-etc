class Exercise6_22 {
    static boolean isNumber(String str) {
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) < 48 || str.charAt(i) > 57) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String str = "123";
        System.out.println(str + " is number? " + isNumber(str));
        str = "1234o";
        System.out.println(str + " is number? " + isNumber(str));
    }
}
