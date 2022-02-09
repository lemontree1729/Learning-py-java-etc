// Lexical scope
const fruit = 'apple'
function printA() {
    const fruit = 'banana'
    printB()
}
function printB() {
    console.log(fruit)
}
printA() // apple
printB() // apple

// Callback function

// Closure
// Currying
// Module pattern
function singleton() {
    let list = []
}
