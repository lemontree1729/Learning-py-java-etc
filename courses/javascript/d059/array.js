const problem1 = Array.from({ length: 100 }, (v, i) => (i + 1) % 3 ? 0 : i + 1)
console.log(problem1)
const alphabet = Array.from({ length: 26 }, (v, i) => String.fromCharCode('a'.charCodeAt(0) + i))
console.log(alphabet)
let temp = ""
const problem2 = Array.from({ length: 26 }, (v, i) => temp += alphabet[i])
console.log(problem2)
const problem3 = Array.from({ length: 10 }, (v, i) => 3 * (i + 1))
console.log(problem3)
function randomStr(n) {
    return Array.from({ length: n }, () => alphabet[Math.floor(Math.random() * 26)])
}
const problem4 = randomStr(4)
console.log(problem4)
// problem5
problem3.forEach((v, i) => problem3[i] = v % 6 ? problem3[i] : null)
console.log(problem3)
// problem6
let movies = [
    { title: 'Harry Potter', release: '2003-02-22' },
    { title: 'Indiana Jhones', release: '2009-01-09' },
    { title: 'Jurassic Park', release: '2007-04-13' },
    { title: 'Iron man', release: '2012-12-18' },
    { title: 'Spider man', release: '2017-03-07' }
]
let movies_copied = []

movies.forEach((v, i) => movies_copied[i] = Object.assign({}, v))

movies[1].title = "syleemomo"
console.log(movies)
console.log(movies_copied)
console.log("word".split(""))
// problem7
const words = [
    'abc', 'animal', 'fruit', 'abba',
    'abcba', 'location', 'radar', 'madam', 'mario', 'level'
]
function isPalindrome(word) {
    return word.split("").filter((v, i) => v !== word[word.length - i - 1]).length === 0
}
console.log(words.filter(v => isPalindrome(v)).length)

let test = { 0: 'a', 1: 'b' }
console.log(Array.isArray(words), Array.from(test), Array.isArray(Object.values(test)))