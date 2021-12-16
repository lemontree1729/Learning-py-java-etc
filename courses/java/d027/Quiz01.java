package d027;

class TV {
    private int size;

    TV(int size) {
        this.size = size;
    }

    protected int getSize() {
        return size;
    }

}

class ColorTV extends TV {
    private int pixel;

    ColorTV(int size, int pixel) {
        super(size);
        this.pixel = pixel;
    }

    void printProperty() {
        System.out.println(getSize() + "inch " + pixel + "color");
    }
}

public class Quiz01 {
    public static void main(String[] args) {
        ColorTV myTV = new ColorTV(32, 1024);
        myTV.printProperty();
    }
}
