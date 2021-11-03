package d020;

class TV {
    String manufacturer;
    int year, inch;

    TV(String manufacturer, int year, int inch) {
        this.manufacturer = manufacturer;
        this.year = year;
        this.inch = inch;
    }

    void show() {
        System.out.println("made by " + manufacturer + ", " + year + " model, " + inch + " inches");
    }
}

public class Quiz01 {

    public static void main(String[] args) {
        TV myTV = new TV("LG", 2017, 32);
        myTV.show();
    }
}
