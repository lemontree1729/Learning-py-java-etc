// package (name);  package that you include(possible to define same class name with different package)
/**
 * class that has sum(add a to b)
 * 
 * AND THIS IS COMMANT
 */
public class Hello { // declare class and class name as "Hello"
	public static int sum(int i, int j) { // declare method, name "sum",output type and input with type
		return i + j; // return int as i + j
	}
	public static void main(String[] args) { // you should declare input String[] (name). else, compiler can't find main function
		int i;
		int j;
		char a;
		String b;
		final int TEN = 10; // make value of variable TEN fixed
		i = 1;
		j = sum(i, TEN);
		a = '?';
		b = "Hello";
		java.lang.System.out.println(a);
		System.out.println(b);
		System.out.println(TEN);
		System.out.println(j);
	}
}
