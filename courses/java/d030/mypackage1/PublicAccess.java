package d030.mypackage1;

class DefaultTest {
    // static private int pri = 1;
    static int def = 2;
    static protected int pro = 3;
    static public int pub = 4;
}

public class PublicAccess {
    // private class PrivateAccess {
    // static private int pri = 1;
    // static int def = 2;
    // static protected int pro = 3;
    // static public int pub = 4;
    // }

    class DefaultAccess {
        // static private int pri = 1;
        static int def = 2;
        static protected int pro = 3;
        static public int pub = 4;
    }

    protected class ProtectedAccess {
        // static private int pri = 1;
        static int def = 2;
        static protected int pro = 3;
        static public int pub = 4;
    }

    // static private int pri = 1;
    static int def = 2;
    static protected int pro = 3;
    static public int pub = 4;
}