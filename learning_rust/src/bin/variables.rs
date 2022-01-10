fn main() {
    // Declaring(let, let mut and const)
    let mut x = 5; // mutable variable
    println!("The value of x is: {}", x);
    x = 6; // can mut
    println!("The value of x is: {}", x);
    const Y: u32 = 5; // constant(must declare the type)
    println!("The value of Y is: {}", Y);
    let z = 5;
    let z = z + 1; // shadowing
    println!("The value of z is: {}", z);
    // let mut spaces = "   ";
    // spaces = spaces.len();
    // not work because we can't change type of declared variable
    let spaces = "   ";
    let spaces = spaces.len();
    println!("The value of spaces is: {}", spaces);
}
