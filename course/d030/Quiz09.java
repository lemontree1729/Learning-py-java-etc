package d030;

import java.util.Scanner;

interface Stack {
    int length();

    int capacity();

    String pop();

    void push(String val);
}

class StringStack implements Stack {
    String stack[];

    StringStack(int n) {
        stack = new String[n];
    }

    public int length() {
        int i = 0;
        while (i < capacity() && stack[i] != null) {
            i++;
        }
        return i;
    }

    public int capacity() {
        return stack.length;
    }

    public String pop() {
        if (length() == 0) {
            return "";
        }
        String a = new String(stack[length() - 1]);
        stack[length() - 1] = null;
        return a;
    }

    public void push(String val) {
        if (length() == capacity()) {
            System.out.println("error: Cannot push. Capacity is already max");
        } else {
            stack[length()] = val;
        }
    }
}

class Quiz09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the capacity of stack >> ");
        StringStack myStack = new StringStack(sc.nextInt());
        String element = "";
        while (true) {
            System.out.print("Enter the element >> ");
            element = sc.next();
            if (element.equals("stop")) {
                break;
            }
            myStack.push(element);
        }
        System.out.print("pop all >> ");
        while (myStack.length() > 0) {
            System.out.print(myStack.pop() + " ");
        }
        System.out.println();
        sc.close();
    }
}
