package d030;

abstract class PairMap {
    protected String keyArray[];
    protected String valueArray[];

    abstract String get(String key);

    abstract void put(String key, String value);

    abstract void delete(String key);

    abstract int length();
}

class Dictionary extends PairMap {
    private int cap;

    Dictionary(int n) {
        keyArray = new String[n];
        valueArray = new String[n];
        cap = n;
    }

    String get(String key) {
        for (int i = 0; i < cap; i++) {
            if (key.equals(keyArray[i])) {
                return valueArray[i];
            }
        }
        return null;
    }

    void put(String key, String value) {
        boolean redundancy = false;
        for (int i = 0; i < cap; i++) {
            if (key.equals(keyArray[i])) {
                valueArray[i] = value;
                redundancy = true;
                break;
            }
        }
        if (!redundancy) {
            if (length() == cap) {
                System.out.println("error: Cannot put. Capacity is already max");
            } else {
                for (int i = 0; i < cap; i++) {
                    if (keyArray[i] == null) {
                        keyArray[i] = key;
                        valueArray[i] = value;
                        break;
                    }
                }
            }
        }
    }

    void delete(String key) {
        for (int i = 0; i < cap; i++) {
            if (key.equals(keyArray[i])) {
                keyArray[i] = null;
                valueArray[i] = null;
                break;
            }
        }
    }

    int length() {
        int cnt = 0;
        for (int i = 0; i < cap; i++) {
            if (keyArray[i] != null) {
                cnt++;
            }

        }
        return cnt;
    }
}

public class Quiz10 {
    public static void main(String[] args) {
        Dictionary dic = new Dictionary(10);
        dic.put("a", "java");
        dic.put("b", "python");
        dic.put("c", "C++");
        System.out.println("value of c is " + dic.get("c"));
        System.out.println("value of b is " + dic.get("b"));
        dic.delete("b");
        System.out.println("value of b is " + dic.get("b"));
    }
}
