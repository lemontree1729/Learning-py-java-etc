package d032;

class Exercise7_18 {
    static void action(Robot r) {
        if (r instanceof DanceRobot) {
            ((DanceRobot) r).dance();
        }
        if (r instanceof SingRobot) {
            ((SingRobot) r).sing();
        }
        if (r instanceof DrawRobot) {
            ((DrawRobot) r).draw();
        }

    }

    public static void main(String[] args) {
        Robot[] arr = { new DanceRobot(), new SingRobot(), new DrawRobot() };
        for (int i = 0; i < arr.length; i++)
            action(arr[i]);
    }
}

class Robot {
}

class DanceRobot extends Robot {
    void dance() {
        System.out.println("Dancing!");
    }
}

class SingRobot extends Robot {
    void sing() {
        System.out.println("singing!");
    }
}

class DrawRobot extends Robot {
    void draw() {
        System.out.println("Drawing!");
    }
}