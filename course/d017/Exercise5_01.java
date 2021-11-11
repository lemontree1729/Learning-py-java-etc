package d017;

class Exercise5_01 { // how to declare variable
    public static void main(String[] args) {
        int[] a[]; // possible
        int[] b = { 1, 2, 3, }; // possible
        int[] c = new int[5]; // possible
        // int[] d = new int[5] { 1, 2, 3, 4, 5 }; impossible!
        // int e[5]; impossible!
        int[] f[] = new int[3][]; // possible
        a = f = null;
        b = c = null;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(f);
    }
}
