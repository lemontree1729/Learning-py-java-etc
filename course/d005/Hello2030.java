package d005;

class Hello2030 {

	public static void main(String[] args) {
		int n = 2030;
		System.out.println("Hello" + n); // output method
		/*
		 * Calling output method order
		 * 
		 * 1. System is defined as class. 2. out is defined as field in System. 3. And
		 * out is defined as PrintStream which is class 4. println is defined as method
		 * in PrintStream.
		 * 
		 * class : frame that makes objects as instance field : global variable used in
		 * each class, same as member variable method : function in each class
		 * 
		 * print(a) : just print a println(a) : print a + print("\n")
		 */
	}

}
