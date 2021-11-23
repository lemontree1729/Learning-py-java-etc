package d035.myMMS;

import java.util.HashMap;
import java.util.LinkedHashMap;

class PersonalData extends LinkedHashMap<String, String> {
    public String toString() {
        String result = "";
        for (String key : this.keySet())
            result += String.format("[%s: %s]", key, this.get(key));
        return result;
    }
}

class MMSData {
    HashMap<String, PersonalData> dataBase = new HashMap<String, PersonalData>();

    void makeId(String id) {
        PersonalData info = new PersonalData();
        dataBase.put(id, info);
    }

    PersonalData get(String id) {
        return dataBase.get(id);
    }
}
