package d025;

import d020.*;

class A {
    String name = "syj";

}

class B extends A {
    int age = 27;

}

class C extends B {
    boolean solo = true;
}

class ClassTest extends Quiz01 {
    static void showins(Object any) {
        System.out.println(any instanceof A);
        System.out.println(any instanceof B);
        System.out.println(any instanceof C);
    }

    public static void main(String[] args) {
        A a0 = new A(); // information : name = "syj"
        B b0 = new B(); // information : name = "syj", age = 27
        C c0 = new C(); // information : name = "syj", age = 27, solo = true
        /*
         * B b1 = (C) a0; makes error because a0 is declared as class A (there is no
         * information for C(for example, int date) in a0)
         */
        A a1 = c0;
        B b1 = (C) a1;
        C c1 = (C) b1;
        showins(a0);
        showins(b0);
        showins(c0);
        showins(a1);
        showins(b1);
        showins(c1);
    }
}