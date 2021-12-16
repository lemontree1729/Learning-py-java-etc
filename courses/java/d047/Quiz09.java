package d047;

import java.util.Vector;

interface IStack<T> {
    T pop();

    boolean push(T ob);
}

class MyStack<T> implements IStack<T> {
    Vector<T> stack = new Vector<T>();

    public T pop() {
        if (stack.size() == 0)
            return null;
        T temp = stack.get(stack.size() - 1);
        stack.remove(temp);
        return temp;
    }

    public boolean push(T ob) {
        stack.add(ob);
        return true;
    }
}

class Quiz09 {
    public static void main(String[] args) {
        IStack<Integer> stack = new MyStack<Integer>();
        for (int i = 0; i < 10; i++)
            stack.push(i);
        while (true) {
            Integer n = stack.pop();
            if (n == null)
                break;
            System.out.print(n + " ");
        }
    }
}
