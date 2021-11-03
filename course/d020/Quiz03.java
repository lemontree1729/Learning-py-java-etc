package d020;

class Song {
    String title, artist, country;
    int year;

    Song() {

    }

    Song(String title, String artist, int year, String country) {
        this.title = title;
        this.artist = artist;
        this.year = year;
        this.country = country;
    }

    void show() {
        System.out.println(title + ", song by " + artist + " in " + year + " whose country is " + country);
    }
}

class Quiz03 {
    public static void main(String[] args) {
        Song song = new Song("Dancing Queen", "ABBA", 1978, "Sweden");
        song.show();
    }
}
