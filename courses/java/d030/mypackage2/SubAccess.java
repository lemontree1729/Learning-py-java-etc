package d030.mypackage2;

import d030.mypackage1.*;

// class SubAccess extends DefaultTest
// error: The type DefaultAccess is not visible

class SubAccess1 extends PublicAccess {
    public static void main(String[] args) {
        // int a = PrivateAccess.pub;
        // error: The type PrivateAccess is not visible

        // int a = DefaultAccess.pub;
        // error: The type DefaultAccess is not visible

        // int a = ProtectedAccess.pri;
        // error: The field PublicAccess.ProtectedAccess.pri is not visible
        // int a = ProtectedAccess.def;
        // error: The field PublicAccess.ProtectedAccess.def is not visible
        // int a = ProtectedAccess.pro;
        // error: The field PublicAccess.ProtectedAccess.pro is not visible
        int a = ProtectedAccess.pub;

        // int b = pri;
        // error: The field PublicAccess.pri is not visible
        // int c = def;
        // error: The field PublicAccess.def is not visible
        int b = pro;
        int c = pub;
        System.out.println(a + b + c);
    }
}