package d032;

public class StringStack implements Stack {
    private String[] stk;
    private int tos;

    public StringStack(int cap) {
        stk = new String[cap];
        tos = -1;
    }

    @Override
    public int length() {
        return tos + 1;
    }

    @Override
    public int capacity() {
        return stk.length;
    }

    @Override
    public String pop() {
        if (tos == -1) {
            return null;
        }
        tos--;
        return stk[tos + 1];
    }

    public boolean push(String str) {
        if (tos == stk.length - 1) {
            return false;
        } else {
            tos++;
            stk[tos] = str;
            return true;
        }
    }
}
