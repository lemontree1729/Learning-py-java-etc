// practice 1
function findMaxValue(...args: Array<any>) {
    return args.filter((v: any) => typeof v === "number")
        .reduce((a: number, b: number) => a > b ? a : b)
}

// 테스트 케이스 
console.log(findMaxValue(-3, 7, -345, 41, 9, 137, 69))
console.log(findMaxValue(-31, 8, null, -26, false, 92, {}, 284, 923, [], "2045.8", 'zip', 54, "1024"))

// practice 2
function Movie(this: any, title: string, author: string, release: string) {
    this.title = title
    this.author = author
    this.release = release

    this.printMovieInfo = () => {
        const getInfo = () => {
            return `${this.title}-${this.author}는 ${this.release}에 발매되었다.`
        }
        console.log(getInfo())
    }
}

const movie = new (Movie as any)("해리포터", "조앤K롤링", "2003 년 3월 23일")
movie.printMovieInfo()

// practice 3
function getDistance(...args: any) {
    if (args.length === 0)
        return 0
    if (args.length === 1)
        return Math.sqrt(args[0].x ** 2 + args[0].y ** 2)
    return Math.sqrt((args[0].x - args[1].x) ** 2 + (args[0].y - args[1].y) ** 2)
}
console.log(getDistance({ x: 3, y: 2 }, { x: 8, y: 14 }))
console.log(getDistance({ x: 3, y: 4 }))

// practice 4
function countDuplication(...args: Array<string>) {
    const keyword = args.splice(0, 1)[0]
    return args.filter(v => v === keyword).length
}

console.log(countDuplication('cat', 'apple', 'cat', 'tiger', 'cat', 'water', 'computer', 'cat', 'lion', 'pear', 'cat'))

// practice 5
function add(...args: any) {
    return args.filter((v: any) => ["number", "string"].includes(typeof v) && !isNaN(parseFloat(v)))
        .reduce((a: any, b: any) => parseFloat(a) + parseFloat(b), 0)
}
// 테스트 케이스
console.log(add(3, null, 19, false, '9', [], 7, {}, '', 34, 'earth', '3.9')) // 75.9

// practice 6
function divider(...args: Array<number>) {
    const keyword = args.splice(0, 1)[0]
    if (keyword === 0)
        return args
    return args.map(v => v / keyword)
}

// 테스트 케이스
console.log(divider(2, 39, 4, 7, 28, 62, 28))
console.log(divider(0, 39, 4, 7, 28, 62, 28))

// practice 7
const numbers = [121, 23, 345, 43, 59]

function pickIndex(len: number) {
    return Math.floor(Math.random() * len)
}
function shuffle(arr: Array<number>) {
    const n = arr.length
    arr.forEach((v, i, e) => {
        const rand = pickIndex(n)
        e[i] = e[rand]
        e[rand] = v
    })
    return arr
}
console.log(shuffle(numbers))

