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

    int getIndex(String key) {
        // getting index of key for keyArray
        // on average, this method's time complexity is twice larger than using for-break
        for (int i = 0; i < cap; i++) {
            if (key == null) {
                if (keyArray[i] == null) {
                    return i;
                }
            } else {
                if (key.equals(keyArray[i])) {
                    return i;
                }
            }
        }
        return -1;
    }

    String get(String key) {
        int keyIndex = getIndex(key);
        if (keyIndex < 0) {
            return null;
        }
        return valueArray[keyIndex];
    }

    void put(String key, String value) {
        int keyIndex = getIndex(key), nullIndex = getIndex(null);
        if (keyIndex >= 0) {
            valueArray[keyIndex] = value;
        } else {
            if (length() == cap) {
                System.out.println("error: Cannot put. Capacity is already max");
            } else {
                keyArray[nullIndex] = key;
                valueArray[nullIndex] = value;
            }
        }
    }

    void delete(String key) {
        int keyIndex = getIndex(key);
        if (keyIndex >= 0) {
            keyArray[keyIndex] = null;
            valueArray[keyIndex] = null;
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
