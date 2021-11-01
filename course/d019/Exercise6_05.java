class Exercise6_05 {
    public static void main(String[] args) {
        Students s = new Students("john do", 1, 1, 100, 60, 76);
        System.out.println(s.info());
    }
}

class Students {
    String name;
    int[] scores;

    public Students(String name, int... args) {
        this.name = name;
        scores = args;
    }

    public String info() {
        String result = name;
        int sum = 0;
        for (int i = 0; i < scores.length; i++) {
            result += ", " + scores[i];
            if (i > 1) {
                sum += scores[i];
            }
        }
        result += ", " + sum + ", " + Math.round(sum * 10.0 / (scores.length - 2)) / 10.0;
        return result;
    }
}