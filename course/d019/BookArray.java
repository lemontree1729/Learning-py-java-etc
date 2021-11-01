import java.util.Scanner;

class Book{
	String title, author;
	public Book(String title, String author) {
		this.title = title;
		this.author = author;
	}
}

public class BookArray {
	public static void main(String[] args) {
		Book[] book = new Book[4];
		Scanner sc = new Scanner(System.in);
		String title;
		for(int i=0;i<book.length;i++) {
			System.out.print("title>>");
			title = sc.nextLine();
			System.out.println(System.identityHashCode(title));
			System.out.print("author>>");
			String author = sc.nextLine();
			System.out.println(System.identityHashCode(author));
			book[i] = new Book(title, author);
		}
		
		for(int i=0; i<book.length; i++) {
			System.out.println("("+book[i].title + ", " + book[i].author + ")");
		}
		sc.close();
	}
}
