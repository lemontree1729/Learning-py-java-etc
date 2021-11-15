console.log("hello world!")

// declare variable(var, let, const)
// var admin = "me"
let admin = "you"
const hello = 1
console.log(admin)

// int types
console.log(10, 0x00ff00, 0o0074, 21.7, -2.9e-37, Infinity, -Infinity, NaN)

const name1 = 'me'
const name2 = 'It\'s' + name1
const name3 = `Not ${name1}` //  It is ``(backtick) not, ''(single quote)
console.log(name1, name2, name3)

const line = 'a\
b\
c'
console.log(line)

const person = {
    name: 'me',
    age: 27,
    isActive: false
}
console.log(person)

const numbers = [0, 1, 2, 4] // array
console.log(numbers)

console.log(typeof 'a', typeof numbers)
console.log(Array.isArray(numbers), Array.isArray(person))
console.log(numbers instanceof Array)
console.log(Number("32"), Number("asdfsaf21"))
console.log(parseInt("41414adsfas"), parseInt("asdfsaf23"))
console.log(person.toString(), numbers.toString())
console.log((31 + "3"), 31 * "3")
console.log(hello.toString())

let price = 360000
let size = 275
const PI = 3.14
const names = "sunrise"
const message = "Happy halloween, "
console.log(message + names)
