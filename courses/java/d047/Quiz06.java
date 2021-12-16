package d047;

import java.util.HashMap;
import java.util.Scanner;

class Location {
    String city;
    int latitude, longitude;

    Location(String city, int latitude, int longitude) {
        this.city = city;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public String toString() {
        return String.format("%-5s%-5d%-5d", city, latitude, longitude);
    }
}

class Quiz06 {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var data = new HashMap<String, Location>();
        System.out.println("enter city, latitude, longitude");
        for (int i = 0; i < 4; i++) {
            System.out.print(">>");
            var input = sc.nextLine().split(", ");
            data.put(input[0], new Location(input[0], Integer.parseInt(input[1]), Integer.parseInt(input[2])));
        }
        System.out.println("-------------");
        data.forEach((name, location) -> System.out.println(location));
        System.out.println("-------------");
        while (true) {
            System.out.print("city name>>");
            var temp = sc.nextLine();
            if (temp.equals("stop"))
                break;
            if (!data.containsKey(temp))
                System.out.println(temp + " not exist");
            else
                System.out.println(data.get(temp));
        }
        sc.close();
    }
}
