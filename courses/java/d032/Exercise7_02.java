package d032;

class NewSutdaDeck extends SutdaDeck {
    void shuffle() {
        for (int i = 0; i < CARD_NUM; i++) {
            int ran = (int) (Math.random() * 20);
            SutdaCard temp = cards[i];
            cards[i] = cards[ran];
            cards[ran] = temp;
        }
    }

    SutdaCard pick(int index) {
        return cards[index];
    }

    SutdaCard pick() {
        return cards[(int) (Math.random() * 20)];
    }
}

class Exercise7_02 {
    public static void main(String[] args) {
        NewSutdaDeck deck = new NewSutdaDeck();
        System.out.println(deck.pick(0));
        System.out.println(deck.pick());
        deck.shuffle();
        for (int i = 0; i < deck.cards.length; i++)
            System.out.print(deck.cards[i] + ", ");
        System.out.println();
        System.out.println(deck.pick(0));
    }
}
