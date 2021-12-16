package d019;

class MyTv {
    boolean isPowerOn;
    int channel, volume;

    final int MAX_VOLUME = 100, MIN_VOLUME = 0;
    final int MAX_CHANNEL = 100, MIN_CHANNEL = 1;

    void turnOnOff() {
        isPowerOn = !isPowerOn;
    }

    void volumeUp() {
        volume += volume < MAX_VOLUME ? 1 : 0;
    }

    void volumeDown() {
        volume -= volume > MIN_VOLUME ? 1 : 0;
    }

    void channelUp() {
        channel = channel == MAX_CHANNEL ? MIN_CHANNEL : channel++;
    }

    void channelDown() {
        channel = channel == MIN_CHANNEL ? MAX_CHANNEL : channel--;
    }
}

class Exercise6_21 {
    public static void main(String[] args) {
        MyTv t = new MyTv();
        t.channel = 100;
        t.volume = 0;
        System.out.println("CH: " + t.channel + ", VOL: " + t.volume);
        t.channelDown();
        t.volumeDown();
        System.out.println("CH: " + t.channel + ", VOL: " + t.volume);
        t.volume = 100;
        t.channelUp();
        t.volumeUp();
        System.out.println("CH: " + t.channel + ", VOL: " + t.volume);
    }
}
