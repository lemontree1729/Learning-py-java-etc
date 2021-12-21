package d055;

class SynchronizedEx {
    public static void main(String[] args) {
        Thread a = new StudentThread("A");
        Thread b = new StudentThread("B");
        System.out.println("main: A start");
        a.start();
        System.out.println("main: B start");
        b.start();
        for (int i = 0; i < 3; i++)
            System.out.println("main: " + i);
    }
}

class StudentThread extends Thread {
    static int n1 = 0, n2 = 0, n3 = 0;

    StudentThread(String name) {
        super(name);
    }

    synchronized void withSync() {
        System.out.printf("%s: withSync on %s, %d\n", Thread.currentThread().getName(), this.getName(), n1++);
    }

    void withoutSync() {
        System.out.printf("%s: withoutSync on %s, %d\n", Thread.currentThread().getName(), this.getName(), n2++);
    }

    void withYield() {
        System.out.printf("%s: force yield occured\n", Thread.currentThread().getName());
        Thread.yield();
        System.out.printf("%s: withYield on %s, %d\n", Thread.currentThread().getName(), this.getName(), n3++);
    }

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            withSync();
            withoutSync();
            withYield();
            System.out.printf("%s: normal yield occured\n", Thread.currentThread().getName());
            Thread.yield();
        }
    }
}