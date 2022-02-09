// practice1
const fruit = 'apple'
let printB: any = null

function printA() {
    const fruit = 'banana'
    printB = function () {
        console.log(fruit)
    }
    printB()
}

printA() // banana
printB() // banana

// practice2
const friendss = [
    { name: 'victoria', age: 13, city: 'seoul' },
    { name: 'sun', age: 34, city: 'busan' },
    { name: 'johseb', age: 25, city: 'busan' },
    { name: 'syleemomo', age: 9, city: 'seoul' },
    { name: 'hannah', age: 41, city: 'daegu' },
    { name: 'shara', age: 37, city: 'seoul' },
    { name: 'martin', age: 28, city: 'daegu' },
    { name: 'gorgia', age: 39, city: 'seoul' },
    { name: 'nana', age: 24, city: 'busan' },
    { name: 'dannel', age: 19, city: 'seoul' },
]
function filter(func: Function, array: Array<any>) {
    return array.filter(v => func(v))
}
function filterSeoul(info: any) {
    if (info.city === "seoul")
        return true
    return false
}
const seoulFriends = filter(filterSeoul, friendss)
console.log(seoulFriends)

// practice3

function add(a: number, b: number) {
    return a + b
}
function subtract(a: number, b: number) {
    return a - b
}
function multiply(a: number, b: number) {
    return a * b
}
function divider(a: number, b: number) {
    return a / b
}
function pow(a: number, b: number): number {
    return b ? multiply(a, pow(a, b - 1)) : 1
}

function calculator(mode: string, a: number, b: number, ...funcs: Array<Function>) {
    let ret = null
    switch (mode) {
        case '+':
            ret = funcs[0](a, b)
            break
        case '-':
            ret = funcs[1](a, b)
            break
        case '*':
            ret = funcs[2](a, b)
            break
        case '/':
            ret = funcs[3](a, b)
            break
        case '^':
            ret = funcs[4](a, b)
            break
    }
    return ret
}

// 테스트 케이스
const ret1 = calculator('+', 3, 4, add, subtract, multiply, divider, pow)
const ret2 = calculator('-', 3, 4, add, subtract, multiply, divider, pow)
const ret3 = calculator('*', 3, 4, add, subtract, multiply, divider, pow)
const ret4 = calculator('/', 3, 4, add, subtract, multiply, divider, pow)
const ret5 = calculator('^', 3, 4, add, subtract, multiply, divider, pow)

console.log(ret1)
console.log(ret2)
console.log(ret3)
console.log(ret4)
console.log(ret5)

// practice4
const comment = '너는 진짜 못말리는 바보 똥개 그지다 !'
const insultss = ['바보', '똥개', '그지']
function filterComment(comment: string) {
    function separateStr(str: string, delimeter: string) {
        return str.split(delimeter)
    }
    function filterKeyword(arr: Array<string>, keyword: string) {
        return arr.filter(word => !word.includes(keyword))
    }
    let strSeparated = separateStr(comment, ' ')
    for (let insult of insultss) {
        strSeparated = filterKeyword(strSeparated, insult)
    }
    return strSeparated
}

console.log(filterComment(comment))

// practice5

const animals = ['cat', 'lion', 'turtle', 'dog', 'pig']
const fruits = ['apple', 'banana', 'strawberry', 'pineapple', 'pear']


function searchItem() {
    let _category: Array<string> = []
    return {
        set category(category: Array<string>) {
            _category = category
        },
        getResult: (key: string) => {
            return _category.filter(item => item === key)[0]
        }
    }
}

const category1 = searchItem()
category1.category = animals
console.log(category1.getResult('turtle')) // searchItemInCategory 내부의 category 변수에는 접근하지는 못하지만 외부인자에 의하여 수정이 가능함
console.log(category1.getResult('pig'))
console.log(category1.getResult('banana'))

const category2 = searchItem()
category2.category = fruits
console.log(category2.getResult('strawberry'))
console.log(category2.getResult('apple'))
console.log(category2.getResult('lion'))


// practice 6
const friendsss = [
    { name: 'victoria', age: 13, city: 'seoul' },
    { name: 'sun', age: 34, city: 'busan' },
    { name: 'johseb', age: 25, city: 'busan' },
    { name: 'syleemomo', age: 9, city: 'seoul' },
    { name: 'hannah', age: 41, city: 'daegu' },
    { name: 'shara', age: 37, city: 'seoul' },
    { name: 'martin', age: 28, city: 'daegu' },
    { name: 'gorgia', age: 39, city: 'seoul' },
    { name: 'nana', age: 24, city: 'busan' },
    { name: 'dannel', age: 19, city: 'seoul' },
]

function Persons(this: any, name: string, age: number, city: string, friends: any) {
    this.name = name
    this.age = age
    this.city = city

    // 초기값이 배열이나 객체인 경우 깊은복사로 저장 및 조회하기
    let _friends = JSON.parse(JSON.stringify(friends)) // 전역변수 friends 는 참조만 하고 프라이빗 변수 _friends 는 외부에서 변경하지 못하도록 깊은복사로 저장함

    this.getFriends = function () {
        return JSON.parse(JSON.stringify(_friends)) // 프라이빗 변수 _friends 를 보호하기 위하여 깊은복사로 조회함
    }
}
Persons.prototype = {
    get friends() {
        return this.getFriends()
    },
    filterFriendsInMyCity() {
        return this.friends.filter((friend: any) => friend.city === this.city)
    },
}


const person = new (Persons('영희', 23, 'daegu', friendsss) as any)

console.log(person.friends === friends) // 전역변수 friends 와 프라이빗변수 _friends 주소가 다름을 확인함 (복사본을 저장하기 때문)
person.friends[0].name = "태양" // 프라이빗 변수 _friends 를 변경하지 못함 (복사본을 조회하기 때문)

console.log(person.friends)
console.log(person.filterFriendsInMyCity())

const person2 = new (Persons('철수', 35, 'seoul', friendsss) as any)
console.log(person2.friends)
console.log(person2.filterFriendsInMyCity())