package model;

public class TestModel extends Model {
    final String key[] = { "name", "email", "address", "hobby", "tel", "age" };

    public TestModel(int n) {
        for (int i = 0; i < n; i++) {
            String[] value = new String[6];
            dataBase.put(i);
            for (int j = 0; j < 6; j++) {
                if (j == 5)
                    value[j] = Integer.toString((int) (Math.random() * 10));
                else
                    value[j] = Character.toString('a' + (int) (Math.random() * 26));
                dataBase.put(i, key[j], value[j]);
            }
        }
    }
}
