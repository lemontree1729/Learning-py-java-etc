package d032;

class Exercise7_19 {
    public static void main(String[] args) {
        Buyer b = new Buyer();
        b.buy(new Tv());
        b.buy(new Computer());
        b.buy(new Tv());
        b.buy(new Audio());
        b.buy(new Computer());
        b.buy(new Computer());
        b.buy(new Computer());

        b.summary();
    }
}

class Buyer {
    int money = 1000;
    Product[] cart = new Product[3];
    int i = 0;

    void buy(Product p) {
        if (p.price > money)
            return;
        money -= p.price;
        add(p);
    }

    void add(Product p) {
        int n = cart.length;
        if (i >= n) {
            Product[] temp = new Product[2 * n];
            for (int j = 0; j < n; j++)
                temp[j] = cart[j];
            cart = temp;
        }
        cart[i] = p;
        i++;
    }

    void summary() {
        int total = 0;
        System.out.print("bought: ");
        for (int j = 0; j < i; j++) {
            System.out.print(cart[j].toString());
            total += cart[j].price;
            if (j != i - 1) {
                System.out.print(", ");
            }
        }
        System.out.println();
        System.out.println("total: " + total);
        System.out.println("charge: " + money);
    }
}

class Product {
    int price;

    Product(int price) {
        this.price = price;
    }
}

class Tv extends Product {
    Tv() {
        super(100);
    }

    public String toString() {
        return "Tv";
    }
}

class Computer extends Product {
    Computer() {
        super(200);
    }

    public String toString() {
        return "Computer";
    }
}

class Audio extends Product {
    Audio() {
        super(50);
    }

    public String toString() {
        return "Audio";
    }
}