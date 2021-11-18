package d032;

class MyTv2 {
    private boolean isPowerOn = false;
    private int channel;
    private int volume;
    final int MAX_VOLUME = 100;
    final int MIN_VOLUME = 0;
    final int MAX_CHANNEL = 100;
    final int MIN_CHANNEL = 1;

    void turnOnOff() {
        isPowerOn = !isPowerOn;
    }

    void setChannel(int n) {
        if (n > MAX_CHANNEL || n < MIN_CHANNEL)
            return;
        channel = n;
    }

    void setVolume(int n) {
        if (n > MAX_VOLUME || n < MIN_VOLUME)
            return;
        volume = n;
    }

    int getChannel() {
        return channel;
    }

    int getVolume() {
        return volume;
    }
}

class Exercise7_10 {
    public static void main(String[] args) {
        MyTv2 t = new MyTv2();
        t.turnOnOff();
        t.setChannel(10);
        System.out.println("CH: " + t.getChannel());
        t.setVolume(20);
        System.out.println("VOL: " + t.getVolume());
    }
}
