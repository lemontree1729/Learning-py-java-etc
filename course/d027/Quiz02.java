package d027;

class IPTV extends ColorTV {
    private String ip;

    IPTV(String ip, int size, int pixel) {
        super(size, pixel);
        this.ip = ip;
    }

    void printProperty() {
        System.out.print("my IPTV is " + ip + " ip address ");
        super.printProperty();
    }
}

public class Quiz02 {
    public static void main(String[] args) {
        IPTV iptv = new IPTV("192.1.1.2", 32, 2048);
        iptv.printProperty();
    }
}
