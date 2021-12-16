package d032;

class NewSutdaCard {
    private int num; // you could also use final!
    private boolean isKwang;

    NewSutdaCard() {
        this(1, true);
    }

    NewSutdaCard(int num, boolean isKwang) {
        this.num = num;
        this.isKwang = isKwang;
    }

    public String toString() {
        return num + (isKwang ? "K" : "");
    }
}

public class Exercise7_14 {
    public static void main(String[] args) {
        SutdaCard card = new SutdaCard(1, true);
        System.out.println(card.toString());
    }
}
