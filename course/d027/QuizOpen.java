package d027;

import java.util.Scanner;

abstract class GameObject {
    protected int distance;
    protected int x, y;

    GameObject(int startX, int startY, int distance) {
        this.x = startX;
        this.y = startY;
        this.distance = distance;
    }

    int getX() {
        return x;
    }

    int getY() {
        return y;
    }

    boolean collide(GameObject p) {
        return this.x == p.getX() && this.y == p.getY() ? true : false;
    }

    protected abstract void move();

    protected abstract char getShape();
}

class Bear extends GameObject {
    private char moveDirection;

    Bear(int x, int y, int dis) {
        super(x, y, dis);
    }

    protected void move() {
        switch (moveDirection) {
        case 'w':
            y = (y + 9) % 10;
            break;
        case 'a':
            x = (x + 19) % 20;
            break;
        case 's':
            y = (y + 1) % 10;
            break;
        case 'd':
            x = (x + 1) % 20;
            break;
        }
    }

    protected char getShape() {
        return 'B';
    }

    void setDirection(char a) {
        moveDirection = a;
    }
}

class Fish extends GameObject {
    private int cnt = 1;

    Fish(int x, int y, int dis) {
        super(x, y, dis);
    }

    protected void move() {
        if (cnt % 5 > 2) {
            switch ((int) (Math.random() * 4)) {
            case 0:
                y = (y + 9) % 10;
                break;
            case 1:
                x = (x + 19) % 20;
                break;
            case 2:
                y = (y + 1) % 10;
                break;
            case 3:
                x = (x + 1) % 20;
                break;
            }
        }
        cnt++;
    }

    protected char getShape() {
        return '@';
    }
}

class Game {
    Bear bear;
    Fish fish;
    char[][] info = new char[10][20];
    Scanner sc = new Scanner(System.in);

    void start() {
        System.out.println("** starting fish eating game! **");
        bear = new Bear(0, 0, 1);
        fish = new Fish((int) (Math.random() * 20), (int) (Math.random() * 10), 1);
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 20; j++) {
                info[i][j] = '-';
            }
        }
        show();
    }

    void show() {
        info[fish.y][fish.x] = fish.getShape();
        info[bear.y][bear.x] = bear.getShape();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 20; j++) {
                System.out.print(info[i][j]);
            }
            System.out.println();
        }
        info[bear.y][bear.x] = '-';
        info[fish.y][fish.x] = '-';
    }

    void move() {
        System.out.print("w(up), a(left), s(down), d(right)>>");
        bear.setDirection(sc.next().charAt(0));
        bear.move();
        fish.move();
    }

    void close() {
        System.out.println("Bear Wins!!");
        sc.close();
    }
}

class QuizOpen {
    public static void main(String[] args) {
        Game my = new Game();
        my.start();
        while (!my.bear.collide(my.fish)) {
            my.move();
            my.show();
        }
        my.close();
    }
}
