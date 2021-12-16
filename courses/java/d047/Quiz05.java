package d047;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class Student {
    String name, major;
    int id;
    double gpa;

    Student(String input) {
        var info = input.split(", ");
        name = info[0];
        major = info[1];
        id = Integer.parseInt(info[2]);
        gpa = Double.parseDouble(info[3]);
    }

    void show() {
        System.out.println("name:" + name);
        System.out.println("major:" + major);
        System.out.println("id:" + id);
        System.out.println("gpa:" + gpa);
        System.out.println("-----------------");
    }

    @Override
    public String toString() {
        return String.format("%s, %s, %d, %f", name, major, id, gpa);
    }
}

class Quiz05 {
    public static void main(String[] args) {
        var n = 4;
        var sc = new Scanner(System.in);
        // for ArrayList
        var data = new ArrayList<Student>();
        System.out.println("enter name, major, id, GPA");
        while (n-- > 0) {
            System.out.print(">>");
            data.add(new Student(sc.nextLine()));
        }
        System.out.println("-----------------");
        data.forEach(Student::show);
        while (true) {
            System.out.print("student name>>");
            var temp = sc.next();
            if (temp.equals("stop"))
                break;
            data.stream().filter(i -> i.name.equals(temp)).forEach(System.out::println);
        }
        // for HashMap
        var data2 = new HashMap<String, Student>();
        data.forEach(i -> data2.put(i.name, i));
        while (true) {
            System.out.print("student name>>");
            var temp = sc.next();
            if (temp.equals("stop"))
                break;
            System.out.println(data2.get(temp));
        }
        sc.close();
    }
}
