fn main() {
    //----------------------------------Scalar Types
    //Integer Types
    let i = 98_222;
    println!("The value of i is: {}", i);
    let j = 0o77;
    println!("The value of j is: {}", j);
    println!("The value of i/j is: {}", i / j);
    // let k: i8 = 127;
    // println!("The value of k is: {}", k + 5);
    //Rust checks for integer overflow!

    //Floating-Point Types
    let x = 2.0;
    println!("The value of x is: {}", x);
    // println!(i / x); // error with not a string
    // println!("{}", i / x); // error with different type division

    //Boolean Type
    // let t = true;

    //Character Type
    let c = 'z';
    let heart_eyed_cat = '😻'; //can use any Unicode letters
    println!("{}{}", c, heart_eyed_cat);

    //----------------------------------Compount Types
    //Tuple Type: fixed size with a variety of types
    let tup = (500, 6.4, 1);
    let (x, y, z) = tup;
    println!(
        "The value of tup.0, x, y, z is: {}, {}, {}, {}",
        tup.0, x, y, z
    );
    //Array Type: fixed size with same type varibales
    let a = [3; 5]; // same as [3, 3, 3, 3, 3]
    println!("The value of a[0] is: {}", a[0])
    //useful when we want data allocated on the stack(rather than heap)
    //Rust ckecks for index overloading!
}
