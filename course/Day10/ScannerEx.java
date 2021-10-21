import java.util.Scanner;

public class ScannerEx {
    public static void main(String[] args) {
        String[] info = { "name", "city of origin", "weight", "single or not" };
        System.out.println("enter " + String.join(", ", info) + " seperated with spacebar");
        Scanner sc = new Scanner(System.in);
        for (String data : info) {
            System.out.println(data + " : " + sc.next());
        }
        sc.close();
    }
}