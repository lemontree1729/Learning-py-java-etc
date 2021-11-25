package d035.myMMS;

class Model {
    DB dataBase = new DB();

    String toString(int id) {
        String result = id + "-->";
        for (String key : dataBase.getKeySet(id))
            result += String.format("[%s: %s]", key, dataBase.get(id));
        return result;
    }

    String[] getData(int id) {
        String result[] = new String[dataBase.getKeySet(id).size()];
        int cnt = 0;
        for (String key : dataBase.getKeySet(id))
            result[cnt++] = dataBase.get(id, key);
        return result;
    }

    void putData(int id, String key[], String value[]) {
        for (int i = 0; i < key.length; i++)
            dataBase.put(id, key[i], value[i]);
    }

    String[] getAll() {
        String result[] = new String[dataBase.getKeySet().size()];
        int cnt = 0;
        for (int id : dataBase.getKeySet())
            result[cnt++] = toString(id);
        return result;
    }

    void update() {

    }

    void delete() {

    }

    void search() {

    }
}
