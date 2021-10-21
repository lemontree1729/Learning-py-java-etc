package d005;

import java.util.Scanner;

public class ScanError { // error with using both nextInt() method and nextLine()

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("error code");
		int i = sc.nextInt();
		System.out.println(i);
		String s3 = sc.nextLine();
		System.out.println(s3);
		sc.close();
	}
}
