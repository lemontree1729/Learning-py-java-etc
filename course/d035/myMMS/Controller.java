package d035.myMMS;

import java.util.InputMismatchException;
import java.util.Scanner;

class Controller {
    public static void main(String[] args) {
        MainController main = new MainController();
        main.initialize();
        main.run();
    }
}

class MainController {
    Model model;
    Scanner sc;

    void run() {
        boolean stop = false;
        Integer toggle = 0;
        do {
            MainUI.call();
            toggle = Validate.inint(sc, 1, 6);
            if (toggle == null)
                continue;
            switch (toggle) {
            case 1:
                register();
                break;
            case 2:
                show();
                break;
            case 3:
                update();
                break;
            case 4:
                delete();
                break;
            case 5:
                search();
                break;
            case 6:
                initialize();
                break;
            case 7:
                stop = true;
                MainUI.printExit();
                break;
            }
        } while (!stop);
    }

    void register() {
        String key[] = { "name", "email", "address", "hobby", "tel", "age" };
        String value[] = new String[6];
        ControlUI.registerInit();
        ControlUI.getID();
        Integer id = Validate.isint(sc);
        boolean a = Validate.existid(id, model);
        for (int i = 0; i < key.length; i++) {
            ControlUI.getData(i);
            if (i == 5)
                value[i] = Integer.toString(Validate.isint(sc));
            else
                value[i] = sc.next();
        }
        model.putData(id, key, value);
    }

    void show() {
        ControlUI.showInit();
        String result[] = model.getAll();
        for (String text : result)
            View.output(text + "\n");
    }

    void update() {
        String key[] = { "name", "email", "address", "hobby", "tel", "age" };
        String newValue[] = new String[6];
        ControlUI.registerInit();
        ControlUI.getID();
        int id = Validate.isint(sc);
        String oldValue[] = model.getData(id);
        for (int i = 0; i < key.length; i++) {
            ControlUI.showData(i, oldValue[i]);
            ControlUI.getData(i);
            if (i == 5)
                newValue[i] = Integer.toString(Validate.isint(sc));
            else
                newValue[i] = sc.next();
            model.putData(id, key, newValue);
        }
    }

    void delete() {

    }

    void search() {

    }

    void initialize() {
        model = new Model();
        sc = new Scanner(System.in);
    }
}

class Validate {
    static boolean keepContinue(Scanner sc) {
        ControlUI.keepContinue();
        if (sc.next().equals("Y"))
            return true;
        return false;
    }

    static Integer isint(Scanner sc) {
        int cnt = 0;
        do {
            try {
                return sc.nextInt();
            } catch (InputMismatchException e) {
                sc.nextLine();
                if (!Validate.keepContinue(sc))
                    break;
                if (cnt < 3)
                    SubUI.notIntError1();
                else
                    SubUI.notIntError2();
                cnt++;
            }
        } while (true);
        return null;
    }

    static Integer inint(Scanner sc, int n, int m) {
        int num, temp;
        if (n > m) {
            temp = n;
            n = m;
            m = temp;
        }
        do {
            num = isint(sc);
            if (n <= num && num <= m)
                return num;
            if (!Validate.keepContinue(sc))
                break;
            SubUI.intRangeError(num, n, m);
        } while (true);
        return null;
    }

    static boolean existid(int id, Model model) {
        model.getData(id);
        return false;
    }
}