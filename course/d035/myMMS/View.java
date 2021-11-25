package d035.myMMS;

class MainUI {
    static void call() {
        System.out.println("=====member menu=====");
        System.out.println("1. member register");
        System.out.println("2. member list");
        System.out.println("3. member update");
        System.out.println("4. member delete");
        System.out.println("5. member search");
        System.out.println("6. exit program");
        System.out.print("menu to go: ");
    }

    static void printExit() {
        System.out.println("program exit");
    }

    static void printIntError(int a) {
        System.out.println(a + " is not in 1~6");
    }
}

class ControlUI {
    static void keepContinue() {
        System.out.print("Wrong input! keep continue?(Y/N): ");
    }

    static void registerInit() {
        System.out.println("=====new member register=====");
    }

    static void getID() {
        System.out.print("new id: ");
    }

    static void getData(int n) {
        if (n == 0)
            System.out.print("new name: ");
        else if (n == 1)
            System.out.print("new email: ");
        else if (n == 2)
            System.out.print("new address: ");
        else if (n == 3)
            System.out.print("new hobby: ");
        else if (n == 4)
            System.out.print("new tel: ");
        else if (n == 5)
            System.out.print("new age: ");
    }

    static void showInit() {
        System.out.println("=====showing data=====");
    }

    static void updateInit() {
        System.out.println("=====update member information=====");
    }

    static void showData(int n, String data) {
        if (n == 0)
            System.out.println("name before: " + data);
        else if (n == 1)
            System.out.println("email before: " + data);
        else if (n == 2)
            System.out.println("address before: " + data);
        else if (n == 3)
            System.out.println("hobby before: " + data);
        else if (n == 4)
            System.out.println("tel before: " + data);
        else if (n == 5)
            System.out.println("age before: " + data);
    }
}

class SubUI {
    static void notIntError1() {
        System.out.print("you should enter int: ");
    }

    static void notIntError2() {
        System.out.print("INPUT--->!!INT!!<---: ");

    }

    static void intRangeError(int a, int n, int m) {
        System.out.printf("%d is not in %d~%d: ", a, n, m);
    }
}

class View {
    static void output(String text) {
        System.out.print(text);
    }
}
