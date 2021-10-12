import java.util.Scanner;


public class Scannererr { // error with using both nextInt() method and nextLine()

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String nl = System.getProperty("line.separato");
		
		System.out.println("error code");
		int i = input.nextInt();
		System.out.println(i);
		String s3 = input.nextLine();
		System.out.println(s3);
	}
}
