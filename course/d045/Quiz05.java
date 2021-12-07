package d045;

import java.util.Calendar;

class Quiz05 {
    public static void main(String[] args) {
        Calendar cal = Calendar.getInstance();
        int minute = cal.get(Calendar.MINUTE);
        int hour = cal.get(Calendar.HOUR_OF_DAY);
        System.out.println("current time is " + hour + ":" + minute);
        if (4 <= hour && hour < 12)
            System.out.println("Good Morning");
        else if (hour < 18)
            System.out.println("Good Afternoon");
        else if (hour < 22)
            System.out.println("Good Evening");
        else
            System.out.println("Good Night");
    }
}
