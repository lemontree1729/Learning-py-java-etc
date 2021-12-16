package d032;

class MyTv3 extends MyTv2 {
    private int prevChannel;

    @Override
    void setChannel(int n) {
        prevChannel = getChannel();
        super.setChannel(n);
    }

    void gotoPrevChannel() {
        setChannel(prevChannel);
    }
}

public class Exercise7_11 {
    public static void main(String[] args) {
        MyTv3 t = new MyTv3();
        t.setChannel(10);
        System.out.println("CH: " + t.getChannel());
        t.setChannel(20);
        System.out.println("CH: " + t.getChannel());
        t.gotoPrevChannel();
        System.out.println("CH: " + t.getChannel());
        t.gotoPrevChannel();
        System.out.println("VOL: " + t.getChannel());
    }
}
