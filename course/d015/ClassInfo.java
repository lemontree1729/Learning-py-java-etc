package d015;

import java.lang.reflect.*;

class ClassInfo {
    static void findInfo(Object obj) {
        Class<?> cls = obj.getClass();
        Method[] mets = cls.getMethods();
        Method[] demets = cls.getDeclaredMethods();
        Field[] flds = cls.getFields();
        Field[] deflds = cls.getDeclaredFields();
        System.out.println("Class name: " + obj.getClass());
        for (Method met : mets) {
            System.out.println("Methods: " + met);
        }
        for (Method demet : demets) {
            System.out.println("Declared Methods: " + demet);
        }
        for (Field fld : flds) {
            System.out.println("Fields: " + fld);
        }
        for (Field defld : deflds) {
            System.out.println("Declared Fields: " + defld);
        }
    }

    public static void main(String[] args) {
        String a = "asdfas";
        findInfo(a);
    }
}
